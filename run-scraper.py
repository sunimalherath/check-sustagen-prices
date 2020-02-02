import requests
from bs4 import BeautifulSoup

pricing_list = []

# Extract Chemist Warehouse Diabetic Sustagen Pricing Details

def extract_pricing_info(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0"}

    page = requests.get(url, headers=headers)
    html = BeautifulSoup(page.content, 'html.parser')

    title = html.find("div", class_='product-name').get_text().strip()
    price = html.find("div", class_='product__price').get_text()
    saving = html.find("div", class_='Savings').get_text()

    # add extracted info into a dictionary
    prod_dict = { "Title": title, "Price": price, "Saving": saving}

    return prod_dict


diab_sus_url = 'https://www.chemistwarehouse.com.au/buy/69980/sustagen-diabetic-400g?rcid=948'

diab_sus_dict = extract_pricing_info(diab_sus_url)
# add the above created dictionary to the pricing_list
pricing_list.append(diab_sus_dict)

# Extract Chemist Warehouse Sustagen - Hospital Formula Pricing Details
hos_sus_url = 'https://www.chemistwarehouse.com.au/buy/85205/sustagen-hospital-active-840g-vanilla?rcid=948'

hos_sus_dict = extract_pricing_info(hos_sus_url)
# add the above created dictionary to the pricing_list
pricing_list.append(hos_sus_dict)

# print pricing by looping through the list and each dictionary.
for each_dict in pricing_list:
    print('\n')
    for k, v in each_dict.items():
        print(f"{k} : {v}")