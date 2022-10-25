import human_delay

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

def create_human_field_filler(value, query_tuple):
    def human_filler(driver, last_call_response=None):
        input_element = driver.find_element(query_tuple[0], query_tuple[1])
        input_element.click()
        input_element.clear()

        for chr in value:
            human_delay.average_people_typing()
            input_element.send_keys(chr)

        return last_call_response
    return query_tuple, human_filler

def create_human_field_click(query_tuple):
    def human_click(driver, last_call_response=None):
        input_element = driver.find_element(query_tuple[0], query_tuple[1])
        human_delay.average_people_waiting_for_click()
        input_element.click()
        return last_call_response

    return query_tuple, human_click

def create_human_fields_click(index, query_tuple):
    def human_click(driver, last_call_response=None):
        input_elements = driver.find_elements(query_tuple[0], query_tuple[1])
        human_delay.average_people_waiting_for_click()
        input_elements[index].click()
        return last_call_response

    return query_tuple, human_click

def create_human_select_by_visible_text(text, query_tuple):
    def select_by_visible_text(driver, last_call_response=None):
        select = Select(driver.find_element(query_tuple[0], query_tuple[1]))
        human_delay.average_people_waiting_for_click()
        select.select_by_visible_text(text)
        return last_call_response

    return query_tuple, select_by_visible_text

def create_human_accept_alert(query_tuple):
    def accept_alert(driver, last_call_response=None):
        Alert(driver).accept()
        return last_call_response

    return query_tuple, accept_alert
