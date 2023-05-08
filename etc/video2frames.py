import cv2

# Open the video file
cap = cv2.VideoCapture('chihiro.mp4')

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Set the frame number to 0
frame_number = 0

# Loop through the video frames
while cap.isOpened():
    # Read the next frame from the video
    ret, frame = cap.read()

    # If the frame was not read successfully, break out of the loop
    if not ret:
        break

    # Save the frame as an image file
    cv2.imwrite(f'frame_{frame_number}.jpg', frame)

    # Increment the frame number
    frame_number += 1

# Release the video file
cap.release()