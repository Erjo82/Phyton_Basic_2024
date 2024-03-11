import time
new_time = 0

now_time = int(time.perf_counter())

print(now_time, new_time)
while True:

    enter2 = input('Press Enter :')
    new_time = int(time.perf_counter()) - int(now_time)
    print(now_time, new_time)



