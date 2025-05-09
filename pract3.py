def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[min_idx],arr[i] = arr[i], arr[min_idx]

def print_array(arr):
    for val in arr:
        print(val)
    print()

if __name__ == '__main__':
    arr = [24,15,58,789,5]
    print('Original Array : ', end=' ')
    print_array(arr)
    selection_sort(arr)
    print('Sorted Array : ', end=' ')
    print_array(arr)