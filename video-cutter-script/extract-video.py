import cv2

# Video file path
video_path = 'sample_video.mp4'

# Start and end times in seconds
start_time = 10  # Replace with your desired start time
end_time   = 20    # Replace with your desired end time

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get the frames per second (fps) of the video
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Calculate the frame numbers corresponding to start and end times
start_frame = int(start_time * fps)
end_frame = int(end_time * fps)

# Create a VideoWriter object to save the extracted frames
output_file = 'extracted_frames.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_file, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

# Read and save frames within the specified time range
frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if start_frame <= frame_number <= end_frame:
        output_video.write(frame)

    frame_number += 1

    # Stop reading frames after the specified end time
    if frame_number > end_frame:
        break

# Release video objects
cap.release()
output_video.release()
cv2.destroyAllWindows()
