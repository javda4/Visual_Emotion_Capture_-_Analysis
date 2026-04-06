import cv2
import mediapipe as mp
import pandas as pd
import os
import re

# -------------------------
# Configurations
# -------------------------
VIDEO_PATH = "videos/example_video.mp4"
OUTPUT_ROOT = "outputs"

# -------------------------
# Setup MediaPipe
# -------------------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=False)

# -------------------------
# Setup video
# -------------------------
cap = cv2.VideoCapture(VIDEO_PATH)
video_name = os.path.splitext(os.path.basename(VIDEO_PATH))[0]

# -------------------------
# Determine next run counter automatically
# -------------------------
existing_runs = []
if os.path.exists(OUTPUT_ROOT):
    for folder in os.listdir(OUTPUT_ROOT):
        match = re.match(rf"{re.escape(video_name)}_run(\d+)", folder)
        if match:
            existing_runs.append(int(match.group(1)))
next_run = max(existing_runs) + 1 if existing_runs else 1

# Create output folder
output_run_folder = os.path.join(OUTPUT_ROOT, f"{video_name}_run{next_run}")
os.makedirs(output_run_folder, exist_ok=True)

# -------------------------
# Prepare DataFrame
# -------------------------
columns = ["frame"]
for i in range(468):
    columns += [f"x{i}", f"y{i}", f"z{i}"]
df = pd.DataFrame(columns=columns)

frame_counter = 0

# -------------------------
# Process video frames
# -------------------------
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    row = [frame_counter]
    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]
        for lm in face_landmarks.landmark:
            row += [lm.x, lm.y, lm.z]
    else:
        row += [None]*(468*3)  # If no face detected

    df.loc[frame_counter] = row
    frame_counter += 1

    # Optional: show video
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------------
# Save CSV
# -------------------------
csv_path = os.path.join(output_run_folder, "landmarks.csv")
df.to_csv(csv_path, index=False)
print(f"Data saved to {csv_path}")

cap.release()
cv2.destroyAllWindows()
