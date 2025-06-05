# EduBox AR

EduBox AR is a simple prototype of an interactive learning device that works offline. Teachers can add questions using the `teacher_interface.py` script and run the interactive session with `edubox_ar.py`.

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
   The script will open the webcam, display each question and detect simple pointing gestures. Move your hand in front of the camera and hold your choice area to select an answer.

At the end of the session, selected answers are printed to the terminal.
