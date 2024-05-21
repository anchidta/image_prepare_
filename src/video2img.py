import cv2
import os
def extract_frames(video_path, output_folder):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    # Get the frame rate
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    # Set the interval to skip frames based on the desired frame rate
    interval = int(round(fps / 15))
    # Start frame count
    frame_count = 0

    while True:
        # Read the next frame
        ret, frame = video_capture.read()
        # Check if frame was successfully read
        if not ret:
            break
        # If frame count is divisible by interval, save the frame
        if frame_count % interval == 0:
            # Construct the output file path
            output_path = f"{output_folder}/frame_{frame_count}.jpg"
            # Save the frame as an image
            cv2.imwrite(output_path, frame)
        # Increment frame count
        frame_count += 1

    # Release the video capture object
    video_capture.release()

# Example usage
video_path = "vi/145F.MP4"
directory = "145F_VER15.MP4"

# Create the directory
os.makedirs(directory, exist_ok=True)

print(f"Directory '{directory}' created successfully.")
output_folder = directory
extract_frames(video_path, output_folder)
