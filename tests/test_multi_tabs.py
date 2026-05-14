from playwright.sync_api import Page, expect
import pytest

@pytest.mark.smoke
def test_multiple_tabs(
        page: Page
):

    page.goto(
        "https://the-internet.herokuapp.com/windows"
    )

    #page.pause()

    with page.expect_popup() as popup_info:

        page.get_by_text(
            "Click Here"
        ).click()

    #page.pause()
    child_page = popup_info.value

    expect(
        child_page
    ).to_have_title(
        "New Window"
    )


    print(
        child_page.url
    )

    expect(

        child_page.get_by_text(
            "New Window"
        )

    ).to_be_visible()

    #page.pause()

    page.bring_to_front()

    expect(
        page
    ).to_have_title(
        "The Internet"
    )