from typing import List

def partition(arr, l, r):
    p, curr = l + 1, l + 1
    while curr < r:
        if arr[curr] <= arr[l]:
            arr[p], arr[curr] = arr[p], arr[curr]
            p += 1
        curr += 1
    p -= 1
    arr[p], arr[l] = arr[l], arr[p]
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
