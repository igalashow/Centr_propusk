from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


link = 'https://transport.mos.ru/gruzoviki/reestr'

class MosTransport():
    """ Работа с траспортным порталом Москвы """

    def __init__(self, link):
        self.link = link

    def init_browser(self):
        """ Запуск браузера Chrome """
        print("\nstart browser.. ")
        browser = webdriver.Chrome()
        browser.get(self.link)
        iframe = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))
        browser.switch_to.frame(iframe)
        return browser

    def login_form(self, browser, sip_series='МБ', sip_number='12345678', grz='B777HC777', validity_period='1'):
        """ Заполнение полей формы логина """
        # Выбираем серию пропуска
        select_series = Select(WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "select#sip_search_series"))))
        select_series.select_by_value(sip_series)
        time.sleep(1)

        # Вводим номер пропуска
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#sip_search_number"))
                                         ).send_keys(sip_number)
        time.sleep(1)

        # Вводим госномер
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#sip_search_grz"))
                                         ).send_keys(grz)
        time.sleep(1)

        # Выбираем тип пропуска по времени
        select_period = Select(WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "select#sip_search_typepassvalidityperiod"))))
        select_period.select_by_value(validity_period)
        time.sleep(1)

        # Вводим код капчи
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#sip_search_captcha"))
                                         ).send_keys(grz)


if __name__ == "__main__":
    try:
        mt = MosTransport(link)
        browser = mt.init_browser()
        resp = mt.login_form(browser, sip_series='МБ', sip_number='12345678', grz='B777HC777', validity_period='1')
    finally:
        print("\nquit browser..")
        browser.quit()
