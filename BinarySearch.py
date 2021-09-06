import random


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        l = mergeSort(arr[:mid])
        r = mergeSort(arr[mid:])

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    return arr


def binarySearch(sortedArray, key):
    left = 0
    right = len(sortedArray) - 1

    ans = None
    # print(f"Key is {key}")

    while left <= right:

        mid = (right + left) // 2

        if sortedArray[mid] < key:
            left = mid + 1

        elif sortedArray[mid] > key:
            right = mid - 1

        else:
            ans = mid
            break

    # print("################")
    if ans != None:
        # print("Element is present at index", str(ans))
        return ans
    else:
        # print("Element is not present in array")
        return -1


def main():
    start = random.randint(0, 100)
    # data = mergeSort([i for i in range(start, 101, 2)])
    data = [i for i in range(start, 101, 2)]

    print(data)
    while True:
        key = input("Pleas Enter the Number You Want to check : ")

        print(key)

        if key == "c" or key == "C":
            exit()

        if key.isdigit():
            key = int(key)
        else:
            print("Element is not number")
            continue

        result = binarySearch(data, key)
        print("\n")

        if result == -1:
            print("Element is not present in array")
        else:
            print("Element is present at index ", result)
        print("\n\nWant to Try Again !!!\nTo Quit Enter C/c\n")


if __name__ == '__main__':
    main()
