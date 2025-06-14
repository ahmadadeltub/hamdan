from question_store import load_questions, save_questions


def add_question():
    qs = load_questions()
    qid = max([q['id'] for q in qs], default=0) + 1
    text = input('Question text: ')
    num_choices = int(input('Number of choices: '))
    choices = []
    for i in range(num_choices):
        choices.append(input(f'Choice {i + 1}: '))
    answer = int(input('Index of correct choice (starting from 1): ')) - 1
    qs.append({
        'id': qid,
        'question': text,
        'choices': choices,
        'answer': answer,
    })
    save_questions(qs)
    print('Question added.')


def list_questions():
    qs = load_questions()
    for q in qs:
        print(f"{q['id']}: {q['question']}")


def main():
    while True:
        print('\nTeacher Interface')
        print('1. Add question')
        print('2. List questions')
        print('3. Quit')
        choice = input('Select option: ')
        if choice == '1':
            add_question()
        elif choice == '2':
            list_questions()
        elif choice == '3':
            break
        else:
            print('Invalid option')


if __name__ == '__main__':
    main()
