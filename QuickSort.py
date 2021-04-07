def partition(array, l, h):
    pivot = l
    i = l
    j = h

    while i < j:
        while array[pivot] >= array[i] and i<h:
            i += 1
        while array[pivot] <= array[j] and j>l:
            j -= 1
        
        if i < j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    
    temp = array[pivot]
    array[pivot] = array[j]
    array[j] = temp
    return j


def MergeSort(array,l,h):
    if l < h:
        p = partition(array, l, h)
        MergeSort(array,l, p - 1)
        MergeSort(array,p + 1, h)
    else:
        return

array = [6, 3, 5,99,0, 1, 4, 2,8]
MergeSort(array,0,len(array)-1)
print(array)
