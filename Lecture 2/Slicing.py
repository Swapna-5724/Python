str = "apna college"
print(str[1:4])

print(str[5:len(str)])

print(str[:4]) #[0:4]

print(str[5:])  #[5:len(str)]



#  Negative Indexing

str = "apple"
print(str[-5:-2])

str = "I am studying python from Apna college"
print(str.endswith("ege"))

print(str.endswith("app"))




#  03
str = "I am studying python from ApnaCollege"
str = print(str.capitalize())
print()
print(str)



str = "i am studying python from ApnaCollege"
print(str.replace("0", "a"))
print(str.replace("python", "javascript"))



#   04
str = "i am studying python from ApnaCollege"
print(str.find("o"))
print(str.find("from"))
print(str.find("Q"))
print(str.count("from"))
