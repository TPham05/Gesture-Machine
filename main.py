import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


import threading
import speech_recognition as sr

from gestures import detect_gesture
from voice_typing import voice_typing_loop  
from gesture_actions import handle_gesture_action



def main():
    # Setup MediaPipe Hands
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

    # Setup audio interface
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_ctrl = cast(interface, POINTER(IAudioEndpointVolume))

    # Start voice typing thread
    typing_thread = threading.Thread(target=voice_typing_loop, daemon=True)
    typing_thread.start()

    # Start webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        gesture = None
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                gesture = detect_gesture(hand_landmarks)

        # Handle gestures
        if gesture is not None:
            handle_gesture_action(gesture, volume_ctrl)

        # Show webcam frame
        cv2.imshow("Hand Gestures", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
