def is_anagrams(s1, s2):
    if len(s1) != len(s2):
        return "No"
    else:
        count = 0
        for char in s1:
            if char in s2:
                if s1.count(char) != s2.count(char):
                    continue
                count = count + 1
        if count == len(s2):
            return "Yes"
        else:
            return "No"


print(is_anagrams('abcd', 'dcba'))
print(is_anagrams('bad', 'dad'))
print(is_anagrams('dad', 'bad'))
print(is_anagrams('dab', 'abd'))