import os
from dotenv import load_dotenv
from main.CovidDataScraper import CovidDataScraper
load_dotenv()

PATH_TO_CHROME_DRIVER = os.getenv("DRIVER_PATH")

print('------- Covid 19 Information -------')

scrapper = CovidDataScraper(PATH_TO_CHROME_DRIVER)

total_cases_ON, new_cases_ON, active_cases_ON, tests_done_ON = scrapper.scrape_ontario()

print('Ontario:')
print('Total Cases:', total_cases_ON)
print('Active Cases:', active_cases_ON)
print('New Cases Today:', new_cases_ON)
print('Tests Done Today:', tests_done_ON)
print('------------------------------------')

