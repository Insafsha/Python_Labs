#количество записей, у которых в поле Название строка длиннее 30 символов
from csv import reader
import random

file = 'books-en.csv'
with open(file, 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    next(table)  
    count = 0
    for row in table:
        if len(row[1]) > 30: 
            count += 1
print(f'Количество записей, у которых строка в поле "Название" длиннее 30 символов: {count}')




#поиск книги по автору
def search_author(file, authorname):
    results = []
    with open(file, 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)  
        for row in table:
            if authorname.lower() in row[2].lower(): 
                results.append(row)
    return results

search = input("Введите имя автора для поиска: ")
books = search_author(file, search)
if books:
    print(f"Найдено {len(books)} книг(и):")
    for book in books:
        print(f"Название: {book[1]}, Автор: {book[2]}, ISBN:{book[0]} ")
else:
    print("Книги данного автора не найдены.")



#генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей
num=20
def indices(file):
    books = []
    with open(file, 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)  
        for index, row in enumerate(table, start=1):  
            books.append({
                'index': index,
                'author': row[2],
                'title': row[1],
                'year': row[3]  
            })
    return books

def generate_b(books, num_r=num):
    random_books = random.sample(books, num_r)  
    bibli = []
    for book in random_books:
        r = f"{book['index']}. {book['author']}. {book['title']} - {book['year']}\n"
        bibli.append(r)
    return bibli

def bibli_file(bibli, filename="result.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(bibli)     

books = indices(file)
bibli = generate_b(books, num_r=num)
bibli_file(bibli)



#Распарсить файл и извлечь данные, согласно варианту. 
import xml.dom.minidom as minidom

xml_f = open('currency.xml', 'r', encoding='windows-1251')
xml_d = xml_f.read()
dom = minidom.parseString(xml_d)
dom.normalize()
el = dom.getElementsByTagName('Valute')
char_codes = []
values = []
for node in el:
    char_code = None
    value = None
    
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3: 
                    char_code = child.firstChild.data

            if child.tagName == 'Value':
                if child.firstChild.nodeType == 3:  
                    value = child.firstChild.data.replace(',', '.')  
                    value = float(value)  

    if char_code and value is not None:
        char_codes.append(char_code)
        values.append(value)
print("CharCode:", char_codes)
print("Value:", values)
xml_f.close()

#доп задание
# Создаем множество для уникальных издательств
publish = set()
with open(file, 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    next(table)  
    for row in table:
        publish.add(row[4]) 
print("Перечень издательств без повторений:")
for publish in sorted(publish):
    print(publish)


#Самые популярные 20 книг(Больше всего загрузок)
books = []
with open(file, 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    next(table)  
    for row in table:
        try:
            downloads = int(row[5])  
            books.append((row[1], downloads))  
        except ValueError:
            continue  
top_20= sorted(books, key=lambda x: x[1], reverse=True)[:20]
print("Самые популярные 20 книг:")
for index, (title, downloads) in enumerate(top_20, start=1):
    print(f"{index}. {title} - {downloads} загрузок")