from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'https://transport.mos.ru/gruzoviki/reestr'

class MosTransport():
    """ Работа с траспортным порталом Москвы """

    def __init__(self, link):
        self.link = link

    def init_browser(self):
        """ Запуск браузера Chrome """
        print("\nstart browser.. ")
        browser = webdriver.Chrome()
        return browser
        # print("\nquit browser..")
        # browser.quit()

    def login_form(self, browser, sip_series='МБ', sip_number='12345678', grz='B777HC777', validity_period='1'):
        """ Заполнение полей формы логина """
        browser.get(self.link)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))).send_keys(str(math.log(int(time.time()))))
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))).click()



if __name__ == "__main__":
    try:
        mt = MosTransport(link)
        browser = mt.init_browser()
        resp = mt.login_form(browser, sip_series='МБ', sip_number='12345678', grz='B777HC777', validity_period='1')
    finally:
        print("\nquit browser..")
        browser.quit()
# browser = webdriver.Chrome()
# browser.get(link)