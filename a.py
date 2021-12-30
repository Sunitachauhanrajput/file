def file_read(fname):
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises\n")
                myfile.write("sunita")
        txt = open(fname)
        print(txt.read())
file_read('dgh.txt')
