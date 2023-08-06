import os
import re
import time

from datetime import date
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import chromedriver_binary


def get_all_list_pages(cplmanager):
    """
    This function:
    - `cplmanager`: an instance of `CPLSeleniumManager`
    - Clicks through creepypasta.com's archive of stories using Selenium
    - Saves each list of stories (urls) to disk, default `list-pages/`
    """

    # run for page 1
    CPLSeleniumPageNav.save_current_page(cplmanager.driver, cplmanager.list_pages_dir)

    # do the looping now
    while True:
        time.sleep(2)
        if not CPLSeleniumPageNav.go_to_next_page(cplmanager.driver):
            break
        # todo: do a smarter wait, lol
        time.sleep(2)
        CPLSeleniumPageNav.save_current_page(cplmanager.driver, cplmanager.list_pages_dir)


def open_browser(headless=False):
    """
    Opens a new automated browser window with all tell-tales of automated browser disabled
    """
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    if headless:
        options.add_argument("--headless")
    
    # remove all signs of this being an automated browser
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # open the browser with the new options
    driver = webdriver.Chrome(options=options)
    return driver


class CPLSeleniumManager:
    """
    Object to hold/access Selenium webdriver instance and 
    set up destination directories for scraper.
    """
    def __init__(self):
        """
        - Calls `setup_fetch_dirs(self)` to create directories for 
          story-lists, stories, and test files if they don't yet exist
        - Opens a new browser and returns webdriver instance
        - Loads creepypasta archive using Selenium
        """
        self.setup_fetch_dirs()
        # visit the page
        url = 'https://www.creepypasta.com/archive/?_orderby=date'
        self.driver = self.open_driver()
        self.driver.get(url)

    def open_driver(self):
        """
        - Called during `__init__`, but can also be executed on its own 
          to reset the browser
        - Closes last open driver if needed
        - Opens a new browser
        """
        # open driver
        try:
            driver.close()
        except:
            print("no webdrivers open")
        finally:
            driver = open_browser()
        return driver

    def setup_fetch_dirs(self):
        """
        - Creates directories for `page_source`.
        - This is where all files will be saved.
        """
        # create dirs for page_source
        # this is where all files will be saved
        self.list_pages_dir = "list-pages/"
        os.makedirs(self.list_pages_dir, exist_ok=True)
        self.story_pages_dir = "story-pages/"
        os.makedirs(self.story_pages_dir, exist_ok=True)
        self.test_dir = "test/"
        os.makedirs(self.test_dir, exist_ok=True)
    
    def close_popups(self):
        """        
        - Closes all popups that are visible on the page
        - Runs twice, to handle ads with delayed loading
        - Uses `CPLSeleniumAdHandler`'s methods
        """
        for i in range(2):
            CPLSeleniumAdHandler.close_first_popups(self.driver)
            CPLSeleniumAdHandler.close_some_ads(self.driver)
            time.sleep(2)


class CPLSeleniumAdHandler:    
    @classmethod
    # TODO: handle accept/reject popup
    def close_first_popups(cls, driver):
        """
        - `driver`: webdriver instance
        -  Closes popups that first appear as creepypasta page is loading
        """
        # todo: wait until load
        try:
            signup_updates_popup_element = driver.find_element(
                By.XPATH,
                '//*[@id="onesignal-slidedown-cancel-button"]'
            )
            signup_updates_popup_element.click()
        except:
            print("no signup popup element on page")
    
    @classmethod
    def close_some_ads(cls, driver):
        """
        - `driver`: webdriver instance
        - Closes more ads that render on the page after initial load
        - May want to run this on its own again for more delayed ads
        """
        try:
            pg_top_ad_element_to_close = driver.find_element(
                By.XPATH,
                '//*[@id="pw-close-btn"]'
            )
            pg_top_ad_element_to_close.click()
        except:
            print("no pg top ad element on page")

        try:
            pg_btm_ad_element_to_close = driver.find_element(
                By.XPATH,
                '//*[@id="pw-oop-bottom_rail"]/div[2]'
            )
            pg_btm_ad_element_to_close.click()
        except:
            print("no pg btm ad element on page")

        try:
            pg_btm_ad_element_to_close_2 = driver.find_element(
                By.XPATH,
                '//*[@id="pw-oop-bottom_rail2"]/div[2]'
            )
            pg_btm_ad_element_to_close_2.click()
        except:
            print("no pg btm ad 2 element on page")


