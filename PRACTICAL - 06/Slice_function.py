def slice_function(obj, start=None, stop=None, step=None):
    # If step is None, default to 1
    if step is None:
        step = 1
    
    # If start is None, default based on the direction of step
    if start is None:
        start = 0 if step > 0 else len(obj) - 1
    
    # If stop is None, default based on the direction of step
    if stop is None:
        stop = len(obj) if step > 0 else -1

    # Handle negative indices
    if start < 0:
        start += len(obj)
    if stop < 0:
        stop += len(obj)

    # Initialize an empty list for the result
    result = []

    # Iterate through the object manually
    index = start
    if step > 0:
        while index < stop:
            result.append(obj[index])
            index += step
    else:  # For negative step
        while index > stop:
            result.append(obj[index])
            index += step

    return result
print(slice_function([1, 2, 3, 4, 5, 6], 1,-1,3))
print(slice_function([1, 2, 3, 4, 5, 6], 2, 5,1))