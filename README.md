🔥 Vision-Based Early Fire Detection System
📌 Overview

This project implements a real-time vision-based fire detection system using camera input and image processing techniques.
The system focuses on detecting actual flame characteristics such as color, brightness, and temporal persistence, enabling early fire detection while minimizing false alarms caused by humans, furniture, or other non-fire objects.

An automated alarm mechanism is triggered once fire is confirmed and continues to ring until the fire condition is cleared.

🎯 Key Features

Real-time fire detection using live camera, video, or image input

Flame-based detection (matchstick, lighter, candle, fire glow)

Stable bounding-box visualization (no flickering)

Continuous alarm until fire is extinguished

Reduced false positives using color and temporal analysis

Lightweight and cost-effective solution

Suitable for early fire warning systems

🧠 Detection Approach

Unlike traditional object detection methods, this system treats fire as a visual phenomenon rather than an object.

The detection pipeline includes:

HSV color analysis for flame-like regions

Brightness filtering to isolate high-intensity areas

Temporal consistency to confirm persistent fire

Region-based visualization for clear interpretation

This approach ensures accurate detection of flames while avoiding incorrect detection of people, furniture, or background objects.

🛠️ Technologies Used

Python

OpenCV

NumPy

Computer Vision & Image Processing

Real-time Video Analysis



▶️ How to Run
1️⃣ Install dependencies

It is recommended to use a virtual environment.

pip install -r requirements.txt

2️⃣ Run using webcam
python yolo.py --webcam

3️⃣ Run using video file
python yolo.py --video --video_path videos/fire1.mp4

4️⃣ Run using image
python yolo.py --image --image_path fire.jpg

