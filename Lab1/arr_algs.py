#Поиск минимума
def minSearch(arr):
    elem=arr[0]
    i=1
    while(i<len(arr))
        if(elem<arr[i]):
            elem=arr[i]
        i+=1
    return (elem)

def ArifmMid(arr):
    mid=0
    for elem in arr:
        mid+=elem
    mid=mid/len(arr)
    return(mid)



arr=[-78,5,1,78,23,4,5]
l=[5,3,7,1,2]
print(minSearch(arr))
print(minSearch(l))
print(ArifmMid(arr))
print(ArifmMid(l))