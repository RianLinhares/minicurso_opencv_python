import cv2
# Load the Haar Cascade
face_cascade = 'haarcascade_eye.xml'

# Create the Haar Cascade
faceCascade = cv2.CascadeClassifier(face_cascade)

# Read the Video
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert to Gray-Scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = face_cascade .detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the resulting Frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
