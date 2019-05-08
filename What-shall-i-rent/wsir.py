import pandas
import requests
from bs4 import BeautifulSoup

#Initial variables to get the program to search a given estates website
city = "London"
radius = 15
base_url = "https://www.century21uk.com/property-search/?location=" + \
    city + "%2C+UK&min=0&radius=" + str(radius) + "&ownership=lettings"

#finds sections of site that detail the total number of pages
soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
page_numbers = soup.find_all("ul", {"class": "page-numbers"})
for i in page_numbers:
    total_pages = i.find_all("li")[4].text

#creates a list of dictionaries each containing the data of a single property
l = []
for page in range(1, int(total_pages)+1):
    r = requests.get(base_url + "&cpage=" + str(page))
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class": "property-tile"})
    for item in all:
        d = {}
        #Pulls price
        for w in item.find("p", {"class": "price"}).text.split():
            if "£" in w:
                d["price"] = w
                break
        #Pulls number of bedrooms, bathrooms and living rooms
        #This for loop needs a lot of love, will clean up at later stage
        for i in range(len(item.find("ul", {"class": "key-features"}).text.split())):
            if i == 0:
                d["bedrooms"] = item.find(
                    "ul", {"class": "key-features"}).text.split()[i]
            if i == 1:
                d["bathrooms"] = item.find(
                    "ul", {"class": "key-features"}).text.split()[i]
            if i == 2:
                d["living_rooms"] = item.find(
                    "ul", {"class": "key-features"}).text.split()[i]
        #Pulls the url of the property on the site and also pulls the address if available from within that url
        for i in str(item.find("a", {"class": "tile-snippet"})).split():
            if "href" in i:
                d["url"] = "https://www.century21uk.com" + i[6:-2]
                try:
                    d["address"] = BeautifulSoup(requests.get(d["url"]).content, "html.parser").find(
                        "div", {"class": "office-details"}).find("p").text
                except:
                    d["address"] = None
        l.append(d)
    print("Page number: " + str(page) + " has been scanned.")

#Stores the dictionary list as a DataFrame object that can then be exported to a csv file.
df = pandas.DataFrame(l)
df.to_csv("Century_Output.csv")
