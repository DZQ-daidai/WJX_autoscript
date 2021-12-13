import random
from selenium import webdriver
import time
import schedule as schedule


# 多选题的多个选项
def int_random(m, n, o):
    p = []
    while len(p) < o:
        new_int = random.randint(m, n)
        if (new_int not in p):
            p.append(new_int)
        else:
            pass
    return p


count = 0


def sum1():
    global count
    count += 1
    w = print("第{}次运行".format(count))
    return w


def generate_choice(choice_list, probabilities_list):
    if not (0.99999 < sum(probabilities_list) < 1.00001):
        raise ValueError("The probabilities are not normalized!")
    if len(choice_list) != len(probabilities_list):
        raise ValueError("The length of two input lists are not match!")
    random_normalized_num = random.random()  # random() -> x in the interval [0, 1).
    accumulated_probability = 0.0
    for item in zip(choice_list, probabilities_list):
        accumulated_probability += item[1]
        if random_normalized_num < accumulated_probability:
            return item[0]


def run():
    # 问卷
    url = 'https://www.wjx.cn/vm/xxxxxxxxxx.aspx'
    # 躲避智能检测
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=option)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
                            })
    driver.get(url)
    # 总共有22个题目
    i = 1
    while i <= 22:
        base_xpath1 = '//*[@id="div{}"]'.format(i)
        base_xpath2 = base_xpath1 + '/div[2]/div'
        a = driver.find_elements_by_xpath(base_xpath2)
        # print(len(a))
        # 在选项个数范围内，随机生成一个数字 如有四个选项，随机生成数字3
        # b = random.randint(1, len(a))
        # 自定义选择概率
        if i == 1:
            b = generate_choice([1, 2], [0.5, 0.5])
        elif i == 2:
            b = generate_choice([1, 2, 3, 4, 5], [0.4, 0.3, 0.2, 0.1, 0])
        elif i == 3:
            b = generate_choice([1, 2, 3, 4], [0.5, 0.3, 0.15, 0.05])
        elif i == 4:
            b = generate_choice([1, 2, 3, 4, 5], [0.5, 0.3, 0.15, 0.05, 0])
        elif i == 5:
            b = generate_choice([1, 2, 3, 4, 5], [0, 0.3, 0.4, 0.1, 0.2])
        elif i == 6:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.3, 0.05, 0.35, 0.2])
        elif i == 7:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 8:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 9:
            b = generate_choice([1, 2, 3, 4, 5], [0.5, 0.3, 0.05, 0.15, 0])
        elif i == 10:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 11:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 12:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 13:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 14:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 15:
            b = generate_choice([1, 2, 3, 4, 5], [0.3, 0.3, 0.05, 0.35, 0])
        elif i == 16:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 17:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 18:
            b = generate_choice([1, 2, 3, 4, 5], [0.3, 0.3, 0.05, 0.35, 0])
        elif i == 18:
            b = generate_choice([1, 2, 3, 4, 5], [0.3, 0.3, 0.05, 0.35, 0])
        elif i == 19:
            b = generate_choice([1, 2, 3, 4, 5], [0.3, 0.3, 0.05, 0.35, 0])
        elif i == 20:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])
        elif i == 21:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.3, 0.05, 0.4, 0.15])
        elif i == 22:
            b = generate_choice([1, 2, 3, 4, 5], [0.1, 0.15, 0.05, 0.4, 0.3])

        time.sleep(0.1)
        driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, b)).click()
        i += 1
    # input()
    # 点击提交按钮
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
    # 出现点击验证码验证
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="alert_box"]/div[2]/div[2]/button').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="rectMask"]').click()
    time.sleep(4)

    # 关闭页面
    handles = driver.window_handles
    driver.switch_to.window(handles[0])
    time.sleep(0.5)
    # 刷新页面（可能不需要）
    driver.refresh()
    # 关闭当前页面，如果只有一个页面，则也关闭浏览器
    driver.close()
    # 计数器
    sum1()


schedule.every(1).seconds.do(run)

while True:
    schedule.run_pending()
