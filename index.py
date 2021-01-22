from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.konga.com/?gclid=CjwKCAiA6aSABhApEiwA6Cbm_xhudnwzg93bX92wUXEe31MbR6M5KRRfQ3bGBjRICTKSYnYVyRBzIRoCf8MQAvD_BwE"

# open the url
request_page = urlopen(url_to_scrape)
# reah the page
page_html = request_page.read()
# close request
request_page.close()
# parse page as html
html_soup = BeautifulSoup(page_html, 'html.parser')

konga_items = html_soup.find_all('a', class_='a2cf5_2S5q5 f0924_2qLSo')
# create a csv file
filename = 'product.csv'

f = open(filename, 'w')

headers = 'Title, Price, Image \n'

f.write(headers)

for item in konga_items:
    img = item.find('img', class_='f5e10_VzEXF')['src'].encode('utf-8').decode('ascii', 'ignore')
    title = item.find('h3', class_='e891d_1EvQ4').text.encode('utf-8').decode('ascii', 'ignore')
    price = item.find('span', class_='d7c0f_sJAqi').text.encode('utf-8').decode('ascii', 'ignore')
    f.write(title + ', ' + price + ', ' + img + '\n')
    # print(type(img))

f.close()
