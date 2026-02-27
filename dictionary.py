#creating and acessing
student={"roll_no":74,
         "name":"omyadav",
         "marks":99
         }
print("dictionary:",student)
print("name:",student["name"])
print()

#update
print("2.update dictionary")
student["marks"]=90
student["grade"]="A"
print("updated dictionary:",student)

#remove 
print("3.removing elements")
removed_value=student.pop("grade")
print("removed value:",removed_value)
print("after removing 'grade':",student)

student.popitem()
print("after popitem():",student)
print()

#merging
print("4.merging dictionaries")
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}

merged_dict=dict1 | dict2
print("first dictionary:",dict1)
print("secondary dict:",dict2)
print("merged dictionary:",merged_dict)