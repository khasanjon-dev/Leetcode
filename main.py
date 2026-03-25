from playwright.sync_api import sync_playwright

BASE_URL = "https://www.rimi.lv"
URL = "https://www.rimi.lv/e-veikals/en"


def get_products():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()

        page.goto(URL)

        # wait until product links appear
        page.wait_for_selector("a.card__url")

        links = page.query_selector_all("a.card__url")

        products = []

        for el in links:
            href = el.get_attribute("href")
            title = el.get_attribute("aria-label")

            if href:
                products.append({"title": title, "url": BASE_URL + href})

        return products


if __name__ == "__main__":
    data = get_products()

    for p in data[:10]:
        print(p)
