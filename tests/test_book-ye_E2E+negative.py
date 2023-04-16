from Book_ye_testing.Model import books

def test_Book_ye_E2E():
    books.open()
    books.sign_up_or_register()
    books.register()
    books.type_name('Alina')
    books.type_email('alinagvrn+72@gmail.com')
    books.type_phone('683692207')
    books.type_password('al2210')
    books.register_click()
    books.should_successful_registration('Alina')
    books.search()
    books.enter_bookname('Project')
    books.book_selection()
    books.buy_book()
    books.should_order('Project Management')
    books.to_order()
    books.order_surname('ТестПр')
    books.order_name('ТестІм')
    books.order_pb('ТестПб')
    books.order_email('alinagvrn+227@gmail.com')
    books.order_phone('979876677')
    books.select_novaposhta_delivery()
    books.delivery_city('Львів', 'Львівська обл')
    books.select_post_office('1')
    books.confirm_order()
    books.should_order_status()
    books.close()

def test_login_incorrect_password():
    books.open()
    books.sign_up_or_register()
    books.enter_login('alinagvrn+7@gmail.com')
    books.enter_password('al2213')
    books.sign_up()
    books.should_reference_text()
    books.close()

def test_empty_review_text():
    books.open()
    books.search()
    books.enter_bookname('Python')
    books.book_selection()
    books.review()
    books.review_type_name('Alina')
    books.review_type_email('alinagvrn+3@gmail.com')
    books.click_leave_a_comment()
    books.should_message_reference_text()
    books.close()




