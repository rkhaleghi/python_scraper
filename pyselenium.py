from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path
from vacancy import Vacancy
from selenium.webdriver.chrome.options import Options

# def init_chrome(self):
chrome_options = Options()
chrome_options.add_argument("--headless")
# adding r makes it raw to deal with windows \
chrome_path = r"C:\Users\reza.Khaleghi\PycharmProjects\selenium\chromedriver.exe"
baseurl='https://apply.cygnetjobs.co.uk'
driver = webdriver.Chrome(chrome_path)
driver.get(baseurl + '/vacancies/#results')
button = driver.find_element_by_xpath("//input[@class='button']")
button.click()


path = Path(r'C:\Users\reza.Khaleghi\PycharmProjects\selenium\file.html')
response = path.read_text()
soup = BeautifulSoup(driver.page_source, "html.parser")
vacancy_result = soup.select(".vacancy_result")
vacancy_list = []
for vacancy in vacancy_result:
    title = vacancy.select_one(".vacancy_title").getText()
    location = vacancy.select_one(".value_location_hc").getText().rstrip().strip()
    salary = vacancy.select_one(".value_salary").getText()
    # hours = vacancy.select_one(".value_hours").getText()
    v =Vacancy(title, location, salary, "hours")
    vacancy_list.append(v)

print(vacancy_list)

# next_url = browser.find_element_by_xpath("//div[@class='paging_links']/a/@href")
# browser.get(baseurl+next_url)

