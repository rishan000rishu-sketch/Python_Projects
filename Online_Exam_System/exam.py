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
