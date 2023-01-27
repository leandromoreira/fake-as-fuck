import runner
import step_creator
import human_delay

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from faker import Faker

def main():
    driver = uc.Chrome()
    # driver = webdriver.Chrome()
    # driver.implicitly_wait(20) # seconds
    # driver.maximize_window()

    random_name = Faker(['en_US', 'pt_BR']).first_name()

    search_element_query, search_element_function = step_creator.create_human_field_filler(random_name + Keys.RETURN, (By.NAME, "q"))
    list_element_query, list_element_function = step_creator.create_human_fields_click(0, (By.CSS_SELECTOR, ".repo-list-item .v-align-middle"))
    
    # step_creator.create_human_field_click((By.XPATH, "//*[contains(text(), 'A full text')]"))
    steps = [
        [f"Search for {random_name}", search_element_query, search_element_function],
        ["Click on the first item", list_element_query, list_element_function],
    ]

    runner_instance = runner.Runner(driver, "https://github.com/", steps)
    runner_instance.run()

    human_delay.delay(3000, 4000) # seconds to take a printscreen
    driver.get_screenshot_as_file("page.png")

    print('\a')
    print('\a')

if __name__ == "__main__":
    main()

