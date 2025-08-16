arr = [4, 2, 1, 3, 5]

def lowest(arr):
    # ===============
    lowest_num=arr[0]
    for i in arr:
        if i<= lowest_num:
            lowest_num=i
    # ===============
    return lowest_num

print(lowest(arr))

def hv(arr):
    hvn=arr[0]
    for i in arr:
        if i>= hvn:
            hvn=i
    return hvn

print(hv(arr))

def arrsum(arr):
    a=len(arr)
    for i in range arr:
        

print(arrsum(arr))

