from typing import List

def partition(arr, l, r):
    #Function implementing partitioning of sub-array arr[l:r]
    #Return: -> index of pivot
    p, curr = l, l + 1
    while curr <= r:
        if arr[curr] <= arr[l]:
            p += 1
            arr[p], arr[curr] = arr[curr], arr[p]
        curr += 1
    arr[p], arr[l] = arr[l], arr[p]
    return p

def quick_sort(data, l, r) -> List[int]:
     #Function implementing in-place quick sort of data[l:r]
    if l < r:
        p = partition(data, l, r)
        quick_sort(data, l, p - 1)
        quick_sort(data, p + 1, r)
    return data

input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))
