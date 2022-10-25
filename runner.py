import time
import datetime
import human_delay

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DebugMode:
    @staticmethod
    def log(msg,debug_mode=False):
        if debug_mode:
            print(f"{datetime.datetime.now()}: {msg}")

class Runner:
    def __init__(self, driver, url, steps=[], default_wait=10, debug_mode=True):
        self.driver = driver
        self.steps = steps
        self.debug_mode = debug_mode
        self.default_wait = default_wait
        DebugMode.log(f"<Runner> driver.get({url})", debug_mode)
        self.driver.get(url)

    def run(self):
        # step_name = title
        # condition = (By.XXXX, value)
        # step_fn = step_fn(driver)
        DebugMode.log("<Runner> starting", self.debug_mode)
        last_call_response = None

        for step_name, condition, step_fn in self.steps:
            DebugMode.log(f"<Runner> running {step_name}", self.debug_mode)

            if isinstance(condition, tuple):
                # Waiting for the condition (aka an element to be present at the page)
                element = WebDriverWait(self.driver, self.default_wait).until(
                    EC.presence_of_element_located(condition)
                )

            if isinstance(condition, str) and condition == "alert":
                # Waiting for the alert to be visible
                WebDriverWait(self.driver, self.default_wait).until(EC.alert_is_present())

            # simulating a delay after an element has rendered
            human_delay.delay(600, 1200) # ms
            # running the step
            last_call_response = step_fn(self.driver, last_call_response)

        return last_call_response
