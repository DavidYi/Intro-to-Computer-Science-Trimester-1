#How to create:
my_dict={"a": "Apple", "b":"Banana"}
#a dictionary 
my_list=["Rabbit", "Dog", "Frog"]
#a list
print(my_dict)
print(my_list)

#How to add things in: 
my_dict["c"] = "Carrot"
#dictionaries
my_list.append("Aardvark")
#lists
print(my_dict)
print(my_list)




#How to delete elements in:
del(my_dict["b"])
#dictionaries
del(my_list[1])
#lists
print(my_dict)
print(my_list)


#How to access the elements in:
my_dict["c"]
my_dict["c", "Not there!"]
    #Theses two are the same, but the bottom one has a default if there is no key called c
#dictionaries
my_list[0]
#lists