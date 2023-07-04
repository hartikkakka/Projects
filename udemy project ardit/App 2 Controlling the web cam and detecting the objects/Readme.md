# Motion Detection with OpenCV

This project utilizes OpenCV, a popular computer vision library, to perform motion detection using a webcam or video file. It captures the frames from the video source, applies image processing techniques, and identifies moving objects by comparing consecutive frames.

## Requirements

- Python (version 3 or higher)
- OpenCV library (`pip install opencv-python`)
- pandas library (`pip install pandas`)

## Usage

1. Ensure your webcam is connected or provide a video file to be processed.

2. Run the Python script:


3. The script will open windows showing the grayscale frame, delta frame (difference between consecutive frames), thresholded frame (black and white image highlighting moving objects), and color frame with rectangles around detected objects.

4. Press 'q' on your keyboard to exit the script.

5. After exiting, a file named `Times.csv` will be generated, containing the timestamps of when motion was detected.

