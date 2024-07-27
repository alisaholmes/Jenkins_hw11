from pathlib import Path
from selene import browser, have
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "alisaholmes")
@allure.feature("Регистрация")
@allure.story("Проверка заполнения формы регистрации")

def test_complete_todo():
    with allure.step("Открыть форму"):
        browser.open("/automation-practice-form")
    with allure.step("Заполнить поле имени"):
        browser.element("#firstName").type("Julia")
    with allure.step("Заполнить поле фамилии"):
        browser.element("#lastName").type("Engineer")
    with allure.step("Заполнить поле email"):
        browser.element("#userEmail").type("engineer@mail.ru")
    with allure.step("Указать свой гендер"):
        browser.element('[for="gender-radio-2"]').click()
    with allure.step("Заполнить поле номера телефона"):
        browser.element("#userNumber").type("8800555353")
    with allure.step("Заполнить поле даты рождения"):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type("2001").click()
        browser.element(".react-datepicker__month-select").element('[value="5"]').click()
        browser.element(".react-datepicker__day--014").click()
    with allure.step("Заполнить поле темы"):
        browser.element("#subjectsInput").type("English").click().press_enter()
    with allure.step("Выбрать хобби"):
        browser.element('[for="hobbies-checkbox-2"]').click()
    with allure.step("Загрузить фото"):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f"resources/photo.png")))
    with allure.step("Заполнить поле адреса"):
        browser.element("#currentAddress").type("Engineer, 14")
    with allure.step("Указать страну и город"):
        browser.element("#react-select-3-input").type("NCR").press_enter()
        browser.element("#react-select-4-input").type("Delhi").press_enter()
        browser.element("#submit").press_enter()
    with allure.step("Проверить форму"):
        browser.element("#example-modal-sizes-title-lg").should(
        have.text("Thanks for submitting the form")
        )
        browser.element('.table').all('td').even.should(have.exact_texts("Julia Engineer",
            "engineer@mail.ru",
            "Female",
            "8800555353",
            "14 June,2001",
            "English",
            "Reading",
            "photo.png",
            "Engineer, 14",
            "NCR Delhi",
        ))