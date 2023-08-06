from .pickle import Pickle

class Automation:
    class NoIp:
        def __init__(self):
            import random

            self.session_id = random.randint(1, 100000)
            self.driver = None

        def open_browser(self):
            from selenium import webdriver

            self.driver = webdriver.Chrome()

        def update(self, username: str, password: str, threaded=False, looped=False, days_delay=0):
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.action_chains import ActionChains
            from selenium.webdriver.common.keys import Keys
            import time, threading, os, datetime

            def action():
                self.open_browser()

                self.driver.get("https://no-ip.com/")
                self.driver.implicitly_wait(10)

                self.driver.find_element(By.CSS_SELECTOR, "#topnav > li:nth-child(1)").click()
                self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)
                self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
                self.driver.find_element(By.CSS_SELECTOR, "#clogs-captcha-button").click()

                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".border-noip-logo-dark-grey.border-0 > strong > a"))
                )
                time.sleep(2)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()

                self.driver.find_element(
                    By.CSS_SELECTOR,
                    "div.grid-row.mb-30 > div:nth-child(1) > div"
                ).click()

                input("Нажмите Enter для продолжения")

            def action_loop():
                result = False

                update = Pickle("noip_update.sbdt")
                if "noip_update.sbdt" not in os.listdir():
                    update.pick(datetime.datetime.now() - datetime.timedelta(days=days_delay + 1))

                while True:
                    if update.unpick() + datetime.timedelta(days=days_delay) < datetime.datetime.now():
                        update.pick(datetime.datetime.now())
                        action()
                        result = True
                    if not looped:
                        break

                    time.sleep(60 * 60 * 12)

                return result

            if threaded:
                #
                threading.Thread(target=action_loop, daemon=True).start()

            else:
                return action_loop()

    class Requests:
        def __init__(self):
            pass

        def post(self, url: str, data: dict):
            import requests

            return requests.post(url, data=data)

    class CRM:
        def __init__(self):
            pass
