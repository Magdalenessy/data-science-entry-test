def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    
    # initialise out as an empty list
    # going through each value in the list lst
    # if the value in the list is same as find_val then append the replace_val to the out list   
    # if the value in the list is different from find_val then append the actual value to the out list
    out = []
    for i in lst:
      if i == find_val:
        out.append(replace_val)

      else:
        out.append(i)
    return out


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
