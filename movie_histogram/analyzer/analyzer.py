import cv2
import numpy as np


class Analyzer:
    def __init__(self, video_file, sampling=24, num_bin=16):
        self.video_file = video_file
        self.sampling = sampling
        self.vid_cap = cv2.VideoCapture(self.video_file)
        self.total_frames = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.num_bin = num_bin

    def get_histogram(self):
        success, frame = self.vid_cap.read()
        num_pixels = np.prod(frame.shape[:2])
        frame_t = 0

        while success:
            if frame_t % self.sampling == 0:
                (b, g, r) = cv2.split(frame)
                histogram_r = cv2.calcHist([r], [0], None, [self.num_bin], [0, 255]) / num_pixels
                histogram_g = cv2.calcHist([g], [0], None, [self.num_bin], [0, 255]) / num_pixels
                histogram_b = cv2.calcHist([b], [0], None, [self.num_bin], [0, 255]) / num_pixels
                yield (histogram_r, histogram_g, histogram_b)

            frame_t += 1
            success, frame = self.vid_cap.read()
