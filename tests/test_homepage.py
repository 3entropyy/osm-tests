import re
from playwright.sync_api import Page, expect

def test_homepage_loads_with_map(page: Page):
    page.goto("https://www.openstreetmap.org")

    expect(page).to_have_title(re.compile("OpenStreetMap"))
    expect(page.locator("#map")).to_be_visible()