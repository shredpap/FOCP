import cv2

# Start webcam
cap = cv2.VideoCapture(0)

# Create the haar cascade
eye_cascade = cv2.CascadeClassifier(r"C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\Personalprojects\Eyetracker\haarcasscade_eye.xml")


while True:
    # Read the webcam frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the frame
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the eyes
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Eye Tracker", frame)

    # Check if the user pressed 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
