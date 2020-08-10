import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


class CovidDataScraper:
    ONTARIO_COVID_URL = 'https://www.ontario.ca/page/how-ontario-is-responding-covid-19'
    LONDON_COVID_URL = 'https://www.healthunit.com/covid-19-cases-middlesex-london'

    driver = None

    def __init__(self, driver_path):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)

    def load_page(self):
        body = None
        try:
            # Wait until the first table of Covid data has loaded
            body = self.driver.find_element_by_xpath(
                "//*[@id='pagebody']/table[1]")

            if body.is_displayed():
                return None
            else:
                time.sleep(5)

        except NoSuchElementException:  # Catches element not found exception and tries again
            self.load_page()

    def scrape_ontario(self):
        self.driver.get(self.ONTARIO_COVID_URL)  # Start the browser and to to website

        try:
            self.load_page()

            total_cases = self.driver.find_element_by_xpath("//*[@id='pagebody']/table[1]/tbody/tr[1]//td[1]").text
            new_cases = self.driver.find_element_by_xpath("//*[@id='pagebody']/table[1]/tbody/tr[2]//td[1]").text
            resolved_cases = self.driver.find_element_by_xpath("//*[@id='pagebody']/table[1]/tbody/tr[3]//td[1]").text
            deaths = self.driver.find_element_by_xpath("//*[@id='pagebody']/table[1]/tbody/tr[7]//td[1]").text
            tests_done = self.driver.find_element_by_xpath("//*[@id='pagebody']/table[3]/tbody/tr[2]//td[1]").text

            total_cases = total_cases.replace(',', '')
            new_cases = new_cases.replace(',', '')
            resolved_cases = resolved_cases.replace(',', '')
            deaths = deaths.replace(',', '')
            tests_done = tests_done.replace(',', '')

            self.driver.quit()

            total_resolved = float(resolved_cases) + float(deaths)
            active_cases = (1 - (float(total_resolved) / float(total_cases))) * float(total_cases)

            return int(total_cases), int(new_cases), round(active_cases, 2), int(tests_done)
        except NoSuchElementException:
            self.driver.quit()
