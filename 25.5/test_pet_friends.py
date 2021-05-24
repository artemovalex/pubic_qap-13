import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_from_base_page():
    pytest.driver.get("https://petfriends1.herokuapp.com/")

    # click on the new user button
    btn_newuser = pytest.driver.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = pytest.driver.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = pytest.driver.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("test2test@mail.ru")

    # add password
    field_pass = pytest.driver.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("123456789Zz")

    # click submit button
    btn_submit = pytest.driver.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    assert pytest.driver.current_url == 'https://petfriends1.herokuapp.com/all_pets', "login error"


def test_all_pets():
    # Open PetFriends login page:
    pytest.driver.get("http://petfriends1.herokuapp.com/login")

    # Entering valid email
    pytest.driver.find_element_by_id('email').send_keys('test2test@mail.ru')
    # Entering valid password
    pytest.driver.find_element_by_id('pass').send_keys('123456789Zz')
    # Click "Enter" button
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # Check getting on valid (after-auth) page
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_my_pets():
    # Open PetFriends login page:
    pytest.driver.get("http://petfriends1.herokuapp.com/login")

    # Entering valid email
    pytest.driver.find_element_by_id('email').send_keys('test2test@mail.ru')
    # Entering valid password
    pytest.driver.find_element_by_id('pass').send_keys('123456789Zz')
    # Click "Enter" button
    # pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # Check getting on valid (after-auth) page
    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

    pytest.driver.find_element_by_xpath('//a[contains(text(),"Мои питомцы")]').click()
    amount = pytest.driver.find_element_by_xpath("//*[h2][1]").text.split()[2]

    assert type(amount) == str
    assert amount != ''

    images = pytest.driver.find_elements_by_xpath('//img')
    names_elems = pytest.driver.find_elements_by_xpath('//td[1]')
    types = pytest.driver.find_elements_by_xpath('//td[2]')
    ages = pytest.driver.find_elements_by_xpath('//td[3]')

    names = []
    for i in range(len(names_elems)):
        names.append(names_elems[i].text)

    assert len(names) == int(amount)

    cnt_img = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            cnt_img += 1
    assert cnt_img >= int(amount) / 2

    assert len(names) == len(list(set(names)))

    for i in range(len(names_elems)):
        assert names_elems[i].text != ''
        assert types[i].text != ''
        assert ages[i].text != ''