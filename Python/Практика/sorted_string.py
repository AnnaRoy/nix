a1 = 'aaaaff№%:fhytd'
a2 = 'aadfgggfdfgh@'


def longest(str1, str2):
    return "".join(sorted(set(str1 + str2)))
    # str1 + str1 и возвращает строку с каждым символами (каждый символ только один раз)


longest(a1, a2)