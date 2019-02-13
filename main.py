def task_1():
    data = {
        'nolan': 'best',
        'leo': 'best',
        'anyone else': 'Everyone is best'
    }
    print(data)


def task_2():
    data = {
        'nolan': 'best',
        'leo': 'best',
        'anyone else': 'Everyone is best'
    }
    try:
        print('Here are all the available indexes \n')
        for row in data:
            print(row)
        del data[input('\nWhat would you like to delete?\n>>>')]
        print(data)
    except IndexError:
        print('That index did not exist.')


def task_3():
    data = {}
    for i in range(0, 3):
        data[i] = input('What would you like to add to the '+str(i)+' index? \n>>>')
    print(data)


def task_4():
    data = {
        'apple': 'oranges',
        'android': 'apple',
        'told': 'sold',
        'bold': 'cold'
    }
    list = []
    for x in data:
        if x[0] == 'a':
            list.append(x)
    for x in list:
        del data[x]
    print(data)


task_1()
task_2()
task_3()
task_4()