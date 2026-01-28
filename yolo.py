import cv2
import numpy as np
import argparse
import threading
from playsound import playsound

# ---------------- ARGUMENTS ----------------
parser = argparse.ArgumentParser()
parser.add_argument('--webcam', action='store_true')
parser.add_argument('--video', action='store_true')
parser.add_argument('--image', action='store_true')
parser.add_argument('--video_path', default='videos/fire1.mp4')
parser.add_argument('--image_path', default='fire.jpg')
args = parser.parse_args()

ALARM_SOUND = "alarm.mp3"
alarm_playing = False

# ---------------- ALARM ----------------
def play_alarm():
    global alarm_playing
    if not alarm_playing:
        alarm_playing = True
        playsound(ALARM_SOUND)
        alarm_playing = False

# ---------------- FIRE DETECTION ----------------
def detect_fire(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_fire = np.array([0, 150, 150])
    upper_fire = np.array([35, 255, 255])

    mask = cv2.inRange(hsv, lower_fire, upper_fire)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    fire_pixels = cv2.countNonZero(mask)
    total_pixels = frame.shape[0] * frame.shape[1]

    return fire_pixels / total_pixels > 0.01, mask

# ---------------- DRAW FIRE ----------------
def draw_fire(frame):
    fire, mask = detect_fire(frame)

    if fire:
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, "FIRE", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        threading.Thread(target=play_alarm, daemon=True).start()

    return frame

# ---------------- MODES ----------------
def webcam_mode():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = draw_fire(frame)
        cv2.imshow("Fire Detection - Webcam", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()

def video_mode(path):
    cap = cv2.VideoCapture(path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = draw_fire(frame)
        cv2.imshow("Fire Detection - Video", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()

def image_mode(path):
    img = cv2.imread(path)

    if img is None:
        print("ERROR: Image not found. Check path.")
        return

    img = draw_fire(img)
    cv2.imshow("Fire Detection - Image", img)
    cv2.waitKey(0)

# ---------------- MAIN ----------------
if __name__ == "__main__":
    if args.webcam:
        webcam_mode()
    elif args.video:
        video_mode(args.video_path)
    elif args.image:
        image_mode(args.image_path)

    cv2.destroyAllWindows()
