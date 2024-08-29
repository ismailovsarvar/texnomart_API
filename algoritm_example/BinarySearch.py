def binary_search(list, n):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if list[mid] < n:
            low = mid + 1

        elif list[mid] > n:
            high = mid - 1

        else:
            return mid

    return -1


list = [12, 24, 32, 39, 45, 50, 54]
n = 45

result = binary_search(list, n)

if result != -1:
    print("Element indeksi", str(result))
else:
    print("Element topilmadi")