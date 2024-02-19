# a function that takes a list and target param
# multiple variables : middle, start, end , steps (the amount of times it splits the dataset into half to find the target)
# while loop solution
# increase the steps each time a split is done
# conditions to track target position

def binary_search(list, target):
    middle = 0
    start = 0
    end = (len(list))
    steps = 0

    while (start <= end):
        print(f"Step {steps} : {list[start:end+1]}")

        steps = steps + 1
        middle = (start + end) // 2

        if target == list[middle]:
            return f"Target found at index {middle}"
        elif target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


my_list = list(range(1, 101))
target = 32

binary_search(my_list, target)
