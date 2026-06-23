import csv
import uuid
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXAMS_FILE = os.path.join(BASE_DIR, 'data/exams.csv')
QUESTION_FILE = os.path.join(BASE_DIR, 'data/questions.csv')

def create_exams():

    exam_id = 'E' + str(uuid.uuid4())[:4]

    exam_name = input('Enter Exam Name: ')

    with open(EXAMS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            exam_id,
            exam_name
        ])

    print('Exam Created Successfully.')
    
    add_questions(exam_id)

def add_questions(exam_id):

    count = int(input('Enter No Of Questions: '))

    with open(QUESTION_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        for i in range(count):

            print(f'\nQuestion {i+1}')

            question_id = 'Q' + str(uuid.uuid4())[:5]

            question = input("Question: ")

            option1 = input("Option 1: ")
            option2 = input("Option 2: ")
            option3 = input("Option 3: ")
            option4 = input("Option 4: ")

            answer = input(
                "Correct Answer (exact option text): "
            )

            writer.writerow([
                question_id,
                exam_id,
                question,
                option1,
                option2,
                option3,
                option4,
                answer
            ])

    print('\nQuestion Added Successfully')

def view_exams():

    try:
        with open(EXAMS_FILE, 'r') as file:
            reader = csv.DictReader(file)

            print('\n-----AVAILABLE EXAMS-----')

            for row in reader:

                print(
                    row['exam_id'],
                    '-',
                    row['exam_name']
                )

    except FileNotFoundError:
        print('No Exams Found !')
