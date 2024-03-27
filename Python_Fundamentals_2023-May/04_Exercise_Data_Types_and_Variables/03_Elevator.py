people = int(input())
capacity = int(input())

full_course = people // capacity
half_course = people % capacity
if half_course > 0:
    full_course += 1
print(full_course)