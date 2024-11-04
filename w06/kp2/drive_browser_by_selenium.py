#!/usr/bin/env python3

USAGE = '''[USAGE] ./command.sh fn
  fn:'''
methods = [(1, 'get_quotes'),
           (2, 'gather_quotes_pressing_the_page_down_key_10_times'),
           (3, 'gather_quotes_scrolling_a_page'),
           (4, 'entry_data_with_step_by_step_input'),
           (5, 'entry_data_with_action_chain_input')]
for i, method in methods: USAGE += f"\n    {i}: {method}"

import os, sys, time
from pathlib import Path

def my_webdriver(url, headless=False):
    from selenium import webdriver
    opt = webdriver.ChromeOptions()
    if headless:
        opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=opt)
    if not headless:
        driver.set_window_size(640, 800)
        driver.set_window_position(0, 0)
    driver.implicitly_wait(10)
    driver.get(url)
    return driver

def get_quotes():
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
    driver = my_webdriver(url)

    quote_elements = WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.quote')))
    
    ret = []
    for quote in quote_elements:
        ret.append(quote.text)
    time.sleep(3)
    return ret

def press_the_page_down_key_10_times(driver, div_element):
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    # アクション（チェーン）の使用を開始
    action_chain = ActionChains(driver)
    # 名言のブロックに移動
    action_chain.move_to_element(div_element)
    # クリックして操作対象にする
    action_chain.click()
    # Page Downキーを10回押す
    action_chain.send_keys([Keys.PAGE_DOWN for i in range(10)])
    # 以上のアクションを実行する
    action_chain.perform()

def scroll_a_page(driver, div_element):
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollHeight', div_element)

class at_least_n_elements_found(object):
    def __init__(self, locator, n):
        self.locator = locator
        self.n = n

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) >= self.n:
            return elements
        else:
            return False

def gather_quotes(scroll_to_the_bottom):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.common.exceptions import TimeoutException
    url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
    driver = my_webdriver(url)

    div_element = driver.find_element(By.CLASS_NAME, 'infinite-scroll')
    quotes_locator = (By.CSS_SELECTOR, ".quote")
    nr_quotes = 0
    while True:
        # 一番下までスクロールする
        scroll_to_the_bottom(driver, div_element)
        # 少なくともnr_quotes + 1個の名言を取得しようとする
        try:
            all_quotes = WebDriverWait(driver, 3).until(
                at_least_n_elements_found(quotes_locator, nr_quotes + 1))
        except TimeoutException:
            # 3秒以内に新しい名言が見つからなければ取得をやめる
            print('... done!')
            break
        #それ以外の場合は，名言のカウンターを更新する
        nr_quotes = len(all_quotes)
        print('... now seeing', nr_quotes, 'quotes')

    # 名言の数を表示する
    print(len(all_quotes), 'quotes found')

    ret = []
    for quote in all_quotes:
        ret.append(quote.text)
    time.sleep(3)
    return ret

def step_by_step_input(driver):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    driver.find_element(By.NAME, 'name').send_keys('a')
    driver.find_element(By.CSS_SELECTOR, 'input[name="gender"][value="F"]').click()
    driver.find_element(By.NAME, 'pizza').click()
    driver.find_element(By.NAME, 'comments').send_keys(
        ['b', Keys.ENTER])

def action_chain_input(driver):
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    chain = ActionChains(driver)
    chain.send_keys_to_element(driver.find_element(By.NAME, 'name'), 'a')
    chain.click(driver.find_element(By.CSS_SELECTOR, 'input[name="gender"][value="F"]'))
    chain.click(driver.find_element(By.NAME, 'pizza'))
    chain.click(driver.find_element(By.NAME, 'comments'))
    chain.send_keys('b', Keys.ENTER)
    chain.perform()

def entry_data(input_form):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.select import Select
    url = 'http://www.webscrapingfordatascience.com/postform2/'
    driver = my_webdriver(url)

    time.sleep(3)
    input_form(driver)
    Select(driver.find_element(By.NAME, 'haircolor')).select_by_value('brown')
    time.sleep(3)
    driver.find_element(By.TAG_NAME, 'form').submit()
    #またはdriver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    return driver.page_source

def switch_func(fn):
    if fn == 1:
        return get_quotes()
    elif fn == 2:
        return gather_quotes(press_the_page_down_key_10_times)
    elif fn == 3:
        return gather_quotes(scroll_a_page)
    elif fn == 4:
        return entry_data(step_by_step_input)
    elif fn == 5:
        return entry_data(action_chain_input)
    
def main(fn):
    path_log = Path('output/output.txt')
    os.makedirs(path_log.parent)
    with open(path_log, 'w') as f:
        ret = switch_func(fn)
        if type(ret) is str:
            f.write(ret)
        elif type(ret) is list:
            for r in ret:
                f.write(str(r) + '\n')
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        fn = int(sys.argv[1])
        if fn in [fn for fn, method in methods]:
            main(fn)
        else:
            print(USAGE)
    else:        
        print(USAGE)
