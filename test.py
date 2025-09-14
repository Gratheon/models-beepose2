import deeplabcut
import os
from deeplabcut.utils import auxiliaryfunctions

print("--- Starting test.py ---")

# Define the project config path
config_path = os.path.abspath('./GratheonBeePose-tot_ra-2025-09-13/config.yaml')

# Define the video to analyze
video_path = os.path.abspath('test2.mp4')

# deeplabcut.analyze_videos(config_path, [video_path], save_as_csv=True)

# # Convert detections to tracklets
# deeplabcut.convert_detections2tracklets(config_path, [video_path], videotype='mp4')

# # Stitch tracklets
# deeplabcut.stitch_tracklets(config_path, [video_path], videotype='mp4')

# Create labeled video
deeplabcut.create_labeled_video(config_path, [video_path], draw_skeleton=False)
