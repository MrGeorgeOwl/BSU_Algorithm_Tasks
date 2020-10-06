import sys
from typing import List
from random import randint


def binary_search(number: int, array: List[int]) -> int:
    if not array:
        raise Exception("Array is empty")

    amount_compares = 0 
    left_border = 0
    right_border = len(array) - 1

    while left_border <= right_border:
        amount_compares += 1
        m = int((right_border + left_border) / 2)
        if array[m] < number:
            left_border = m + 1
            amount_compares += 1
        elif array[m] > number:
            right_border = m - 1
            amount_compares += 1
        else:
            print(f"Amount of compares: {amount_compares}")
            return m

    print(f"Amount of compares: {amount_compares}")
    return -1    


def interpolation_search(number: int, array: List[int]) -> int:
    if not array:
        raise Exception("Array is empty")
    
    amount_compares = 0
    left_border = 0
    right_border = len(array) - 1

    while array[left_border] < number < array[right_border]:
        mid = int(left_border + (number - array[left_border]) 
                  * (right_border - left_border) 
                  / (array[right_border] - array[left_border]))
        amount_compares += 2
        if array[mid] < number:
            left_border = mid + 1
            amount_compares += 1
        elif array[mid] > number:
            right_border = mid - 1
            amount_compares += 1
        else:
            print(f"Amount of compares: {amount_compares}")
            return mid
   
    if array[left_border] == number:
        amount_compares += 1
        print(f"Amount of compares: {amount_compares}")
        return left_border
    elif array[right_border] == number:
        amount_compares += 1
        print(f"Amount of compares: {amount_compares}")
        return right_border
    else:
        print(f"Amount of compares: {amount_compares}")
        return -1

def generate_array(len_array: int, range_elements: int) -> List[int]:
    return [randint(0, len_array) for _ in range(range_elements)]


if __name__ == "__main__":
    args = list(map(lambda x: int(x), sys.argv[1:]))
    number, len_array, range_elements = args 
    array = sorted(generate_array(len_array, range_elements))
    print(array)
    print("Binary search")
    binary_search(number, array)
    print("Interpolation search")
    interpolation_search(number, array) 
