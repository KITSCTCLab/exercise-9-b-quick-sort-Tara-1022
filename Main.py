from typing import List

def partition(arr, l, r):
    p, i = l, l
    while i < r:
        if arr[i] <= arr[p]:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
        i += 1
    return p

def quick_sort(data, l, r) -> List[int]:
    p = partition(data, l, r)
    quick_sort(data, l, p)
    quick_sort(data, p, r)
    return data

input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))
