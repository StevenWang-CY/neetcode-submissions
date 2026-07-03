class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # 保证 A 是较短的数组
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = (total + 1) // 2

        left, right = 0, len(A)

        while left <= right:
            i = (left + right) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            # 找到了正确切分
            if Aleft <= Bright and Bleft <= Aright:
                # 总长度是奇数
                if total % 2 == 1:
                    return float(max(Aleft, Bleft))

                # 总长度是偶数
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # A 的左边太大了，说明 i 切太靠右
            elif Aleft > Bright:
                right = i - 1

            # B 的左边太大了，说明 A 切太靠左
            else:
                left = i + 1