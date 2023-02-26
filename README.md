# Navtrack-Enhancing independance for the visually impaired
## Description
This project is designed to help visually impaired people navigate their surroundings using object detection and monocular distance estimation techniques. The system uses YOLOv5 for object detection and a monocular distance estimation technique to predict the distances of the detected objects in meters. The system also tracks the location of the blind person in real-time and plots it on a map that can be accessed by their family or caretakers.

## System Architecture
We have created our own server architecture system where one of our laptop is the server, we are using our phone to stream live video to laptop 1 and that is supposed to be our module, laptop 1 is transferring data to our server (laptop) and all the computation is done there.

## Requirements
- Python 3.8+
- YOLOv5
- OpenCV
- NumPy
- ZMQ
- Flask-SocketIO
- MapBox
- Flask
- JSON
- Torch
- pyttsx3

## Installation
- Clone the repository: git clone https://github.com/Maaitrayo/Blind-People-Guidance-System
## Features
* Object detection: Our project uses YOLOv5 for object detection, which can identify various objects in the blind person's environment and help them navigate accordingly.

* Distance estimation: We use a monocular distance estimation technique to estimate the distance of the detected objects in meters, which provides more information about the environment to the blind person.

* Real-time location tracking: Our project tracks the location of the blind person in real-time and plots it on a map for their family to see, which can help them keep track of their loved one and ensure their safety.

* Server architecture: We have created your own server architecture system that allows for data to be transferred and computation to be done remotely, which can help improve the efficiency and reliability of your project.

* Mobile streaming: We use our phone to stream live video to your laptop, which serves as the module for your project, making it more portable and accessible.
## Usage
- Helping blind people navigate their environment more safely and independently using object detection, distance estimation, and location tracking.
- Providing real-time information to the blind person's family or caretakers about their location and potential obstacles in their path.
- Improving the quality of life and autonomy of blind individuals

# License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors
- Maaitrayo Das
- Debangshu Kantha
- Shreasi Mukherjee
- Debayan Kumar Ghosh



