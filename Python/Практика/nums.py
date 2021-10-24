nums = [1, 3, 3, 3, 2, ]


def incrementer(nums):
    x = 0
    b = []
    for i in nums:
        x += 1
        i = x + i
        b.append(i)
        i += 1
    return [i % 10 if len(str(abs(i))) >= 2 else i for i in b]


########################################################################################
def incrementer2(nums):
    return [(n + i) % 10 for i, n in enumerate(nums, 1)]


incrementer2(nums)
incrementer(nums)
