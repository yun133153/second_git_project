import time
import selenium
from selenium import webdriver

print("연평균 등록금이 궁금한 대학교 3개를 입력하시오(콤마로 구분할 것)")
print("ex : 부산대, 경북대, 부경대")
university_list_string=input(">> : ")
university_list=university_list_string.split(",")

URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

for university_tuition_fee in university_list:
    search_box = driver.find_element_by_name("query")
    search_box.send_keys(university_tuition_fee)
    search_btn = driver.find_element_by_class_name("bt_search")
    search_btn.click()

    title = driver.find_element_by_class_name("main_title").text
    d = driver.find_elements_by_class_name('university_chart')
    e = []
    for i in d:
        f = i.find_elements_by_tag_name('p')
        for d in f:
            d = d.text
            e.append(d)
    fee = e[5]

    print(title + " - " + fee)

    time.sleep(3)
    search_box = driver.find_element_by_name("query")
    search_box.clear()

time.sleep(3)

driver.close()