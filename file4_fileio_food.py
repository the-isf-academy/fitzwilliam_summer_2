# /////////// INSTRUCTIONS /////////////////
# 💡 File input and output is the processing of
#     reading and writing to a file 
#
# 📄 food.txt is a record of each student's snacks they brough to ELP 
#      each group of numbers is a different student
#       each number represents a different snack 

# 💻 Write code that finds the student carying the most calories
#       print out the student's name and their total calories 

# ////////////////////////////////////////////

file = open("text_files/food.txt", "r") # opens file in read mode

line = file.readline()  # read the first line

while line != "":   # check that we're not at the end of the file

    print(line)
    line = file.readline()  # read the next line



file.close()    # closes file
