import pandas
import re
from bs4 import BeautifulSoup
from collections import Counter
import random
import random
import pandas

colours = []
dress_table = pandas.read_html('file:///C:/Users/Queen/Desktop/BINCOMTEST/bincom.html')[0]
for i in dress_table['COLOURS']:
    colour_list = i.split(', ')
    colours.append(colour_list)
duplicate_colours = []
for x in colours:
    for y in x:
        duplicate_colours.append(y)
non_duplicates = list(set(duplicate_colours))
#print(non_duplicates)
#print(Counter(duplicate_colours)['BLUE'])
#Number 1
mean_colour = len(duplicate_colours)/len(non_duplicates)
print("1. The mean colour is ",mean_colour)

#Number 2
most_worn = Counter(duplicate_colours).most_common(1)
print("2. The mos worn is ", most_worn)

listValues = [i for i in Counter(duplicate_colours).values()]

#Number 4
variance = sum((x - mean_colour) ** 2 for x in listValues) / len(listValues)
print("4. The variance is ", variance)

#Number 5
prob_red = duplicate_colours.count('RED')/len(duplicate_colours)
print("5. Probability of red is ",prob_red)



#Number 8
test_list = [0,1]
randList = [1]
for i in range(3):
    randList.append(random.choice(test_list))

index = []
i = len(randList)- 1
while i >= 0:
    index.append(i)
    i -= 1

df = pandas.DataFrame({
    'Num':randList,
    'Index':index
})
df['Powers'] = df['Num'] * 2**(df['Index'])

number = ''
for i in randList:
    number += str(i)

print("8a. The random binary number is ", int(number))
print("8b. The number in base ten is ", sum(df['Powers']))


#Number 9
first = 0
second = 1
i = 1
fibList = []
fibList.append(first)
fibList.append(second)
while i <= 48:
    third = first + second
    first = second
    second = third
    fibList.append(third)
    i +=1
print("9 The sum of the first 50 Fibonacci number is ", sum(fibList))