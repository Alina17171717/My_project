from time import sleep
from selene.support.shared import browser
from selene import have, query, command, be



def test_e2e():
    browser.open('https://book-ye.com.ua/')
    browser.element('.header-bottom__login').click()
    browser.element('#login-modal .auth-popup__bottom-link').click()
    sleep(3)
    browser.element('[name="REGISTER[NAME]"]').set_value('Alina')
    browser.element('[name="REGISTER[EMAIL]"]').set_value('alinagvrn+222@gmail.com')
    browser.element('[name="REGISTER[PERSONAL_PHONE]"]').click()
    sleep(2)
    browser.element('[name="REGISTER[PERSONAL_PHONE]"]').set_value('502222222')
    browser.element('[name="REGISTER[PASSWORD]"]').set_value('al2210')
    sleep(5)
    browser.element('#register-modal .auth-popup__submit').click()
    sleep(5)
    browser.element('.header-bottom__login-txt').should(have.text('Alina'))

    # browser.element('[name="USER_LOGIN"]').type('alinagvrn+1@gmail.com')
    # browser.element('[name="USER_PASSWORD"]').type('al2210')
    # browser.element('#login-modal .auth-popup__submit').click()
    # sleep(10)
    # if browser.all('.om-overlay .om-wheel-canvas').get(query.size) > 0:
    #     browser.element('.om-overlay .om-wheel-canvas .om-popup-close-x').click()
    # sleep(5)

    browser.element('#title-search-input').click()
    sleep(2)
    browser.element('#q').type('Project').click()
    sleep(5)
    browser.all('.multi-grid .multi-item a')[0].click()
    sleep(10)
    browser.element('.card-section .button').perform(command.js.click)
    sleep(2)
    browser.element('.checkout__name').should(have.text('Effective Communication'))

    browser.element('.modal-content__btn-secondary').click()
    browser.element('[name="ORDER_PROP_31"]').set_value('ТестПр')
    browser.element('[name="ORDER_PROP_30"]').set_value('ТестІм')
    browser.element('[name="ORDER_PROP_46"]').set_value('ТестПб')
    browser.element('[name="ORDER_PROP_2"]').set_value('alinagvrn+222@gmail.com')
    browser.element('[name="ORDER_PROP_3"]').set_value('502000000')
    browser.element('#radio13').perform(command.js.click)
    browser.element('.city-search__results').type('Львів')
    sleep(2)
    browser.all('#city_search_results li').by(have.text('Львівська обл'))[0].click()
    sleep(2)
    browser.element('.np-search__results').type('1')
    sleep(2)
    browser.all('#np_search_results li')[0].click()
    browser.all('.payment_section .button')[1].click()
    sleep(10)
    browser.element('.order-page .width-57 p').should(have.text('Дякуємо за замовлення!'))
    browser.quit()

def test_login_incorrect_password():
    browser.open('https://book-ye.com.ua/')
    browser.element('.header-bottom__login').click()
    browser.element('[name="USER_LOGIN"]').type('alinagvrn+3@gmail.com')
    browser.element('[name="USER_PASSWORD"]').type('al2213')
    browser.element('#login-modal .auth-popup__submit').click()
    sleep(2)
    element = browser.element('.submit-error')
    reference_text = 'Невірний логін або пароль.'
    element.should(be.visible)
    element.should(have.text(reference_text))
    browser.quit()

def test_empty_review_text():
    browser.open('https://book-ye.com.ua/')
    browser.element('#title-search-input').click()
    sleep(2)
    browser.element('#q').type('Python').click()
    sleep(2)
    browser.all('.multi-grid .multi-item')[0].click()
    sleep(10)
    if browser.all('.om-overlay .om-wheel-canvas').get(query.size) > 0:
        browser.element('.om-overlay .om-wheel-canvas .om-popup-close-x').click()
    sleep(5)
    browser.all('.nav-tabs li')[2].click()
    browser.element('[name="name"]').type('Alina').press_enter()
    sleep(2)
    browser.element('[name="email"]').type('alinagvrn+222@gmail.com')
    sleep(5)
    browser.element('.form__footer').click()
    element = browser.element('#text-error')
    reference_text = 'Поле має бути заповнено'
    element.should(be.visible)
    element.should(have.text(reference_text))
    browser.quit()








