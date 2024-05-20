# ● Compute the length of the longest strictly increasing subsequence in a list.
# ○ Input: nums = [11, 5, 2, 5, 3, 7, 101, 18]
# ○ Output: 4
# ○ Explanation: The longest increasing subsequence is [2,3,7,101], therefore
# the length is 4.

def longest_strictly_increasing_sub(arr):
    n = len(arr)

    # Declare the list (array) for longest strictly increasing subsequence and
    # initialize longest strictly increasing subsequence values for all indexes
    lsis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lsis[i] < lsis[j] + 1:
                lsis[i] = lsis[j] + 1

    # Initialize maximum to 0 to get
    # the maximum of all longest strictly increasing subsequence
    maximum = 0

    # Pick maximum of all longest strictly increasing subsequence values
    for i in range(n):
        maximum = max(maximum, lsis[i])

    return maximum


nums = [11, 5, 2, 5, 3, 7, 101, 18]
print("Length of longest strictly increasing subsequence:", longest_strictly_increasing_sub(nums))
