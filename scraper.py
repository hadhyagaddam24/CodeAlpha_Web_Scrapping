import requests
from bs4 import BeautifulSoup
import csv
url = "https://books.toscrape.com./"
response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article",class_="product_pod")
data = []
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    rating =book.find("p",class_="star-rating")["class"][1]
    availability = book.find("p",class_="availability").get_text(strip=True)
    data.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability
    })
with open("books.csv", "w", newline="",encoding="utf-8") as file:
    writer = csv.DictWriter(file,fieldnames=["Title", "Price", "Rating", "Availability"])
    writer.writeheader()
    writer.writerows(data)
print("Data saved to books.csv")
