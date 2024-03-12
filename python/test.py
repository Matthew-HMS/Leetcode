# Using remove()
lst = [1, 2, 3, 4, 5]
lst.remove(3)
lst.remove(4)  # Removes the first occurrence of 3
print(lst)  # Outputs: [1, 2, 4, 5]

# Using pop()
lst = [1, 2, 3, 4, 5]
lst.pop(2)  # Removes the item at index 2
print(lst)  # Outputs: [1, 2, 4, 5]