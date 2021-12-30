my_file = open("question3.txt","w")
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
i=0
while i<len(color):
    print(color[i])
    my_file.write("/n")
    i=i+1
my_file.close()