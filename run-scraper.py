import requests
from bs4 import BeautifulSoup

#cw - Chemist Warehouse
cw_diab_sus_url = 'https://www.chemistwarehouse.com.au/buy/69980/sustagen-diabetic-400g?rcid=948'

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0"}

cw_diab_sus_pg = requests.get(cw_diab_sus_url, headers=headers)

cw_diab_sus_html = BeautifulSoup(cw_diab_sus_pg.content, 'html.parser')

#cw_diab_sus_title = cw_diab_sus_html.find(text='Sustagen Diabetic 400g')
cw_diab_sus_title = cw_diab_sus_html.find("div", class_='product-name').get_text().strip()
cw_diab_sus_price = cw_diab_sus_html.find("div", class_='product__price').get_text()
cw_diab_sus_saving = cw_diab_sus_html.find("div", class_='Savings').get_text()

print(cw_diab_sus_saving)