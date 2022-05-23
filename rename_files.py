import os

# write path where is your folder that includes files
path = "C:/Users/..."

liste=os.listdir(path)

# you can use x variable to rename folders like newfile0.png to newfilex.png
# also you can change png as ".pdf , .jpeg, .jpg" etc. 

x = 0
for i in liste:
    print(path+i)
    os.rename(path + i ,path + "newName" + str(x) + ".png")
    x += 1
    print(x)
