# /////////// INSTRUCTIONS /////////////////
# 💡 File input and output is the processing of
#     reading and writing to a file 
#
# 📄 poem_part1.txt and poem_part2.txt is one complete poem, that has
#    been broken into parts. The lines from the two incomplete files s
#    should be interleaved into the output file 
#    (e.g., first line from poem_part1, first line from poem_part2, second line from poem_part1, etc.) 

# 💻 Write code that merges the text from both files
#    and outputs the whole poem to a new file wholepoem.txt

# ////////////////////////////////////////////


file_wholepoem = open("text_files/wholepoem.txt", "w")   # creates new file in write mode 



file_wholepoem.close()
