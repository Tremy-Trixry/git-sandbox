def fib():
    first_num = 0
    second_num = 1
    limit = 1000
    rounds = 0

    while rounds < limit:
        third_num = second_num + first_num
        first_num = second_num
        second_num = third_num
        rounds += 1
        print(first_num, second_num)

(fib())