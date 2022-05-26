unsorted_array = [7, 6, 8, 9, 1, 2, 3, 0, -10, 4, 5]


def exchange_sort(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] < n[j]:
                n[i], n[j] = n[j], n[i]

    return n


exchange_sort(unsorted_array)
print(unsorted_array)