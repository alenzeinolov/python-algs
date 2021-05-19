from typing import List


def binary_search(arr: List[int], n: int):
    low = 0
    high = len(arr) // 2
    while (low <= high):
        mid = (high + low) // 2

        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            return mid
    return None

def main():
    print(binary_search([1, 3, 5, 7, 9], 5))

if __name__ == '__main__':
    main()