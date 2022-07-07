import requests


def count_of_animals(link='https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pageuntil='
                          'Азиатский+муравей-портной#mw-pages'):
    '''
    Функция, возвращающая словарь, ключами которого являются уникальные буквы, а значениями - количество животных для
    каждой буквы

    :param link: Ссылка на статью
    :return: Словарь
    '''
    res = requests.get(link)
    ignore_list = ['Служебная:Категории', 'Страница участника для моего IP', 'Страница категории [c]" accesskey="c',
                   'Редактировать данную страницу [v]" accesskey="v', 'Перейти на заглавную страницу [z]" accesskey="z',
                   'Сообщить об ошибке в этой статье', 'Список всех страниц, ссылающихся на данную [j]" accesskey="j',
                   'Создать книгу или коллекцию статей',
                   'Kateqoriya:Əlifba sırasına görə heyvanlar — азербайджанский" lang="az" hreflang="az" '
                   'class="interlanguage-link-target', 'm:Privacy policy/ru', 'Википедия:Описание',
                   'Википедия:Отказ от ответственности']
    animals_dict = dict()
    next_bool = False
    while next_bool or not animals_dict:
        for i in res.text.splitlines():
            if i.find('title="') != -1 and i.find('</a></li>') != -1:
                i = i[i.find('title="') + 7:]
                i = i[:i.find('>') - 1]

                if ignore_list.count(i) == 0:
                    if i[0] in animals_dict:
                        animals_dict[i[0]] += 1
                    else:
                        animals_dict.update({i[0]: 1})
            if i.find('Следующая страница') != -1:
                link = res.url
                if link.find('&pageuntil') != -1:
                    next_bool = True
                    link = link.replace('&pageuntil', '&pagefrom')
                    res = requests.get(link)
                elif i.find(') (<a href="/w/index.php?title=') != -1 and i.find('&amp;') != -1:
                    next_bool = True
                    link = 'https://ru.wikipedia.org'
                    link += i[i.find(') (<a href="/w/index.php?title=') + 12:]
                    link = link[:link.find(' title=') - 1]
                    link = link.replace('amp;', '')
                    res = requests.get(link)
                else:
                    next_bool = False

    return animals_dict


if __name__ == '__main__':
    animals_dict = count_of_animals()

    for keys, values in animals_dict.items():
        print(keys + ': ' + str(values))
