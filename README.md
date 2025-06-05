# EduBox AR

EduBox AR is a simple prototype of an interactive learning device that works offline. Teachers can add questions using the `teacher_interface.py` script, run the webcam driven quiz with `edubox_ar.py`, or use the new graphical interface in `edubox_gui.py`.

## Requirements

- Python 3
- OpenCV (`pip install opencv-python`)

## Usage

1. **Add Questions**

   ```bash
   python teacher_interface.py
   ```
   Follow the prompts to add new multiple-choice questions. Questions are saved in `questions.json`.

2. **Run Interactive Session**

   ```bash
   python edubox_ar.py
   ```
   The script will open the webcam (camera index `0` by default), display each question and detect simple pointing gestures. Move your hand in front of the camera and hold your choice area to select an answer. Use `--camera N` to select a different camera on your system.

3. **Use the GUI (Recommended for Mac)**

   ```bash
   python edubox_gui.py
   ```
   This launches a small application with a Teacher page to add questions and a Student page to start the quiz using your laptop camera.

The GUI should run on macOS without additional setup beyond installing Python and OpenCV.

At the end of the session, selected answers are printed to the terminal.
