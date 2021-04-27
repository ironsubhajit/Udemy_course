from selenium import webdriver

from pages.quotes_page import QuotePage, InvalidTagForAuthorError


try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter Your tag: ")

    # executable_path = PATH where de-compressed 'chromedriver' is located
    chrome = webdriver.Chrome(executable_path="S:\software_backUp\chromedriver_win32\chromedriver.exe")
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotePage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
    available_tags = page.get_available_tags()
    print("Select one of these tags: [{}]".format(" || ".join(available_tags[1:])))  # exclude first '------' tag choice
except Exception as e:
    print(e)
    print("An unknown error occurred! Please try again.")
