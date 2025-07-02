def is_anagrams(s1, s2):
    if len(s1) != len(s2):
        print("No")
    else:
        count = 0
        for item in s1:
            if item in s2:
                if s1.count(item) != s2.count(item):
                    continue
                count += 1
        if len(s1) == count:
            print("Yes")
        else:
            print("No")


is_anagrams('abcd', 'dcba')
is_anagrams('bad', 'dad')
is_anagrams('dad', 'bad')
is_anagrams('dab', 'abd')