class CPLSeleniumPageNav:
    """
    Container for functions that navigate and save individual pages.
    """
    @classmethod
    def go_to_next_page(cls, driver):
        """
        - `driver`: webdriver instance
        - Navigates to next page
        - In a loop, stops advancing pages on final page
        """
        try:
            next_page_element = driver.find_element(
                By.XPATH,
                '//*[@id="post-40339"]/div/div[1]/div[4]/ul/li[8]/a'
            )
        except:
            # retry once in case element has not yet loaded
            # TODO: swap to implicit wait
            next_page_element = driver.find_element(
                By.XPATH,
                '//*[@id="post-40339"]/div/div[1]/div[4]/ul/li[8]/a'
            )
        # need to scroll down to click
        # otherwise action will be caught by iframe/ads
        scroll_into_view_js = 'document.querySelector("#post-40339 > div > div.pt-cv-wrapper > div.text-left.pt-cv-pagination-wrapper > ul > li.cv-pageitem-next > a").scrollIntoView();'
        driver.execute_script(scroll_into_view_js, next_page_element)
        driver.execute_script("window.scrollBy(0, -50);")

        # checking to see if clicking does anything, or if button is already "active"
        # todo: refactor to exclude already "active" (red) elements earlier?
        current_url = driver.current_url # before click
        print(current_url)
        next_page_element.click()
        print(driver.current_url)

        # if the "clicked" page is new, then return True
        # this will tell the calling function to use the results
        # and continue looping
        return (current_url != driver.current_url)
    
    @classmethod
    def reset_to_first_page(cls, driver):
        """
        - `driver`: webdriver instance
        - Navigates back to first page
        """
        try:
            next_page_element = driver.find_element(
                By.XPATH,
                '//*[@id="post-40339"]/div/div[1]/div[4]/ul/li[8]/a'
            )
        except:
            # retry once in case element has not yet loaded
            # TODO: swap to implicit wait
            next_page_element = driver.find_element(
                By.XPATH,
                '//*[@id="post-40339"]/div/div[1]/div[4]/ul/li[8]/a'
            )
        scroll_into_view_js = 'document.querySelector("#post-40339 > div > div.pt-cv-wrapper > div.text-left.pt-cv-pagination-wrapper > ul > li.cv-pageitem-next > a").scrollIntoView();'
        driver.execute_script(scroll_into_view_js, next_page_element)
        driver.execute_script("window.scrollBy(0, -50);")
        first_page_carrots = driver.find_element(
            By.XPATH,
            '//*[@id="post-40339"]/div/div[1]/div[4]/ul/li[1]/a'
        )
        first_page_carrots.click()
    
    @classmethod
    def save_current_page(cls, driver, dest_dir):
        """
        - `driver`: webdriver instance
        - `dest_dir`: directory files are saved to
        - Saves `driver.page_source` for rendered page
        - Default saves to `./list-pages/`, `./story-pages/`, `./test/`
        """
        dest = f"{dest_dir}{date.today()}_{driver.current_url.split('?')[-1]}.html"
        print(dest)
        source = driver.page_source
        with open(dest, 'w') as f:
            f.write(source)


if __name__ == "__main__":
    # executing this file as is will get all list pages
    # and save to `./list-pages/`
    cplm = CPLSeleniumManager()
    cplm.close_popups()
    get_all_list_pages(cplm)
