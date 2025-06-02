import os
from selene import browser, have


def test_registration_form_selene():
    #Установить максимальный размер окна браузера
    browser.driver.maximize_window()
    #Открыть форму регистрации
    browser.open('https://demoqa.com/automation-practice-form')
    #Заполнить поля формы регистрации
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('alex.iv@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9050050506')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="5"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1999"]').click()
    browser.element("[aria-label='Choose Monday, June 28th, 1999']").click()
    browser.element('#subjectsInput').type('Physics').press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('Test_file.jpg'))
    browser.element('#currentAddress').type('Test Address')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    #Подтвердить регистрацию
    browser.element('#submit').click()

    #Проверить данные в таблице
    browser.element('.table-responsive').all('td').even.should(
            have.exact_texts('Alex Ivanov', 'alex.iv@gmail.com',
                             'Male','9050050506', '28 June,1999', 'Physics',
                             'Music', 'Test_file.jpg', 'Test Address', 'NCR Noida'))