# Introduction
This project consists of a Python script that extracts frames from a video file and creates a subtitle collage. It uses OpenCV and PIL to handle video and image processing. The script captures frames at specified time points and extracts subtitle regions from those frames. These frames are then combined vertically to create a final image with the subtitle regions labeled with the respective time points.

Project Preview
![preview](./assets/p1.png)

# Installation
To install the necessary dependencies, you can use the following commands:

```
pip install opencv-python-headless
pip install pillow
```
# Usage
1. Setting up the Script

Download the script.py file and open it in your preferred code editor.

2. Modifying Time Points

Before running the script, you are advised to modify the time_points variable in the script to suit your needs. It is currently set to capture frames at every second from the 2nd to the 20th second. Adjust the values and the step in the np.arange function to specify different time points.

```python
time_points = np.arange(2, 20, 1)  # Modify these values as needed
```

3. Running the Script

The script is designed to be run from the command line with the following arguments:

- video_path: Path to the video file
- y_start: Start Y-coordinate of the subtitle region
- y_end: End Y-coordinate of the subtitle region
- output_path: Path to save the output image
Example:

```bash
python script.py video_path y_start y_end output_path
```
Replace video_path, y_start, y_end, and output_path with the actual values for your use case.
