# Motion Detection App

This is a simple motion detection app built using OpenCV (cv2) and Pandas in Python. The app uses the webcam to detect motion and records the start and end times of each detected motion event. It displays the grayscale frame, delta frame (difference between consecutive frames), threshold frame (binary form of the delta frame), and color frame with rectangles around detected objects.

## Installation

1. Make sure you have Python installed (version 3.7 or higher).
2. Install the required dependencies by running the following command:
   ```python
   pip install opencv-python pandas

## Usage

1. Run the Python script.
2. The webcam will be accessed, and the motion detection app will start.
3. The app will open separate windows for the grayscale frame, delta frame, threshold frame, and color frame with detected objects.
4. As you move in front of the webcam, the app will detect the motion and draw green rectangles around the moving objects in the color frame.
5. The grayscale, delta, and threshold frames are displayed for reference and understanding.
6. Press the 'q' key to exit the app.
7. After exiting, the app will save the motion start and end times to a CSV file named "Times.csv" in the current directory.

## File Structure

- `main.py`: The main Python script that detects motion using the webcam, displays frames, and saves motion times to a CSV file.

## Dependencies

- `cv2`: The OpenCV library used for accessing the webcam, processing frames, and drawing rectangles around objects.
- `pandas`: The Pandas library used for creating and manipulating the DataFrame to store motion start and end times.

## Output

The app outputs the following:

- Motion detection status list: A list that stores the status of motion detection for each frame.
- Times list: A list that stores the start and end times of each detected motion event.
- Times.csv: A CSV file that contains the motion start and end times in a tabular format.
eadme.md` in your project directory.