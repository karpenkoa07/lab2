import csv
import random
import xml.etree.ElementTree as ET
from collections import Counter


with open('books.csv') as f:
    rows = list(csv.DictReader(f, delimiter=';'))


TITLE = 'Название'
AUTHOR = 'Автор'
DATE = 'Дата поступления'


# task 1
print('Task 1')
amount_of_books = 0
for r in rows:
    if len(r[TITLE]) > 30:
        amount_of_books += 1

print(amount_of_books)

input('press enter')


# task 2
print('Task 2')
search_result = []
author_search = input('Введите имя автора: ')
for r in rows:
    if author_search in r.get(AUTHOR, ''):
        year = int(r[DATE].split('.')[-1].split()[0])
        if year >= 2018:
            search_result.append(r)

if not search_result:
    print('Нет книг этого автора, вышедших с 2018 года.')
else:
    for r in search_result:
        print(f"{r[TITLE]} - {r[AUTHOR]} - {r[DATE]}")

input("press enter")


# task 3
bibs = random.sample(rows, 20)
with open('bibliosearch.txt', 'w', encoding='utf-8') as f:
    for i, b in enumerate(bibs, 1):
        f.write(f"{i}. {b[AUTHOR]} - {b[TITLE]} - {b[DATE]}\n")
print('Task 3')
print('file "bibliosearch.txt" is done')

input("press enter")


# task 4
print('Task 4')
parsing = ET.parse('currency.xml')
root = parsing.getroot()

output = {}

for i in root.findall('.//Valute'):
    nominal = int(i.find('Nominal').text)
    NAME = i.find('Name').text
    CHAR_CODE = i.find('CharCode').text
    output[NAME] = CHAR_CODE

print('The charcodes are:')
for NAME, CHAR_CODE in output.items():
    print(f"{NAME} - {CHAR_CODE}")

input("press enter")


print('Extra task 1')
tags = {l.tag for l in root.iter()}
print("The tags are:")
for tag in sorted(tags):
    print(tag)

input("press enter")


print('Extra task 2')
top20 = Counter(r['Название'] for r in rows).most_common(20)
for n, (TITLE, count) in enumerate(top20, 1):
    print(f"{n}. {TITLE} - {AUTHOR} - {count}")

input("press enter")
print('Tasks are completed')
