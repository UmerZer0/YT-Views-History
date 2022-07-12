# Python code to demonstrate
# sort list by frequency
# of elements

from collections import Counter

ini_list = [1, 2, 3, 4, 4, 5, 5, 5, 5, 7,
			1, 1, 2, 4, 7, 8, 9, 6, 6, 6]
            
print(*sorted(Counter(ini_list).most_common()), sep = "\n")
# printing initial ini_list
# print ("initial list", str(ini_list))

# sorting on basis of frequency of elements
result = [str(items) + ' count: ' + str(c) for items, c in Counter(ini_list).most_common()]
