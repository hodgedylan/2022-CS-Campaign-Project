import bs4
from playwright.sync_api import sync_playwright
from requests_html import HTMLSession
from selenium import webdriver

##Check beautifulsoup4 version
print(bs4.__version__)

def get_webpage():

    url = "https://secure.sos.state.or.us/orestar/gotoPublicTransactionSearch.do?"
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    ##TLDR future Dylan. Tried various web session html request packages, and finally playwright. None were able to
    ##overcome the javascript error. I tried changing p.chromium.launch() to firefox, but can't figure out
    ##how to install that. I can try different browsers, that may be a potential solution.

    ##playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_extra_http_headers(headers)
        page.goto(url)
        # Wait for JavaScript to render the page
        page.wait_for_load_state('networkidle')
        # Get the rendered HTML content
        html_content = page.content()
        print(html_content)
        browser.close()
    return html_content

    ####Selenium
    # options = webdriver.ChromeOptions()
    # options.add_argument("--enable-javascript")
    # driver = webdriver.Chrome(options=options)
    # driver.get(url)
    # # Get the page source after JavaScript execution
    # page = driver.page_source
    # # Close the webdriver
    # driver.quit()

    ####requests
    # ##Create HTML request to Orestar website
    # session = HTMLSession()
    # page = session.get(url=url, headers=headers)
    # page.html.render()



    soup = bs4.BeautifulSoup(page, "html.parser")
    print(soup)


##main method
if __name__ == '__main__':
    get_webpage()

