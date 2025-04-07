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

match = re.findall(pattern, text)
matches = re.finditer(pattern, text)
match_all = re.findall(pattern, text)

for iter in matches:
    print(iter)
    print(iter.span())