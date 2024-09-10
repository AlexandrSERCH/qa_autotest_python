import os
import time

from selenium.webdriver import Keys

from generator.generator import genetared_person, generate_file
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        person = genetared_person()
        path = generate_file()
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)
        time.sleep(0.5) # было добавлено специально, чтобы был виден на видео
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        time.sleep(0.5)
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        time.sleep(0.5)
        self.element_is_visible(Locators.GENDER).click()
        time.sleep(0.5)
        self.element_is_visible(Locators.MOBILE).send_keys(person.mobile)
        time.sleep(0.5)
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        time.sleep(0.5)
        self.element_is_visible(Locators.HOBBIES).click()
        time.sleep(0.5)
        self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
        time.sleep(0.5)
        os.remove(path)
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(person.current_address)
        time.sleep(0.5)
        self.element_is_visible(Locators.SUBMIT).click()
        time.sleep(0.5)
        return person

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = []
        for i in result_list:
            result_text.append(i.text)
        return result_text





