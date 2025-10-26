import csv, random
import xml.etree.ElementTree as ET
from collections import Counter

with open('books.csv') as f:
    rows = list(csv.DictReader(f, delimiter = ';'))

title = 'Название'
author = 'Автор'
date = 'Дата поступления'


#task 1
print('Task 1')
amount_of_books = 0
for r in rows:
    if len(r[title]) > 30:
        amount_of_books +=1

print(amount_of_books)

input('press enter')
#task 2
print('Task 2')
author_search = input('Who is the author of the book?')
search_result = []
for r in rows:
    try:
        year = int(r[date].split('.')[-1].split()[0])
        if author_search in r[author] and (year >= 2018):
            search_result.append(r)
    except:
        pass

for r in search_result[:10]:
    print(r[title], '-', r[author], '-', r[date])

input("press enter")
#task 3
bibs = random.sample(rows, 20)
with open('bibliosearch.txt', 'w', encoding='utf-8') as f:
    for i, b in enumerate(bibs, 1):
        f.write(f"{i}. {b[author]} - {b[title]} - {b[date]}\n")
print('Task 3')
print('file "bibliosearch.txt" is done')
input("press enter")


#task 4
print('Task 4')
parsing = ET.parse('currency.xml')
root = parsing.getroot()

output = {}

for i in root.findall('.//Valute'):
    nominal = int(i.find('Nominal').text)
    name = i.find('Name').text
    char_code = i.find('CharCode').text
    output[name] = char_code

print('The charcodes are:')
for name, char_code in output.items():
    print(f"{name} - {char_code}")

input("press enter")

print('Extra task 1')
tags = {l.tag for l in root.iter()}

print("The tags are:")
for tag in sorted(tags):
    print(tag)

input("press enter")

print('Extra task 2')

top20 = Counter(r['Название'] for r in rows).most_common(20)
for n, (title, count) in enumerate(top20, 1):
    print(f"{n}. {title} - {author} - {count}")

input("press enter")
print('Tasks are completed')