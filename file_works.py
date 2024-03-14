# opening a file and reading its contents
file_loc_1 = "C:/Users/TJO1COB/source.txt"
with open(file=file_loc_1,mode='r') as open_file:
    pr_file=open_file.read()
print(pr_file)

# writing contents into
with open(file=file_loc_1,mode='w') as open_file:
    pr_file = open_file.write("This is a great practice and she's acing it!")
print(pr_file)

# to see the contents open the file again or execute the above lines of code
# with open(file=file_loc_1,mode='r') as open_file:
#     see_cont = open_file.read()
# print(see_cont)