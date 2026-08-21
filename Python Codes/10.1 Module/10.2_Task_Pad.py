# It's a Self Made Module
# Import the full Task Pad module

import task

tasks = []

task.add(tasks, "Study Python")
task.add(tasks, "Practice DSA")
task.add(tasks, "Complete Assignment")

task.show(tasks)
print( )

task.remove(tasks, "Practice DSA")

task.show(tasks)