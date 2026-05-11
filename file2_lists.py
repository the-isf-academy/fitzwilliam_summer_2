# /////////// INSTRUCTIONS /////////////////
# 💡 Lists are super useful data structure to store 
#     multiple pieces of data 

# 💻 Run the file and make sure you understand
#    how each line maps to the output
# ////////////////////////////////////////////


dessert_list = ["ice cream", "brownies", "mochi", "timtams"]

print(dessert_list)       # print entire list

print(dessert_list[0])    # print specific item  

# 💻 try changing the number above, which numbers are possible? 

print(dessert_list[-1])   # prints the last item

print(len(dessert_list))  # prints the length of the list 


print()

dessert_list.append('cookies')


print("Harry Potter decided to buy:")
for dessert in dessert_list:
  print(dessert)

print()

print('cheese' in dessert_list)

if 'cheese' not in dessert_list:
  print('no cheese :(')
else:
  print('we have cheese!')