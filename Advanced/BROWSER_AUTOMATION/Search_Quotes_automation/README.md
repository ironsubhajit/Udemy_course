# Browser Automation with Selenium

The code is very similar to webscraping([`my_repo`](https://github.com/ironsubhajit/WebScraping)), but this time launching chrome browser instead of
requesting the page with Python and controlling the browser, instead of just getting HTML.
## Requirements
* `Selenium` library
* A WebDriver ([Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/))
### Selenium
Install `selenium` in your Virtual Environment
### WebDriver
Each of the major browsers releases a webdriver for their browser. It essentially allows other applications to interact with the browser. Here i'm using 
[`Chrome WebDriver`](https://sites.google.com/a/chromium.org/chromedriver/).
<br>Make sure to download the version for your browser (e.g v84 if you're using Chrome v84) and de-compressed executable.
## Project List
1. Search_Quote_Automation : [`Quotes to Scrape`](http://quotes.toscrape.com/search.aspx)