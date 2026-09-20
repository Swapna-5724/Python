#   Question = 01

#  Store following word meanings in a python dictionary: 
# table: "a piece of furniture", "list of facts and figures"
#  cat: "a small animal"

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}

print(dictionary)




#    Question  =  02

#  You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#   "python", "java", "C++", "python", "javascript"
#    "java", "python", "java", "C++", "C"

subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}

print(subjects)
print(len(subjects))




#   Question  =  03

#   Write a Program to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary and add one by one. Use Subject name as key and marks as value.

marks = {}

x = input("enter phy : ")
marks.update({"phy" : x})

x = input("enter math : ")
marks.update({"math" : x})

x = input("enter chem : ")
marks.update({"chem" : x})

print(marks)
