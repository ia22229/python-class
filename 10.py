# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)
        
# i=1
# while i<4:
#     j=1
#     while j<4:
#         print(i,j)
#         j+=1
#     i+=1



# for i in range(1,6):
#     for j in range(1,6):
#         print('a',end='\t')
#     print("\n")
    
# i=1
# while i<6:
#     j=1
#     while j<i+1:
#         print(j,end='\t')
#         j+=1
#     i+=1
#     print("\n")

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='\t')
#     print("\n")

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='\t')
    print("\n")
    
i=5
while i>0:
    j=1
    while j<i+1:
        print(j,end='\t')
        j+=1
    i-=1
    print("\n")