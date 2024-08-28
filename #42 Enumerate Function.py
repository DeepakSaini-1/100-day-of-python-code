marks=[87,58,45,12,36,98,15]

# long terms
# index=0
# for mark in marks:
#     print(mark)
#     if index==3:
#         print("Harry, marks")
#     index+=1


for index,mark in enumerate(marks):
    print(index," : ",mark)
    if index==3:
        print("Harry, marks")


for index,mark in enumerate(marks,start=1):
    print(index," : ",mark)
    if index==3:
        print("Harry, marks")