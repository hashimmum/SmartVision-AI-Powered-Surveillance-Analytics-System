import cv2

rtsp_url = "rtsp://zebBNxTy:UHHIwTsnuLXMsEi6@192.168.1.235:554/live/ch0"

cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
else:
    print("Successfully connected to the video stream.")

    while True:
        
        ret, frame = cap.read()

        
        if ret:
            cv2.imshow('RTSP Stream', frame)

            # Press 'q' to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Failed to grab frame")


cap.release()
cv2.destroyAllWindows()
