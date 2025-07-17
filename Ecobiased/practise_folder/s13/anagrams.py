def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return "No"
    else:
        count = 0
        for char in s1:
            if char in s1:
                if s1.count(char) != s2.count(char):
                    continue
                count += 1
        if count == len(s2):
            return "Yes"
        return "No"


print(is_anagram('abcd', 'dcba'))
print(is_anagram('bad', 'dad'))
print(is_anagram('dad', 'bad'))
print(is_anagram('dab', 'abd'))