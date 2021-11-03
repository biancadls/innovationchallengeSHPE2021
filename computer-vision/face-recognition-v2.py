# This script will detect + track an individual oscilating face via your webcam
# First of its kind frontal classifier + tracking system
# SHPE Innovation Challenge 2021 - Santiago Gomez Paz

import cv2

cap = cv2.VideoCapture(0)

# Create the lbp cascade, better performance than haarcascade_frontalface_default.xml
faceCascade = cv2.CascadeClassifier("lbpcascade_frontalface_improved.xml")

# Get first set of frames
ret, last_frame = cap.read()

# Initialize variables
tracker_cnt = 0
face_x = 0
face_y = 0
face_w = 100
face_h = 100

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
    )

    # Draw a rectangle around the face
    cnt = 0
    if(type(faces) != tuple):
        tracker_cnt = 0
        for (x, y, w, h) in faces:
            if(cnt == 0):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                face_x = int(x)
                face_y = int(y)
                face_w = int(w)
                face_h = int(h)
                cnt = cnt + 1

    elif(type(faces) == tuple):  # If there's no face, the type of faces is tuple
        if(tracker_cnt == 0):
            # Set up tracker.
            # Instead of MIL, you can also use

            tracker_types = ['BOOSTING', 'MIL', 'KCF',
                             'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
            tracker_type = tracker_types[5]

            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker = cv2.TrackerMedianFlow_create()
            if tracker_type == 'CSRT':
                tracker = cv2.TrackerCSRT_create()
            if tracker_type == 'MOSSE':
                tracker = cv2.TrackerMOSSE_create()

            # Define an initial bounding box
            bbox = (face_x, face_y, face_w, face_h)

            # Initialize tracker with first frame and bounding box
            ok = tracker.init(last_frame, bbox)

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        tracker_cnt = tracker_cnt + 1

    # Save last frame
    last_frame = frame

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
