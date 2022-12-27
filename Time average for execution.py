import time
# a = time.time()
# print(a)
# b = time.asctime(time.localtime(time.time()))
# print(b)
while (True):
    number = 1
    timelist_for = []
    timelist_while = []
    while number<=1000:
        intial_for = time.time()

        for i in range(0,50):
            print("Akash is learning python")
            print(10 + 10)
            print(10 * 10)
            print(10 - 10)
            print(10 / 10)

        final_for = time.time()
        time_taken_for = final_for - intial_for
        timelist_for.append(time_taken_for)


        intial_while = time.time()
        n = 1
        while n <= 50:
            print("Akash is learning python")
            print(10 + 10)
            print(10 * 10)
            print(10 - 10)
            print(10 / 10)
            n += 1

        final_while = time.time()
        time_taken_while = final_while - intial_while
        timelist_while.append(time_taken_while)
        # print(f"The time taken by for loop is {time_taken_for}")
        # print(f"The time taken by while loop is {time_taken_while}")
        number += 1

    # print(timelist_for)
    totaltime_for = 0.0
    totaltime_while = 0.0
    for x in timelist_for:
        totaltime_for = totaltime_for + x
    for y in timelist_while:
        totaltime_while = totaltime_while + y

    print(f"the sum total of time taken by for loop is {totaltime_for}\n")
    print(f"the sum total of time taken by while loop is {totaltime_while}\n")
    avg_time_for = totaltime_for/number
    avg_time_while = totaltime_while/number
    print(number)
    print("")
    print(f"the average time taken by for loop is {avg_time_for}\n")
    print(f"the average time taken by for loop is {avg_time_while}\n")
    time.sleep(5)
