import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture
def output_subdir(request):
    path_arg = request.config.getoption("--output-subdir")
    return './output/' + path_arg + '/' if path_arg != '' else './output/'

def save_snapshot(page, name, setup_data):
    page.screenshot(path= setup_data +  name + '.png')


def test_login(page:Page, output_subdir):
    #launch browserstack demo
    page.goto("https://bstackdemo.com/")
    #click on sign button
    page.click('#signin')
    #select Username
    page.get_by_text("Select Username").click()
    page.locator("#react-select-2-option-0-0").click()
    #select Password
    page.get_by_text("Select Password").click()
    page.locator("#react-select-3-option-0-0").click()
    #click login
    page.get_by_role("button", name="Log In").click()
    #verify user have logged in
    assert page.get_by_text("demouser").is_visible()
    save_snapshot(page, 'username', output_subdir)

def test_example(page: Page, output_subdir) -> None:
    page.goto("https://www.amazon.co.uk/")
    save_snapshot(page, 'amazon', output_subdir)
