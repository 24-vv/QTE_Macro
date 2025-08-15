import cv2
import time
import pygetwindow as gw
from core.capture import Capture
from core.detection import Detection
from core.clicker import Clicker

roblox_windows = [w for w in gw.getWindowsWithTitle("Roblox") if w.visible]
if not roblox_windows:
    exit()
roblox_window = roblox_windows[0]
roblox_window.activate()
time.sleep(2)

qte_region = {"top": 724, "left": 505, "width": 842, "height": 50}
bar_lower = [200, 200, 200]
bar_upper = [255, 255, 255]
target_lower = [0, 200, 0]
target_upper = [50, 255, 50]

capture = Capture(qte_region)
detection = Detection(bar_lower, bar_upper, target_lower, target_upper)
clicker = Clicker()

while True:
    frame = capture.get_frame()
    if frame is None:
        continue

    bar_info, target_info = detection.process_frame(frame)

    if bar_info and target_info:
        predicted_x = detection.predict_bar_position()
        bx, by, bw, bh, _, _ = bar_info
        tx, ty, tw, th, tcx, tcy = target_info

        if (predicted_x + bw > tx) and (predicted_x < tx + tw) and (by + bh > ty) and (by < ty + th):
            clicker.safe_click(qte_region["left"] + tcx, qte_region["top"] + tcy)

    cv2.imshow("Live Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
