def is_anagrams(s1, s2):
    count = 0
    if len(s1) != len(s2):
        return 'no'
    else:
        for char in s1:
            if char in s2:
                if s1.count(char) != s2.count(char):
                    continue
                count += 1
        if len(s1) == count:
            return 'Yes'
        else:
            return 'No'


print(is_anagrams('abcd', 'dcab'))
print(is_anagrams('bad', 'dad'))
print(is_anagrams('dad', 'bad'))
print(is_anagrams('dab', 'abd'))