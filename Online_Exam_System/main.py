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
    