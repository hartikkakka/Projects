from datetime import datetime

import cv2
import pandas

# making the variable with None, the variable will capture the first frame
first_frame = None

status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

# VideoCapture that allows you to access and manipulate video files or capture video from a connected camera
# "0" indicates the default camera (usually the webcam)
video = cv2.VideoCapture(0)

while True:
    # check variable is a boolean that indicates the success of reading a frame from the video source
    # If check is True, a frame was successfully read. If False, there are no more frames to read.
    # frame variable stores a single frame read from the video source
    check, frame = video.read()

    status = 0

    # Convert the frame to grayscale for processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # GaussianBlur is used to blur the image , so its remove noise and increase accuracy in the calculation
    # first para is the image you want to blur
    # GaussianBlur Kernel size determines the extent of blurring. It should be a positive odd integer.
    # standard deviation values like 1 or 2 are commonly used for mild blurring or noise reduction,
    # while larger values like 5 or 10 are used for more pronounced blurring effects.
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Script will run the loop first and capture the first frame according to condition
    if first_frame is None:
        first_frame = gray
        continue

    # # Calculates the absolute difference between two images or arrays.
    delta_frame = cv2.absdiff(first_frame, gray)

    # Thresholding converts an image to a binary form by separating pixels into foreground and
    # background based on a specified threshold value.
    # cv2.threshold(image, threshold_value, max_value, threshold_type) - Apply image thresholding.
    # no 30 correspondence to black and 255 to white
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # cv2.dilate expands or thickens the boundaries of foreground objects in a binary image.
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Parameters: (image, mode, method)
    # - image: The input image on which contours will be detected
    # - mode: Contour retrieval mode
    #     - cv2.RETR_EXTERNAL: Retrieve only the external contours
    # - method: Contour approximation method
    #     - cv2.CHAIN_APPROX_SIMPLE: Compresses contours to their endpoints
    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over each contour found
    for contour in cnts:
        # Filter out small contours based on their area
        if cv2.contourArea(contour) < 10000:
            continue

        status = 1

        # Calculate the bounding rectangle for the contour
        (x, y, w, h) = cv2.boundingRect(contour)

        # Draw a green rectangle around the contour on the original frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    status_list.append(status)

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    # Display the grayscale frame in a window titled "gray frame"
    cv2.imshow("gray frame", gray)
    # Display the grayscale frame in a window titled "gray frame"
    cv2.imshow("delta frame", delta_frame)
    # Display the black and white frame in a window titled "thresh frame"
    cv2.imshow("thresh frame", thresh_frame)
    # Display the color frame with rectangle detecting the object in a window titled "color frame"
    cv2.imshow("color Frame", frame)

    # Wait for a keyboard event for 1 millisecond
    # If any key is pressed, it returns the Unicode value of the key, otherwise it returns -1
    key = cv2.waitKey(1)

    # # Print the grayscale frame
    # print(gray)
    # # Print the delta frame
    # print(delta_frame)

    # If the pressed key is 'q' (Unicode value 113), exit the loop
    if key == ord("q"):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = pandas.concat([df, pandas.DataFrame({"Start": [times[i]], "End": [times[i+1]]})], ignore_index=True)

    
df.to_csv("Times.csv", index=False)

# Release the video capture object
video.release()

# Close all open windows
cv2.destroyAllWindows()
