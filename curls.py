# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import cv2  # imports opencv into the program
import mediapipe  # imports mediapipe into program
import numpy  # for trigonometry


def calculate_angle(a, b, c):
    a = numpy.array(a)  # First
    b = numpy.array(b)  # Mid
    c = numpy.array(c)  # End
    radians = numpy.arctan2(c[1] - b[1], c[0] - b[0]) - numpy.arctan2(a[1] - b[1], a[0] - b[0])
    angle = numpy.abs(radians * 180.0 / numpy.pi)
    if angle>180.0:
        angle = 360 - angle
    return angle






mediapipe_drawing = mediapipe.solutions.drawing_utils  # for drawing utilities
mediapipe_pose = mediapipe.solutions.pose  # import pose estimation model




# VIDEO FEED
cap = cv2.VideoCapture(0)  # setting video capture device (laptop camera), number 0 represents mac cam

#Curl counter
count=0
stage=None


with mediapipe_pose.Pose(min_detection_confidence=0.5,
                         min_tracking_confidence=0.5) as pose:  # Set up mediapipe instance,detetction confidence is 50% and tracking confidence is 50%
    while cap.isOpened():
        ret, frame = cap.read()  # give feed from web came, ret is return variable, frame gives image

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # recoloring the  image from bgr to rgb
        image.flags.writeable = False  # performace tuning

        results = pose.process(image)  # makes detetctions, accesses our pose model

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # rerendering the changed image

        try:  # Extract landmarks
            landmarks = results.pose_landmarks.landmark



            # Used to get coordinates of the shoulder, elbow and wrist
            shoulder = [landmarks[mediapipe_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mediapipe_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mediapipe_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mediapipe_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mediapipe_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mediapipe_pose.PoseLandmark.LEFT_WRIST.value].y]

            # Calculating angles
            angle = calculate_angle(shoulder, elbow, wrist)
            # Curl counting logic
            if angle > 160:
                stage = "down"
            elif angle < 50 and stage == "down":
                stage = "up"
                count += 1
                print(count)
            print(stage)
            print(angle)






        except:
            pass
        #render curl counter
        #setup status box
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)

        #represent data
        cv2.putText(image, 'REPS', (15,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(count), (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        #STAGE DATA
        cv2.putText(image, 'STAGE', (65, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, (60, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        mediapipe_drawing.draw_landmarks(image, results.pose_landmarks, mediapipe_pose.POSE_CONNECTIONS,
                                         mediapipe_drawing.DrawingSpec(color=(245, 117, 66), thickness=2,
                                                                       circle_radius=3),
                                         mediapipe_drawing.DrawingSpec(color=(245, 66, 230), thickness=2,
                                                                       circle_radius=3))  # draws detections to the image

        cv2.imshow('Mediapipe Feed', image)  # visualisation of image via pop up, frame is called mediapipe feed

        if cv2.waitKey(10) & 0xFF == ord('q'):  # I wrote and instead of & (checking if we try to close our screen with q)
            break

    cap.release()  # releases web cam
    cv2.destroyAllWindows()  # closes video feed
