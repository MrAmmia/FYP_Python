import sqlite3
import RPi.GPIO as GPIO
import time
import datetime
from picamera import PiCamera
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

pir_pin = 12
led_pin = 11

db_path = "/home/mrammia/FYP/db.sqlite3"
conn = sqlite3.connect(db_path)
c = conn.cursor()


def send_push_notification():
    cred = credentials.Certificate('final-year-project-50477-firebase-adminsdk-z23ka-75c58ad43a.json')

    # Initialize the Firebase app with the service account
    firebase_admin.initialize_app(cred)

    token = "eZMEGuFnQEqViXeJcu5rSd:APA91bHjPMMZjRGcPpgfIePSur5b9hTPQu73LhVhJzRRAiGtYFX4F81s4X5uT6dVkR1fFnIlGehWX402WQOes61JDCFpUbtcRBpGkIKNsudVESiPUut16F6bWci5jO4hzRI1ZdLI2H1u"

    # Create a message with the body and title
    message = messaging.Message(
        notification=messaging.Notification(
            title='Intruder',
            body='Intruder Alert Motion was detected'
        ),
        token=token
    )

    # Send the message
    response = messaging.send(message)

    # Print the message ID on success
    print('Successfully sent message:', response)


count = 1


def take_photo():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    # camera.video_format = 'mp4'
    image_storage_path = "/home/mrammia/FYP/motion_detection/motion_images/"
    video_storage_path = "/home/mrammia/FYP/motion_detection/motion_videos/"

    # Wait for camera to warm up
    time.sleep(2)
    send_push_notification()

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Capture image
    image_name = 'motion' + str(timestamp) + '.jpg'
    image_path = image_storage_path + image_name
    camera.capture(image_path)

    # Record video for 10 seconds
    video_name = 'motion' + str(timestamp) + '.mjpeg'
    new_video_name = 'motion' + str(timestamp) + '.mp4'
    video_path = video_storage_path + video_name
    camera.start_recording(video_path)
    time.sleep(10)
    camera.stop_recording()

    c.execute("INSERT INTO home_MotionEvent (timestamp,image,video) VALUES(?,?,?)",
              (timestamp, 'motion_images/' + image_name, 'motion_videos/' + video_name))
    conn.commit()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        if GPIO.input(pir_pin):
            print("Motion Detected")
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(1)
            if count == 1:
                take_photo()
            count += 1
        else:
            GPIO.output(led_pin, GPIO.LOW)
            print("Motion Stopped")
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    conn.close()


