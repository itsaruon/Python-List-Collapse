import random
k = random.randint(2,11)

k = int(input("Enter the number :"))
list =[]

for x in range(k):
    num = random.randint(2,10)
    print("Enter value ",x+1,":",num)
    list.append(num)
def collapse(list):
    l = len(list)
    newList = []
    for i in range(1,l,2):
        newList.append(list[x]+list[x-1])
    if l%2==1:
        newList.append(list[l-1])
    return newList

print("Old List: ",list)
print("Collapse List: ",collapse(list))
