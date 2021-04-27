import csv

import requests

from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup as bs


browser = webdriver.Firefox(executable_path='geckodriver.exe')
browser.implicitly_wait(5)

browser.get('https://www.booking.com/')


with open('Test.csv', 'r') as f_read:
    lines = f_read.readlines()
    lines_3 = lines[:5]
    header = lines[0].strip().split(",")
    lines_3 = [line.strip().split(",") for line in lines_3[1:]]

found_hotel_link = []


def search_hotel(name, search_input):
    # search_input = browser.find_element_by_css_selector("input[id='ss']")
    search_input.clear()
    search_input.send_keys(name)
    print(f"Searching for: {name}...")
    search_button = browser.find_element_by_xpath("//button[@class='sb-searchbox__button '][@type='submit']")
    sleep(5)
    browser.execute_script("arguments[0].click();", search_button)
    return


def scrape_address(hotel_page_url):
    response_content = requests.get(hotel_page_url).content
    soup = bs(response_content, 'html.parser')
    li = soup.find_all('span', {'class': 'hp_address_subtitle js-hp_address_subtitle jq_tooltip'})
    address = li[0].text.strip()
    return address


for line in lines_3:
    user_input = browser.find_element_by_css_selector("input[id='ss']")
    user_input.clear()
    search_hotel(line[1], user_input)

    sleep(3)
    hotel_detail = browser.find_element_by_xpath("//a[@class='js-sr-hotel-link hotel_name_link url']")

    hotel_name = hotel_detail.text.split("\n")[0]
    print(f"Hotel Name: {hotel_name}")

    hotel_link = hotel_detail.get_attribute('href').split("?")[0]
    print(f"BCOM base URL: {hotel_link}")

    hotel_address = scrape_address(hotel_link)
    print(hotel_address)

    if (line[1] in hotel_name) and (line[2] in hotel_address) and (line[3] in hotel_address):
        line[-3] = 'FOUND'
        line[-2] = hotel_address
        line[-1] = hotel_link
    elif (line[3] in hotel_address) or (line[4] in hotel_address) or (line[5] in hotel_address):
        line[-3] = 'PROBABLY FOUND'
    else:
        line[-3] = 'NOT FOUND'

    #line: ['34', 'Hotel Veneto Palace', 'Via Piemonte 63', '00187', 'Roma', 'Italia', '0', 'FOUND', '', '']
    print(f"Line: {line}\n")


with open('output.csv', 'w', newline='') as file:
    f_writer = csv.writer(file)
    f_writer.writerow(header)
    for line in lines_3:
        print(f"line: {line}\n")
        f_writer.writerow(line)





# ADDRESS = browser.find_element_by_xpath()
# STATUS = False # Good match = FOUND, No Good Match = NOT FOUND, else PROBABLY FOUND (city, postcode)

# BCOM_URL = browser.find_element_by_xpath()



sleep(50)
browser.close()


