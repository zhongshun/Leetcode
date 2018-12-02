nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

k = m + n - 1
if m == 0:
    for i in range(n):
        nums1[i] = nums2[i]
k = m + n - 1
while m > 0 and n > 0:
    if nums1[m-1] >= nums2[n-1]:
        nums1[k] = nums1[m-1]
        k = k - 1
        m = m - 1
    else:
        nums1[k] = nums2[n-1]
        k = k - 1
        n = n - 1
while n > 0 or m > 0:
    if m > 0:
        nums1[k] = nums1[m-1]
        k = k - 1
        m = m - 1
    else:
        nums1[k] = nums2[n-1]
        k = k - 1
        n = n - 1

print(nums1)
print(nums2)
