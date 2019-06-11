import json
import pprint

jf = open("input.json")
a = json.load(jf)
pprint.pprint(a)
def tester():
    try:
        open("input.json")
    except FileNotFoundError:
        print("file not found")
    try:
        json.load(jf)
    except:
        print("File is not JSON/structure error")

tester()
