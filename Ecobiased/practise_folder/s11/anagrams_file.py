def is_anagram(s1, s2):

    if len(s1) != len(s2):
        return "No"
    else:
        count = 0
        for char in s1:
            if char in s2:
                if s1.count(char) != s2.count(char):
                    continue
                count += 1
        if count == len(s1):
            return 'Yes'
        else:
            return 'No'


print(is_anagram('abcd', 'dcba'))
print(is_anagram('bad', 'dad'))
print(is_anagram('dad', 'bad'))
print(is_anagram('dab', 'abd'))