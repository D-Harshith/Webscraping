from bs4 import BeautifulSoup
# import lxml
import requests


response = requests.get(url="https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)  # or use article_tag.string
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
# print(article_texts)
# print(article_upvotes)
# print(article_links)
















with open("website.html", encoding="utf8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
# print(soup.a)
# # print(soup.ul.prettify())
# all_paragraphs = soup.find_all(name="p a")
# print(all_paragraphs)
# for i in all_paragraphs:
#     print(i.getText())
# # print(soup.a)
# company_url = soup.select_one(selector="p a")  # This is css selector.
# # print(company_url)
# name = soup.select_one("#name")
# heading = soup.select_one(".heading")
# # print(name)
# print(heading)


