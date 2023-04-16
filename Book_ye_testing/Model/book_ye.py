from time import sleep
from selene import have, query, command, be
from selene.support.shared import browser


class Books:
    def open(self):
        browser.open('https://book-ye.com.ua/')
        return self

    def sign_up_or_register(self):
        browser.element('.header-bottom__login').click()
        return self

    def register(self):
        browser.element('#login-modal .auth-popup__bottom-link').click()
        return self

    def type_name(self, name: str):
        browser.element('[name="REGISTER[NAME]"]').set_value(name)
        return self

    def type_email(self, email: str):
        browser.element('[name="REGISTER[EMAIL]"]').set_value(email)
        return self

    def type_phone(self, number: str):
        browser.element('[name="REGISTER[PERSONAL_PHONE]"]').click()
        sleep(2)
        browser.element('[name="REGISTER[PERSONAL_PHONE]"]').type(number)
        sleep(2)
        return self

    def type_password(self, password: str):
        browser.element('[name="REGISTER[PASSWORD]"]').set_value(password)
        return self

    def register_click(self):
        browser.element('#register-modal .auth-popup__submit').click()
        sleep(25)
        if browser.all('.om-overlay .om-wheel-canvas').get(query.size) > 0:
            browser.element('.om-overlay .om-wheel-canvas .om-popup-close-x').click()
        sleep(5)
        return self

    def should_successful_registration(self, name: str):
        browser.element('.header-bottom__login-txt').should(have.text(name))
        return self

    def search(self):
        browser.element('#title-search-input').click()
        sleep(2)
        return self

    def enter_bookname(self, bookname: str):
        browser.element('#q').type(bookname).click()
        sleep(5)
        return self

    def book_selection(self):
        browser.all('.multi-grid .multi-item a')[0].click()
        return self

    def buy_book(self):
        sleep(5)
        browser.element('.card-section .button').perform(command.js.click)
        sleep(10)
        return self

    def should_order(self, bookname: str):
        browser.element('.checkout__name').should(have.text(bookname))
        return self

    def to_order(self):
        browser.element('.modal-content__btn-secondary').click()
        return self

    def order_surname(self, r_surname: str):
        browser.element('[name="ORDER_PROP_31"]').set_value(r_surname)
        return self

    def order_name(self, r_name: str):
        browser.element('[name="ORDER_PROP_30"]').set_value(r_name)
        return self

    def order_pb(self, r_pb: str):
        browser.element('[name="ORDER_PROP_46"]').set_value(r_pb)
        return self

    def order_email(self, r_email: str):
        browser.element('[name="ORDER_PROP_2"]').set_value(r_email)
        return self

    def order_phone(self, r_number: str):
        browser.element('[name="ORDER_PROP_3"]').set_value(r_number)
        return self

    def select_novaposhta_delivery(self):
        browser.element('#radio13').perform(command.js.click)
        return self

    def delivery_city(self, city: str, region: str):
        browser.element('.city-search__results').type(city)
        sleep(2)
        browser.all('#city_search_results li').by(have.text(region))[0].click()
        sleep(2)
        return self

    def select_post_office(self, post: str):
        browser.element('.np-search__results').type(post)
        sleep(2)
        browser.all('#np_search_results li')[0].click()
        return self

    def confirm_order(self):
        browser.all('.payment_section .button')[1].click()
        sleep(10)
        return self

    def should_order_status(self):
        browser.element('.order-page .width-57 p').should(have.text('Дякуємо за замовлення!'))
        return self

    def close(self):
        browser.quit()
        return self

    def enter_login(self, login: str):
        browser.element('[name="USER_LOGIN"]').type(login)
        return self

    def enter_password(self, inc_pw: str):
        browser.element('[name="USER_PASSWORD"]').type(inc_pw)
        return self

    def sign_up(self):
        browser.element('#login-modal .auth-popup__submit').click()
        sleep(2)
        return self

    def should_reference_text(self):
        element = browser.element('.submit-error')
        reference_text = 'Невірний логін або пароль.'
        element.should(be.visible)
        element.should(have.text(reference_text))
        return self

    def review(self):
        sleep(10)
        if browser.all('.om-overlay .om-wheel-canvas').get(query.size) > 0:
            browser.element('.om-overlay .om-wheel-canvas .om-popup-close-x').click()
        sleep(5)
        browser.all('.nav-tabs li')[2].click()
        return self

    def review_type_name(self, us_name: str):
        browser.element('[name="name"]').type(us_name).press_enter()
        return self

    def review_type_email(self, us_email: str):
        browser.element('[name="email"]').type(us_email)
        sleep(5)
        return self

    def click_leave_a_comment(self):
        browser.element('.form__footer').click()
        return self

    def should_message_reference_text(self):
        element = browser.element('#text-error')
        reference_text = 'Поле має бути заповнено'
        element.should(be.visible)
        element.should(have.text(reference_text))


























