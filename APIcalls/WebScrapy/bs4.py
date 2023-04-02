from bs4 import BeautifulSoup4
# import lxml


with open("website.html") as file:
    contents=file.read()

soup=beautifulSoup4(contents,"html.parser")
print(soup.title.name)