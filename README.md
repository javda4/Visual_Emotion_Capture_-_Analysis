# Facial Landmark Capture Research Tool

## Overview
This project is a Python-based research tool designed to capture detailed facial landmark data while a participant views controlled visual stimuli such as videos or timed image sequences. Using MediaPipe Face Mesh, the system records 468 facial landmarks (x, y, z coordinates) for each frame of the video.

The program plays a defined visual input while simultaneously collecting facial data and exporting it to CSV files for later statistical or behavioral analysis.

---

## Features
- Captures all 468 facial landmarks from MediaPipe Face Mesh
- Records x, y, z coordinates for every landmark per frame
- Automatically organizes experiment outputs by video name and run number
- Saves captured data to CSV files for easy analysis
- Ends execution automatically when the input video finishes
- Designed for repeatable research experiments

---

## Project Structure

facial_capture_project/

│

├── videos/                # Input videos used for experiments

│   └── example_video.mp4

│

├── outputs/               # Automatically generated experiment results

│   └── example_video_run1/

│       └── landmarks.csv

│

└── capture_script.py      # Main experiment script

---

## Requirements

- Python 3.8+
- opencv-python
- mediapipe
- pandas

Install dependencies:

pip install opencv-python mediapipe pandas

---

## How It Works

1. The program loads a specified video file.
2. The video is played frame-by-frame using OpenCV.
3. For each frame, MediaPipe Face Mesh detects and tracks 468 facial landmarks.
4. The (x, y, z) coordinates of every landmark are recorded.
5. Data is appended to a dataframe during execution.
6. When the video ends, the data is exported to a CSV file.

Each experiment run creates a new folder automatically:

outputs/
video_name_run1/
video_name_run2/
video_name_run3/

This ensures repeated experiments remain organized and reproducible.

---

## CSV Output Format

Each CSV row represents a single video frame.

Example structure:

| frame | x0 | y0 | z0 | x1 | y1 | z1 | ... |
|------|----|----|----|----|----|----|-----|
| 0 | 0.45 | 0.33 | -0.01 | ... |
| 1 | 0.46 | 0.32 | -0.01 | ... |

Total columns:

1 frame column  
+ 468 landmarks × 3 coordinates  
= 1,405 columns per row

---

## Running the Experiment

1. Place a video inside the `videos/` folder.
2. Update the `VIDEO_PATH` variable in the script if needed.
3. Run the program:

python capture_script.py

The program will:
- Display the video during processing
- Capture facial landmark data
- Save the results when the video ends

---

## Potential Research Applications

- Emotion response studies
- Visual stimulus reaction analysis
- Human-computer interaction research
- Behavioral pattern analysis
- Facial movement trend detection

---

## Future Improvements

- Support for image sequence experiments
- Multiple participant session tracking
- Frame timestamp recording
- Automatic batch processing of multiple videos
- Real-time visualization of facial landmark trends

---

## License

This project is intended for research and educational purposes.
