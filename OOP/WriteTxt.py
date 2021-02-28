# read the file and store all the lines in list
# reverse the list 
# write the list back to the file

with open('.\\OOP\\test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content) # reverse the content 

    with open('.\\OOP\\test.txt', 'w') as writer:
        for i in reversed(content):
            writer.write(i)