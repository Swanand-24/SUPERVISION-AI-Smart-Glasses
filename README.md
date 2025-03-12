# SUPERVISION - AI Smart Glasses for Visually Impaired People
![image alt](https://github.com/Swanand-24/SUPERVISION-AI-Smart-Glasses/blob/main/images/supervision_prototype.jpg?raw=true)
## Overview
SUPERVISION is an AI-powered wearable device designed to assist visually impaired individuals by providing real-time object detection, obstacle avoidance, and audio feedback. The system leverages **Raspberry Pi 4B**, **Machine Learning**, **Google Text-to-Speech (gTTS)**, and **Ultrasonic Sensors** to process visual and spatial data and convert it into meaningful voice-based guidance.

## Features
- **Real-time Object Detection:** Utilizes MobileNetV2 to identify objects in the user's surroundings.
- **Obstacle Detection:** Ultrasonic sensors detect obstacles within a predefined range.
- **Voice Feedback:** Converts detected objects and obstacles into speech using Google Text-to-Speech (gTTS).
- **Compact and Wearable:** Designed as a lightweight and portable smart glass solution.

## Hardware Components
- **Raspberry Pi 4B (8GB RAM)** - Primary processing unit
- **Sony IMX Camera Module** - Captures real-time video
- **Ultrasonic Sensor (HC-SR04)** - Detects obstacles
- **Croma Power Bank (10000 mAh)** - Provides portable power supply
- **Wired Earphones** - Delivers audio feedback to the user
- **MicroSD Card (32GB)** - Storage for OS and model files

## Software & Technologies Used
- **Operating System:** Raspbian OS
- **Programming Language:** Python 3
- **Machine Learning Model:** MobileNetV2 (Pre-trained on COCO Dataset)
- **Text-to-Speech Engine:** Google Text-to-Speech (gTTS)
- **Deep Learning Framework:** TensorFlow & OpenCV
- **IDE:** Thonny IDE

## System Architecture
1. **Image Capture:** The Sony IMX camera captures frames in real time.
2. **Object Detection:** The MobileNetV2 model processes frames and detects objects.
3. **Obstacle Sensing:** The Ultrasonic sensor measures distances to nearby objects.
4. **Voice Feedback:** Detected objects and obstacle distances are converted to speech using gTTS.
5. **Audio Output:** The processed audio is played through wired earphones.


## How It Works
1. The camera continuously captures frames.
2. Frames are passed through the **MobileNetV2** model to detect objects.
3. The system calculates the distance of nearby objects using the **Ultrasonic Sensor**.
4. The detected information (e.g., "Person ahead, 2 meters away") is converted into speech using **Google Text-to-Speech (gTTS)**.
5. The generated speech is played through wired earphones.

## Performance Metrics
- **Object Detection Accuracy:** ~72% (MobileNetV2 on COCO dataset)
- **Latency:** ~120ms per frame processing
- **Ultrasonic Sensor Precision:** ±1cm error margin
- **Battery Life:** ~6 hours on 10000mAh power bank

## Future Improvements
- Integration of **Edge TPU Accelerator** for real-time processing.
- Adding **GPS and Navigation Assistance**.
- Implementing **Gesture-based Controls**.

## Contact
dm me on my instagram: https://www.instagram.com/swanand_wirkar.24?igsh=MWQyZHV3NWZpcXJvZA%3D%3D&utm_source=qr

## Acknowledgments
- Supported by **PES Modern College of Engineering** Innovation Cell.
- Developed under the guidance of faculty mentors.

