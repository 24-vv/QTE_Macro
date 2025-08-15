# QTE Macro for Huzz RNG

![Python](https://img.shields.io/badge/python-3.10%2B-blue)

A fast and accurate macro for automating the QTE (Quick Time Event) sequence in Huzz RNG. Uses multi-threaded screen capture and predictive clicking for high-speed precision.

---

## Features

- Real-time screen capture for high responsiveness
- Predictive bar clicking to reduce misses
- Modular design for easy maintenance and future development
- Live detection visualization (optional)
- Lightweight and efficient

---

## Installation

1. Ensure you have **Python 3.10+** installed.
2. Clone or download the repository:

```bash
git clone https://github.com/yourusername/QTE-Macro.git

cd QTE-Macro

pip install -r requirements.txt
```
 ## Dependencies include:

 - `pyautogui`
 - `opencv-python`
 - `numpy`
 - `mss`
 - `pygetwindow`

 ## Usage

 1. Naviagte to the quick time event.

 2. Go through all the necassary dialogue, once there press "Play Hard".

 3. Run the macro.
    ```bash
    python main.py
    ```

5. If everything is done correctly then it should start automating the QTE instantly.

## Configuration

- The screen capture region is set in main.py with qte_region. Adjust the coordinates if your resolution or UI layout differs.
- Color thresholds for the bar and target are in `main.py` as `bar_lower`, `bar_upper`, `target_lower`, and `target_upper`. Adjust if needed.

## Notes

- The macro only handles the QTE itself; it does not automate any menu buttons like “Play Hard.” (yet)
- Multi-threaded capture ensures high frame rates for fast-moving bars.
