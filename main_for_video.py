# IMPORT THE NECESSARY LIBRARIES
import os
import cv2
from collections import deque
import matplotlib.pyplot as plt
from os.path import join, basename
from lane_detection import color_frame_pipeline


resize_h, resize_w = 540, 960

test_videos_dir = join('data', 'test_videos')
test_videos = [join(test_videos_dir, name) for name in os.listdir(test_videos_dir)]

for test_video in test_videos:
	print('Processing video: {}'.format(test_video))

	cap = cv2.VideoCapture(test_video)
	out = cv2.VideoWriter(join('out', 'videos', basename(test_video)),
                              fourcc=cv2.VideoWriter_fourcc(*'DIVX'),
                              fps=20.0, frameSize=(resize_w, resize_h))

	# Once a bounded length deque is full, when new items are added, a 
	# corresponding number of items are discarded from the opposite end. 
	# Bounded length deques provide functionality similar to the tail filter in 
	# Unix. They are also useful for tracking transactions and other pools of 
	# data where only the most recent activity is of interest.
	frame_buffer = deque(maxlen=10)
	
	while cap.isOpened():
		ret, color_frame = cap.read()
		if ret:
			color_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB)
			color_frame = cv2.resize(color_frame, (resize_w, resize_h))
			frame_buffer.append(color_frame)
			blend_frame = color_frame_pipeline(frames=frame_buffer, solid_lines=True, temporal_smoothing=True)
			out.write(cv2.cvtColor(blend_frame, cv2.COLOR_RGB2BGR))
			cv2.imshow('blend', cv2.cvtColor(blend_frame, cv2.COLOR_RGB2BGR)), cv2.waitKey(1)
		else:
			break

	cap.release()
	out.release()

	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()
