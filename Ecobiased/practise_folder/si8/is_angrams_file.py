def is_angrams(s1, s2):
    count = 0
    if len(s1) != len(s2):
        return 'no'
    else:
        for char in s1:
            if char in s2:
                if s1.count(char) != s2.count(char):
                    continue
                count += 1
    if count == len(s2):
        return 'yes'
    else:
        return 'no'


print(is_angrams('abcd', 'dcab'))
print(is_angrams('bad', 'dad'))
print(is_angrams('dad', 'bad'))

