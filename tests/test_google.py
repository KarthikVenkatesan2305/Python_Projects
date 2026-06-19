from playwright.sync_api import Page,expect

def test_verify_url(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page).to_have_url("https://demowebshop.tricentis.com/")

def test_verify_title(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page).to_have_title("Demo Web Shop")
    print(page.title().strip())
   