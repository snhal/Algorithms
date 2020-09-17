
def quicksort(l,h):
    if l<h:
        x = partition(l,h)
        quicksort(l,x-1)
        quicksort(x+1,h)
    return

def partition(l,h):
    p = a[h]
    low = l
    high = h-1

    while True:
        while a[low] < p:
            low += 1
            if low == h:
                break

        while a[high] > p:
            high -= 1
            if high == l:
                break

        if low < high:
            a[low], a[high] = a[high], a[low]
        else:
            break

    a[h], a[low] = a[low], a[h]
    return low

def issorted(a):
    for i in range(0,len(a)-1):
        if not a[i] < a[i+1]:
            return False
    return True


if __name__ == '__main__':
    a = [7, 2, 5, 1, 8]
    quicksort(0,len(a)-1)
    print('Sorted array:', a)
    assert issorted(a), 'Error sorting'

