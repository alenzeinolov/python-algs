from typing import List

def find_smallest(arr: List[int]):
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index

def selection_sort(arr: List[int]):
    result = []
    for i in range(len(arr)):
        i = find_smallest(arr)
        result.append(arr.pop(i))
    return result

def main():
    print(selection_sort([5, 3, 7, 11, 2]))

if __name__ == '__main__':
    main()