import tkinter as tk
from tkinter import ttk, messagebox

from teacher_interface import load_questions, save_questions
from edubox_ar import run_quiz


def refresh_question_list(box):
    box.delete(0, tk.END)
    for q in load_questions():
        box.insert(tk.END, f"{q['id']}: {q['question']}")


def add_question(question_entry, choice_entries, answer_var, box):
    text = question_entry.get().strip()
    choices = [e.get().strip() for e in choice_entries]
    if not text or any(not c for c in choices):
        messagebox.showerror('Error', 'Please fill in all fields')
        return
    try:
        answer_idx = int(answer_var.get())
    except ValueError:
        messagebox.showerror('Error', 'Select correct answer')
        return
    qs = load_questions()
    qid = max([q['id'] for q in qs], default=0) + 1
    qs.append({'id': qid, 'question': text, 'choices': choices, 'answer': answer_idx})
    save_questions(qs)
    refresh_question_list(box)
    messagebox.showinfo('Added', 'Question added')
    question_entry.delete(0, tk.END)
    for e in choice_entries:
        e.delete(0, tk.END)


def build_teacher_page(root):
    frame = ttk.Frame(root, padding=10)
    ttk.Label(frame, text='Add Question', font=('Helvetica', 16)).pack(pady=5)
    question_entry = ttk.Entry(frame, width=40)
    question_entry.pack(fill='x', pady=2)
    choice_entries = []
    for i in range(4):
        ce = ttk.Entry(frame, width=30)
        ce.pack(fill='x', pady=2)
        choice_entries.append(ce)
    answer_var = tk.StringVar()
    ttk.Label(frame, text='Correct answer (1-4):').pack(pady=2)
    answer_box = ttk.Combobox(frame, textvariable=answer_var, values=['0','1','2','3'], width=5)
    answer_box.pack(pady=2)
    listbox = tk.Listbox(frame, height=6)
    listbox.pack(fill='both', expand=True, pady=5)
    refresh_question_list(listbox)
    ttk.Button(frame, text='Add', command=lambda: add_question(question_entry, choice_entries, answer_var, listbox)).pack(pady=5)
    return frame


def build_student_page(root):
    frame = ttk.Frame(root, padding=10)
    ttk.Label(frame, text='EduBox AR Quiz', font=('Helvetica', 16)).pack(pady=10)
    ttk.Button(frame, text='Start Quiz', command=run_quiz).pack(pady=10)
    return frame


def main():
    root = tk.Tk()
    root.title('EduBox AR')
    style = ttk.Style(root)
    style.theme_use('clam')

    nb = ttk.Notebook(root)
    teacher_frame = build_teacher_page(nb)
    student_frame = build_student_page(nb)
    nb.add(student_frame, text='Student')
    nb.add(teacher_frame, text='Teacher')
    nb.pack(fill='both', expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
