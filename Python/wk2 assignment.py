#creating an emoty list called 'my_list'
my_list = []
#appending the following to my_list: 10, 20, 30, 40.

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#inserting 15 at index 1 (2nd position)
my_list.insert(1,15)
#creating another list
list2 = [50, 60, 70]
#extending my_list with list2
my_list.extend(list2)
#Removing last element from my_list
my_list.pop(7)
# sorting the list in ascending order
my_list.sort()
#finding and printing the index of 30 in my_list
index_of_30 = my_list.index(30)
print("\n The index of the value 30: ", index_of_30)