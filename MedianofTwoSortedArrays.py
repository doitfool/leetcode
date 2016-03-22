"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        i, j = 0, 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        while i < len(nums1):
            nums3.append(nums1[i])
            i+=1
        while j < len(nums2):
            nums3.append(nums2[j])
            j+=1
        length = len(nums3)
        if length % 2 == 0:
            median = 1.0*(nums3[length/2-1]+nums3[length/2]) / 2
        else:
            median = 1.0*nums3[length/2]
        # print nums3
        return median

if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([4,5,9,20], [1,2,6,9,10])
