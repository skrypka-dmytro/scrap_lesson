import re

from bs4 import BeautifulSoup

with open("index.html") as file:
    src = file.read()
#print(src)
soup = BeautifulSoup(src, "lxml")
# title = soup.title
# print(title.text)

#.find() .find_oll()
# page_1 = soup.find("h1")
# print(page_1.text)

# page_1_find_all = soup.find_all("h1")
# print(page_1_find_all)
# for page in page_1_find_all:
#     print(page.text)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find("div", class_="user__name").find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id": "lesson"}).find("span").text
# print(user_name)

# find_all_span_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_span_in_user_info)
#
# for item in find_all_span_in_user_info:
#     print(item.text)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_links)
# for links in social_links:
#     print(links)

# all_links = soup.find_all("a")
# print(all_links)
#
# for item in all_links:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")

# .find_parent() .find_parents()

# text_div = soup.find(class_="post__text").find_parent()
# print(text_div)

# text_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(text_div)

# text_div = soup.find(class_="post__text").find_parents("div", "user__post")
# print(text_div)

# .next_element .previous_element

# next_element = soup.find(class_="post__title").next_element.next_element.text
# print(next_element)
#
# next_element = soup.find(class_="post__title").find_next().text
# print(next_element)

# .find_next_sibling() .find_previous_sibling()

# next_sibling = soup.find(class_="post__title").find_next_sibling()
# print(next_sibling)

# prev_sibling = soup.find(class_="post__data").find_previous_sibling()
# print(prev_sibling.text)

# post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text
# print(post_title)

# some_links = soup.find(class_="some__links").find_all("a")
# print(some_links)

# for link in some_links:
#     link_href = link.get("href")
#     link_text = link.text
#     print(f"{link_text}: {link_href}")

# for link in some_links:
#     link_href = link["href"]
#     print(link_href)

# find_a_by_text = soup.find("a", text="Mate academy")
# print(find_a_by_text)

# find_a_by_text = soup.find("a", text=re.compile("Mate"))
# print(find_a_by_text)

find_all_mate = soup.find_all(text=re.compile("([Mm]ate)"))
print(find_all_mate)
