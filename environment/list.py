"""
Lists, Tuples, and Dictionaries
"""

myfruit = ["apple", "banana" ,"chery"]
myfruit[2] ="orange"
print(myfruit)
print(myfruit[1])
myfavouritedictionary ={
    "aukaa" :"apple",
    "saanyi" :"banana",
    "paulo" : "pineapple"
}
print(myfavouritedictionary)
mymixedtypelist = [45, 290578, True, "Mydog is on the bed.","49"]
for item in mymixedtypelist:
    print("{} is of the data type{}".format(item,type(item)))