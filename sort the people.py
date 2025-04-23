def sort_people(names,heights):
    for i in range(1, len(heights)):
        j = i
        while j > 0 and heights[j-1] < heights[j]:
            heights[j-1], heights[j] = heights[j], heights[j-1]
            names[j-1], names[j] = names[j],names[j-1]
            j-=1
    return names


names = ["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
heights = [17233,32521,14087,42738,46669,65662,43204,8224]

print(sort_people(names,heights))
