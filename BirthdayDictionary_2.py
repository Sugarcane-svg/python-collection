"""
modify the program from part 1 to load the birthday dictionary from a JSON file on disk, rather than having dictionary defined in the program
"""
import BirthdayDictionary_1
import json

with open("simple_json.json", "w") as f:
    json.dump(BirthdayDictionary_1.bd, f)

with open("simple_json.json", "r") as f:
    bd = json.load(f)

if bd['a']:
    BirthdayDictionary_1.print_bd("a")