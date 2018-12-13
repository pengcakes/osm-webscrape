'''
Opens 'x' page and scans by h1 and class name
Returns results (if any to .csv)

'''
import csv
import pickle
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup


def scrape():
	for pg in quote_pages:
		# query the website and return the html to the variable ‘page’
		page = urlopen(pg)

		# parse the html using beautiful soup and store in variable `soup`
		soup = BeautifulSoup(page, "html.parser")

		# Take out the <div> of name and get its value
		name_box = soup.find("h1", attrs={"class": "firstHeading"})

		# strip() is used to remove starting and trailing
		name = name_box.text.strip() 
		# # get the index price
		# price_box = soup.find("div", attrs={"class":"price"})
		# price = price_box.text
		# print(price)
		data.append(name)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

# names = load_obj("kodak_names")
# print(names)
data = []
quote_pages = ["https://en.wikipedia.org/wiki/Willis_Tower", "https://en.wikipedia.org/wiki/Empire_State_Building"]

scrape()
print(data)


# # open a csv file with append, so old data will not be erased
# with open("index.csv", "a") as csv_file:
#  writer = csv.writer(csv_file)
#  for name in data:
#  	writer.writerow([name, datetime.now()])



