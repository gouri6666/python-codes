#linear search
# l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     if i==7:
#         print("found")
#         break
# else:
#     print("not found")


#binary search
# l=[9,7,78,10,5,1,0]
# l.sort()
# print(l)
# i=0
# j=len(l)-1
# s=11
# while i<j:
#     mid=(i+j)//2
#     if l[mid]==s:
#         print(mid,"found")
#         break
#     elif l[mid]>s:
#         j=mid-1
#     else:
#         i=mid+1
# else:
#     print("not found")


#1.bubble sort
# l=[9,7,97,10,5,1,0]
# for i in range(0,len(l)-1):
#     for j in range(0,len(l)-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

#2. selection sort
# b=[6,5,4,3,21,19,10]
# for i in range(0,len(b)-1):
#     m=i
#     for j in range(i+1,len(b)):
#         if b[m]>=b[j]:
#             m=j
#     b[i],b[m]=b[m],b[i]
# print(b)

#####sorting###

#3.insertion sort
# b=[3,4,5,6,19,21,10]
# for i in range(1,len(b)):
#     j=i-1
#     a=b[i]
#     while j>=0 and b[j]>a:
#         b[j+1]=b[j]
#         j-=1
#     b[j+1]=a
# print(b)


# 4.merge sort
# def merge(arr,beg,mid,end):
#     n1=mid-beg+1
#     n2=end-mid
#     i=j=0
#     left=arr[beg:mid+1]
#     right=arr[mid+1:end+1]
#     k=beg
#     while i<n1 and j<n2:
#         if left[i]<right[j]:
#             arr[k]=left[i]
#             i+=1
#         else:
#             arr[k]=right[j]
#             j+=1
#         k+=1
#     while i<n1:
#         arr[k]=left[i]
#         k+=1
#         i+=1
#     while j<n2:
#         arr[k]=right[j]
#         k+=1
#         j+=1
# def mergesort(arr,beg,end):
#     if beg<end:
#         mid=(beg+end)//2
#         mergesort(arr,beg,mid)
#         mergesort(arr,mid+1,end)
#         merge(arr,beg,mid,end)
# a=[8,7,6,4,3,2,1]
# b=0
# e=len(a)-1
# mergesort(a,b,e)
# print(a)

#5.quick sort
# def partition(arr,low,high):
#     pivot=arr[low]
#     start=low+1
#     end=high
#     while True:
#         while start<=end and arr[start]<=pivot:
#             start+=1
#         while start<=end and arr[end]>pivot:
#             end-=1
#         if start<end:
#             arr[start],arr[end]=arr[end],arr[start]
#         else:
#             break
#     arr[low],arr[end]=arr[end],arr[low]
#     return end
# def quicksort(arr,beg,end):
#     if beg<end:
#         p=partition(arr,beg,end)
#         quicksort(arr,beg,p-1)
#         quicksort(arr,p+1,end)
# a=[8,7,6,4,3,2,5]
# b=0
# e=len(a)-1
# quicksort(a,b,e)
# print(a)        

nums=[-1,0,3,5,9,12]
nums.sort()
i=0
j=len(nums)-1
target=9
while i<j:
            mid=(i+j)//2
            if nums[mid]==target:
                print(mid)
                break
            elif nums[mid]>target:
                j=mid-1
            else:
                 i=mid+1