from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_arr = []
        for i in nums:
            num = i
            counter = 0
            for j in nums:
                if num == j:
                    counter += 1
            num_arr.append(counter)

        max_num = max(num_arr)

        total = 0
        for i in num_arr:
            if i == max_num:
                total += i

        return int(total/max_num)
    

s = Solution()
ans = s.maxFrequencyElements([1,2,3,4,5])
print(ans)


# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         freq_counter = Counter(nums)
        
#         max_frequency = max(freq_counter.values())

#         max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]

#         total_frequency = max_frequency * len(max_freq_elements)

#         return total_frequency

# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         return prod(max(Counter(Counter(nums).values()).items()))