import csv
import uuid
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RESULT_FILE = (BASE_DIR, 'data/results.csv')

def save_result(user_id,exam_id,score,total):

    result_id = 'R' + str(uuid.uuid4())[:5]

    with open(RESULT_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                result_id,
                user_id,
                exam_id,
                score,
                total
            ]
        )

def view_result():

    try:
        with open(RESULT_FILE, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:

                print('\nRESULTS\n')

                print(f'Result ID: {row['result_id']}')
                print(f'Student: {row['user_id']}')
                print(f'Exam ID: {row['exam_id']}')
                print(f'Score: '
                      f'{row['score']}/'
                      f'{row['total']}'
                )
                print('-' * 30)

    except FileNotFoundError:
        print('Results Not Found !')
    