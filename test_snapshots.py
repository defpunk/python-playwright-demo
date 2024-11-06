import pytest
from playwright.sync_api import Page, expect


@pytest.mark.regression
def test_snapshot(page, assert_snapshot):
    page.goto('https://bbc.co.uk');
    assert_snapshot(page.screenshot())
