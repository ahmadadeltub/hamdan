import cv2
import json
import os

QUESTIONS_FILE = 'questions.json'


def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        return []
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def draw_question(frame, q):
    y = 30
    cv2.putText(frame, q['question'], (10, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    for idx, choice in enumerate(q['choices']):
        y += 40
        text = f"{idx + 1}. {choice}"
        cv2.putText(frame, text, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)


def detect_motion(bg_gray, frame_gray):
    diff = cv2.absdiff(bg_gray, frame_gray)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    largest = max(contours, key=cv2.contourArea)
    if cv2.contourArea(largest) < 500:
        return None
    M = cv2.moments(largest)
    if M['m00'] == 0:
        return None
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    return (cx, cy)


def main():
    questions = load_questions()
    if not questions:
        print('No questions available. Use teacher_interface.py to add.')
        return

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('Camera not available')
        return

    ret, frame = cap.read()
    if not ret:
        print('Failed to read from camera')
        return
    bg_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    current = 0
    selections = {}
    hold_counter = 0
    current_choice = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        motion = detect_motion(bg_gray, gray)
        h, w = frame.shape[:2]

        if motion:
            cx, cy = motion
            cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)
            region_width = w // len(questions[current]['choices'])
            choice = cx // region_width
            if choice != current_choice:
                current_choice = choice
                hold_counter = 0
            else:
                hold_counter += 1
            if hold_counter > 15:
                selections[current] = choice
                current += 1
                hold_counter = 0
                current_choice = None
                if current >= len(questions):
                    break
                cv2.putText(frame, 'Answer recorded', (10, h-30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        draw_question(frame, questions[current])
        cv2.imshow('EduBox AR', frame)
        if cv2.waitKey(30) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    # show summary
    for idx, q in enumerate(questions):
        sel = selections.get(idx)
        if sel is None:
            ans_text = 'No response'
        else:
            ans_text = q['choices'][sel]
        print(f"Q{idx+1}: {ans_text}")


if __name__ == '__main__':
    main()
