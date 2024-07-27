from pathlib import Path
from selene import browser, have


def test_complete_todo():
    browser.open("/automation-practice-form")
    browser.element("#firstName").type("Julia")
    browser.element("#lastName").type("Engineer")
    browser.element("#userEmail").type("engineer@mail.ru")
    browser.element('[for="gender-radio-2"]').click()
    browser.element("#userNumber").type("8800555353")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").type("2001").click()
    browser.element(".react-datepicker__month-select").element('[value="5"]').click()
    browser.element(".react-datepicker__day--014").click()
    browser.element("#subjectsInput").type("English").click().press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f"resources/photo.png")))
    browser.element("#currentAddress").type("Engineer, 14")
    browser.element("#react-select-3-input").type("NCR").press_enter()
    browser.element("#react-select-4-input").type("Delhi").press_enter()
    browser.element("#submit").press_enter()
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
        )
    )