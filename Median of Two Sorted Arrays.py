class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        imin = 0
        imax = len(nums1)
        half_len = (len(nums1) + len(nums2) + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < len(nums1) and nums1[i] < nums2[j - 1]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max_of_left

                if i == len(nums1):
                    min_of_right = nums2[j]
                elif j == len(nums2):
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return float(max_of_left + min_of_right) / 2