first_num = int(input())
second_num = int(input())
third_num = int(input())

if third_num < first_num > second_num:
    print(first_num)
elif third_num < second_num > first_num:
    print(second_num)
else:
    print(third_num)