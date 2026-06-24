from auth import login
from exam import create_exams, take_exam
from result import save_result, view_result

def admin_menu():

    while True:

        print("\nADMIN MENU")
        print("1. Create Exam")
        print("2. View Results")
        print("3. Logout")

        choice = input('Enter Your Choice: ')

        if choice == '1':
            create_exams()

        elif choice == '2':
            view_result()

        elif choice == '3':
            break

        else:
            print('Invalid Choice !')

def student_menu(user):

    while True:

        print("\nSTUDENT MENU")
        print("1. Attend Exam")
        print("2. Logout")

        choice = input('Enter Your Choice: ')

        if choice == '1':

            exam_id, score, total = (take_exam(user['user_id']))

            if exam_id:

                save_result(
                    user['user_id'],
                    exam_id,
                    score,
                    total
                )

                print('\nExam Completed')

                print(f'Score: {score}/{total}')

        elif choice == '2':
            break

        else:
            print('Invalid Choice !')

def main():

    while True:

        print('\nONLINE EXAMINATION')

        user = login()

        if not user:
            print('Invalid Login !')
            continue

        if user['role'] == 'admin':
            admin_menu()

        elif user['role'] == 'student':
            student_menu(user)

        else:
            print('Invalid Choice !')

if __name__ == '__main__':
    main()
