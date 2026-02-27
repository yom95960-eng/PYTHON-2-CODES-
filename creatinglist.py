#creat a list
numbers = [10,5,8,2,15]
#acess list elements
print("original list:",numbers)
print("first element:",numbers[0])
print("last element:",numbers[-1])

#add elements
numbers.append(20)
numbers.insert(2,12)
print("list after adding elements:",numbers)

#remove elements
numbers.remove(8)
numbers.pop()
print("list after removing elements:",numbers)

#sort list elements
numbers.sort()
print("sorted list:",numbers)

#reverse list elements
numbers.reverse()
print("reversed list:",numbers)
