student={}

def calculate_grade(avg):
    if avg>=90:
        return 'A+'
    elif avg>=80:
        return 'B+'
    elif avg>=70:
        return 'C+'
    elif avg>=60:
        return 'D'
    else:
        return 'FAIL'

while True:
    print('1. Add Student')
    print('2. Search student')
    print('3. View all students')
    print('4. remove student')
    print('5. clear data')
    print('6. show topper')
    print('7. exit')

    choice=input('Enter your choice: ')

    if choice=='1':
        name=input('Enter student name to add: ')
        num=int(input('Enter no.of subjects: '))
        mark=[]

        for i in range(num):
            m=int(input('enter mark {}: '.format(i+1)))
            mark.append(m)

        student[name]=mark
        print('student added succesfully')

    elif choice=='2':
        name=input('Enter student name to search: ')

        if name in student:
            avg=sum(mark)/len(mark)
            grade=calculate_grade(avg)

            print('name: ',name)
            print('mark: ',mark)
            print('average: ',avg)
            print('grade: ',grade)

    elif choice=='3':
        if not student:
            print('no students found')
        else:
            for name,mark in student.items():
                avg = sum(mark) / len(mark)
                grade = calculate_grade(avg)

                print('name: ', name)
                print('mark: ', mark)
                print('average: ', avg)
                print('grade: ', grade)

    elif choice=='4':
        name=input('Enter student name to remove: ')
        if name in student:
            del student[name]
            print('student removed succesfully')
        else:
            print('no students found')

    elif choice=='5':
        confirm=input('Are you sure? (yes or no)')
        if confirm.lower()=='yes':
            student.clear()
            print('all data cleared')

    elif choice=='6':
        if not student:
            print('no students found')
        else:
            topper=None
            highest_avg=0

            for name,mark in student.items():
                avg=sum(mark)/len(mark)

                if avg>highest_avg:
                    highest_avg=avg
                    topper=name
                    grade=calculate_grade(avg)

            print('topper: ',topper)
            print('average: ',round(highest_avg))
            print('grade: ',grade)

    elif choice=='7':
        print('exiting program...')
        break
    else:
        print('invalid choice')