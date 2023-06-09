import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

# Increase camera view height to capture entire range of hand movements
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
mouse_x, mouse_y = pyautogui.position()
smooth_factor = 0.5

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            # Get the index finger landmark
            index_x = None
            index_y = None
            for id, landmark in enumerate(landmarks):
                if id == 8:
                    index_x = int(landmark.x * frame_width)
                    index_y = int(landmark.y * frame_height)

            # Move the mouse cursor with the index finger
            if index_x is not None and index_y is not None:
                # Adjust the calculation for moving the cursor outside the camera view
                mouse_x += smooth_factor * ((index_x / frame_width) * screen_width - mouse_x)
                mouse_y += smooth_factor * ((index_y / frame_height) * screen_height - mouse_y)
                pyautogui.moveTo(mouse_x, mouse_y)

            # Check for a left-click gesture (thumb and index finger touching)
            thumb_x = None
            thumb_y = None
            for id, landmark in enumerate(landmarks):
                if id == 4:
                    thumb_x = int(landmark.x * frame_width)
                    thumb_y = int(landmark.y * frame_height)

            if thumb_x is not None and thumb_y is not None:
                thumb_dist = ((thumb_x - index_x)**2 + (thumb_y - index_y)**2)**0.5
                if thumb_dist < 30:
                    pyautogui.click(button='left')

    cv2.imshow('Virtual Mouse', frame)
    key = cv2.waitKey(1)
    if key == 27: # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()

