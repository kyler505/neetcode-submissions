class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate product and # of zeroes
        product = 1
        zeroes = 0

        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                product *= num

        # create the result array
        result = []

        for num in nums:
            if zeroes > 1:
                result.append(0)
            elif zeroes == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product//num)

        return result