task=[]

while True:
    print('1. Add Task')
    print('2. View Task')
    print('3. Mark Status')
    print('4. Remove Task')
    print('5. Exit')

    choice=input('Enter your option: ')

    if choice=='1':
        name=input('Enter Your task: ')

        if name.strip()== "":
            print('Task cannot be Empty!!!')
        else:
            task.append({
                'name': name,
                'Completed': False
            })
            print('Task Added Successfully')

    elif choice=='2':
        if len(task)==0:
            print('No Tasks Found!!!')
        else:
            print('\n-----Your Tasks-----')

            for i in range(len(task)):

                status='Completed' if task[i]['Completed'] else 'Pending'
                print(f'{i+1}. {task[i]} -{status}')

    elif choice=='3':
        if len(task)==0:
            print('No task Available!!!')
        else:
            for i in range(len(task)):
                status='Completed' if task[i]['Completed'] else 'Pending'
                print(f'{i+1}.{task[i]}- {status}')

            try:
                index=int(input('Enter Task number to mark Completed: ')) -1

                if 0 <=index <len(task):
                    task[index]['Completed']=True
                    print('Marked successfully!!')
                else:
                    print('Invalid task number!!')
            except ValueError:
                print('please enter a valid number')

    elif choice=='4':
        if len(task)==0:
            print('Task not Found!!!')
        else:
            for i in range(len(task)):
                status='Completed' if task[i]['Completed'] else 'Pending'
                print(f'{i+1}. {task[i]} -{status}')

            try:
                index=int(input('Enter Task No: '))-1

                if 0<=index<len(task):
                    task.pop(index)
                    print('Task Removed!!!')
                else:
                    print('Invalid Task Number')
            except ValueError:
                print('Please Enter valid number')

    elif choice=='5':
        print('Exiting program!!!')
        break
    try:
        print('Invalid Choice')
    except ValueError:
        print('Please Enter Valid choice!!!')
