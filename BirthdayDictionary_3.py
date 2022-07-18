"""
load that JSON file from disk, extract the months of all the birthdays, anc count how many people have a birthday in each month
"""
import json
from collections import Counter
def extract_month(dict):
    month=[]
    for i in dict:
        s = dict.get(i).split("/")
        month.append(s[0])
    return month

if __name__ == "__main__":
    bd = {}
    with open("simple_json.json", "r") as f:
        bd = json.load(f)

    month = extract_month(bd)
    c = Counter(month)

    print(c)