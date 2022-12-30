myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        middle_term = (low + high) // 2
        if target == data[middle_term]:
            return True
        elif target < data[middle_term]:
            high = middle_term - 1
            print("high",high)
        elif target > data[middle_term]:
            low = middle_term + 1
            print("low", low)
    return False

found = binary_search(myList, 4)

print(found)







