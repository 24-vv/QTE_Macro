import cv2
import numpy as np
from collections import deque
import time

class Detection:
    def __init__(self, bar_lower, bar_upper, target_lower, target_upper):
        self.bar_lower = np.array(bar_lower)
        self.bar_upper = np.array(bar_upper)
        self.target_lower = np.array(target_lower)
        self.target_upper = np.array(target_upper)
        self.bar_history = deque(maxlen=5)

    def process_frame(self, frame):
        bar_mask = cv2.inRange(frame, self.bar_lower, self.bar_upper)
        target_mask = cv2.inRange(frame, self.target_lower, self.target_upper)

        bar_contours, _ = cv2.findContours(bar_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        target_contours, _ = cv2.findContours(target_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        bar_info = None
        target_info = None

        if bar_contours:
            bar = max(bar_contours, key=cv2.contourArea)
            bx, by, bw, bh = cv2.boundingRect(bar)
            bar_center_x = bx + bw // 2
            bar_center_y = by + bh // 2
            self.bar_history.append((bar_center_x, time.time()))
            bar_info = (bx, by, bw, bh, bar_center_x, bar_center_y)

        if target_contours:
            target = max(target_contours, key=cv2.contourArea)
            tx, ty, tw, th = cv2.boundingRect(target)
            target_center_x = tx + tw // 2
            target_center_y = ty + th // 2
            target_info = (tx, ty, tw, th, target_center_x, target_center_y)

        return bar_info, target_info

    def predict_bar_position(self):
        if len(self.bar_history) >= 2:
            x1, t1 = self.bar_history[-2]
            x2, t2 = self.bar_history[-1]
            speed = (x2 - x1) / max(t2 - t1, 0.0001)
            predicted_x = x2 + speed * 0.015
            return predicted_x
        return None
