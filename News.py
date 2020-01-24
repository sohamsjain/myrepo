import json

final = {}

def add_month(month):
    print("Month {} created successfully!".format(month))
    news_dict = {}
    news = input("Add news: ")
    while news != "done":
        news_dict.update(add_news(news))
        news = input("Add News: ")

    with open('news.json', 'w') as f:
        json.dump({month: news_dict}, f)


def add_news(news):
    print("News created successfully!")
    element_dict = {}
    element = input("Add concerned element: ")
    while element != "done":
        change = float(input("Add Change: "))
        element_dict.update({element: change})
        element = input("Add concerned element: ")
    return {news: element_dict}

month = input('Add month: ')
while month != 'done':
    add_month(month)
    month = input("Add month: ")

with open('news.json', 'r') as f:
    months = json.load(f)
    print(months)
