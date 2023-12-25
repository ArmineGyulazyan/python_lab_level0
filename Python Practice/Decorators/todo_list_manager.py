class EmptyDescriptionId(Exception):
    pass

class InvalidPriority(Exception):
    pass

def task_addition(task_list):
    task={}
    try:
        task_id = input('Enter the task identifier: ')
        task_des = input('Enter the task description: ')
        if not task_des or not task_id or task_id in task_list:
            raise EmptyDescriptionId('\nBoth description and identifier are needed and Id must be unique\n')
        task['descr'] = task_des
        task['status'] = 'incomplete'
        task_list[task_id] = task

    except EmptyDescriptionId as e:
        print(e)

    print(task_list)
    return task_list

def task_remove(task_list):
    inp=input('Enter the identifier to remove the task: ')
    try:
        task_list.pop(inp)

    except KeyError:
        print('Identifier was not found')
    return task_list

def task_listing(task_list):
    if not task_list:
        print("There aren't any tasks")
    else:
        for key,value in task_list.items():
            print(key,'->',value)

def task_completion(task_list):
    inp = input('Enter id to mark as completed: ')
    try:
        task_list[inp]['status'] = 'complete'
    except KeyError:
        print('Identifier was not found')
    else:
        inp2 = input('Do you want to list completed tasks separately? yes/no: ')
        if inp2.lower() == 'yes':
            comp_list = [task_list[t] for t in task_list if task_list[t]['status'] == 'complete']
            incomp_list = [task_list[t] for t in task_list if task_list[t]['status'] == 'incomplete']
            print(incomp_list+comp_list)

    return task_list

def task_priority(task_list):

    inp = input('Enter Id to assign a priority: ')
    print('\nChoose from here:\nhigh\nmedium\nlow\n')
    pri = input('priority?: ')
    try:
        if pri not in ['high','medium','low']:
            raise InvalidPriority('\nChoose from given priorities\n')

        task_list[inp]['priority'] = pri
    except KeyError:
        print('Identifier was not found')
    except InvalidPriority as e:
        print(e)
    else:
        inp2 = input('Do you want to list tasks by priority? yes/no: ')

        if inp2.lower() == 'yes':
            try:
                high_p = [task_list[i] for i in task_list if task_list[i]['priority']=='high']
                medium_p = [task_list[i] for i in task_list if task_list[i]['priority']=='medium']
                low_p = [task_list[i] for i in task_list if task_list[i]['priority']=='low']
                print(high_p+medium_p+low_p)
            except KeyError:
                print('You did not priorities for all tasks')
    return task_list

task_list={}
while True:

    print("\nHello! Here are the options we offer\n")
    print("1.Add a task\n2.Remove a task\n3.List the tasks\n4.Mark as completed\n5.Prioritize\n6.Quit\n")
    inp = input("Select what you want to do: ")

    if inp == '1':
        task_addition(task_list)

    elif inp == '2':
        task_remove(task_list)

    elif inp == '3':
        task_listing(task_list)

    elif inp == '4':
        task_completion(task_list)

    elif inp == '5':
        task_priority(task_list)

    elif inp == '6':
        break
    else:
        print('\nInvalid input, Choose again\n')


