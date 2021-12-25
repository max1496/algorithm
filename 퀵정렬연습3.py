arr=[3,4,2,1,5]
def quick_sort(arr,s,e):
    if s>=e:
        return
    p=s
    l=s+1
    r=e
    while l<=r:
        while l<=e and arr[l]<=arr[p]:
            l+=1
        while r>s and arr[r]>=arr[p]:
            r-=1
        if l>r:
            arr[p],arr[r]=arr[r],arr[p]
        else:
            arr[l],arr[r]=arr[r],arr[l]
    quick_sort(arr,s,r-1)
    quick_sort(arr,r+1,e)
quick_sort(arr,0,len(arr)-1)