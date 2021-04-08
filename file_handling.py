#
# f = open('Questions.txt','r')
#
# #print(f.read())
#
# print("Printing only 1st line")
# # print(f.readline(),end="") # end is added to avoid new line
# # print(f.readline())
# # print(f.readline())
# print(f.readline(4)) #gives 4 characters in a line

### Writing into a file
# f1 = open('abc','w')
# f1.write("Something")
# f1.write(" People")

## Appending text into an existing file
# f1 = open('abc','a')
# f1.write(" Take care")


### Copying data from 'Sample' to 'abc'
# f = open('Sample','r')
#
# f1 = open('abc','w')
#
# for data in f:
#     f1.write(data)


#### Print all the data about the image file
f = open('DSC00007.jpg', 'rb')

# copying the image and making another image
f1 = open('MyPic.jpg', 'wb')

# for i in f:
#     print(i)

for i in f:
    f1.write(i)
