def binary_search(arr,search_ele,low,high):
    while high >= low:
        mid_pos = (low + high)//2
        if arr[mid_pos] == search_ele:
            return mid_pos
        elif arr[mid_pos] > search_ele:
            high = mid_pos - 1
        else:
            low = mid_pos + 1
        
arr = [3,4,5,6,7,8,9]
low = 0
high = len(arr) - 1
search_ele = 11
obj = binary_search(arr,search_ele,low,high)
print(obj)

        