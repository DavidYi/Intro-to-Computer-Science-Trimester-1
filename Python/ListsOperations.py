print ("Enter some numbers")

num_list=[]
#Creates empty lists
num = int(input())
while (num!=0):
    num_list.append(num)
#This adds an element to end of list
    num=int(input())
print(num_list)
num_list.reverse()
#This reverses the order of the list as the name implies
print("Reverse:", num_list)
num_list.sort()
#This sorts the list according to smallest to biggest
print("Min:", min(num_list))
#This finds the minimum of the list and can also be put as num_list.min()
print("Max:", max(num_list))
#This finds the maximum of the list and can also be put as num_list.max()
print("Len:", len(num_list))
#This finds the length of the list or number of elements in the list.
print("List[2]:", num_list[2])
#Prints the 2nd element in the list
list_product=1
for num in num_list:
    list_product *=num
print("list_product:", list_product)
