# FYP Python Backend & Raspberry Pi Motion Detection System

This repository contains the **Django backend** and **Raspberry Pi 3 motion detection circuit** code that works together with the [Android app](https://github.com/FYP_Android).

- The **Django backend** serves as the server for handling requests, storing intrusion data, and providing real-time notifications.
- The **Raspberry Pi 3** with a connected motion sensor detects intruders, captures images, and sends a 10-second video clip to the Django backend hosted on it.

## Features

- **Django Backend**:
  - Handles API requests for real-time notifications and streaming.
  - Stores intrusion data including images and video clips.
  
- **Raspberry Pi 3 Motion Detection**:
  - Monitors for motion using a PIR sensor.
  - Captures images and a 10-second video clip when motion is detected.
  - Sends data to the Django backend for further processing.

## Project Structure

### Backend (Django)

- **API Endpoints**: The Django app exposes RESTful API endpoints for the Android app to retrieve notifications, images, and video clips.
- **Database**: Stores intrusion data such as captured images and timestamps.
- **Streaming**: Provides live streaming capabilities for the Android app.
  
#### Key Files:
- `settings.py`: Configuration file for the Django project.
- `urls.py`: URL routing for the Django app.
- `models.py`: Defines the database schema for storing intrusion data.
- `views.py`: API views for handling requests.

### Raspberry Pi Motion Detection

- **motion.py**: Contains the code that handles motion detection using a PIR sensor and camera. When motion is detected, it captures an image and records a 10-second video clip.
- **Communication**: The `motion.py` script communicates with the Django backend by sending the captured data for storage and notification.

#### Key Files:
- `motion.py`: Handles the motion detection, image capturing, and communication with the backend.

## Setup Instructions

### Raspberry Pi Motion Detection

1. **Hardware Requirements**:
   - Raspberry Pi 3
   - PIR Motion Sensor
   - Raspberry Pi Camera Module

2. **Install Required Libraries**:
   Follow steps detailed in this [report]()

### Django Backend

1. **Install Python and Django**: Make sure you have Python installed, and install Django:
   ```bash
   pip install django

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/FYP_Python.git
   cd FYP_Python

3. **Set Up the Django Project**:
   - **Create a Virtual Environment**:
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows use `env\Scripts\activate`
   - **Install Dependencies**: Navigate to the project directory and install the required dependencies from the requirements.txt:
     ```bash
     pip install -r requirements.txt
   - **Configure your settings.py**: Get your Firebase Cloud Messaging Credentials and add it to the settings.pu

## Integration with FYP Android
   - The Android app communicates with the Django backend to receive notifications, display captured images, and play 10-second video clips when motion is detected.
   - Additionally, it streams the live feed from the Raspberry Pi camera when requested.
