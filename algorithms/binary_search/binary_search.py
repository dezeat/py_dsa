def binary_search(arr: list[int], target: int, left_ptr: int, right_ptr: int) -> int:
    """ 
    If the target is present in arr returns the index of target in arr.
    Else returns -1. Assumes a sorted arr with unique values.
    """

    if not arr or target is None:
        msg = "Both paramts 'arr' and 'target' need to be not none."
        raise ValueError(msg)
    
    if left_ptr > right_ptr:
        return -1
    
    middle = (left_ptr +  right_ptr) // 2

    if arr[middle] == target:
        return middle
    
    else:
        if arr[middle] > target:
            return binary_search(arr, target, left_ptr, middle-1)
        
        return binary_search(arr, target, middle+1, right_ptr)
