color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('color.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('color.txt')
print(content.read())
