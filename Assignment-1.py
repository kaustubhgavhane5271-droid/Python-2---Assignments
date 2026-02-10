numbers=[10,2,5,8,15]
print("Original List:", numbers)
print("first element:", numbers[0])
print("last element:", numbers[-1])

numbers.append(20)
numbers.insert(2,12)
print("list after adding elements", numbers)

numbers.remove(8)
numbers.pop()
print("list after removing elements:", numbers)

numbers.sort()
print("sorted list:", numbers)

numbers.reverse()
print("reversed list:", numbers)