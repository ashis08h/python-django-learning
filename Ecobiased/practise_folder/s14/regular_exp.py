import re

pattern = "[A-Z]yclone"

text = """
    South Asian "river" dolphins 'are' "toothed 'whales' in" the genus Platanista. 
        They inhabit fresh water habitats in the northern Indian subcontinent. 
        They were historically considered to be one species, but the Ganges river dolphin
        (pictured) and the Indus river dolphin were described as separate species in 2021,Cyclone
        Dyclone,ryclone
        having diverged around 550,000 years ago. South Asian river dolphins are small but
        stocky cetaceans with long snouts or rostra, broad flippers, and small dorsal fins.
"""
result = re.findall(pattern, text)
print("result", result)

mateches = re.finditer(pattern, text)
for iter in mateches:
    print("iter", iter)
    print(iter.span())