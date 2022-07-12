import json
from collections import Counter

jsonFile = open('watch-history.json', encoding="utf8")

data = json.load(jsonFile)

#! Channels List
initialList = []

for i in data:
    tempTitle = i.get('subtitles')
    if tempTitle != None:
        initialList.append(str(tempTitle))

result = [
    str(item) + ' count: ' + str(c) 
    for item, c in Counter(initialList).most_common() 
]

myFile = open("Channels List.txt", "w",  encoding="utf-8")
myFile.write("\n".join(map(str, result)))
myFile.close()


#! Videos List
initialList = []

for i in data:
    tempTitle = i.get('title')
    if tempTitle != None:
        initialList.append(str(tempTitle))

result = [
    item + ' count: ' + str(c) 
    for item, c in Counter(initialList).most_common()
    if(item != "Watched a video that has been removed")
]

myFile = open("Videos List.txt", "w",  encoding="utf-8")
myFile.write("\n".join(map(str, result)))
myFile.close()