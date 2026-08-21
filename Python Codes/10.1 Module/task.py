def add(tasks, task):
    tasks.append(task)


def remove(tasks, task):
    if task in tasks:
        tasks.remove(task)


def show(tasks):
    print("My Tasks:")

    for task in tasks:
        print("-", task)