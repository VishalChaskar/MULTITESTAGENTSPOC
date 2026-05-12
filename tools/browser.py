from playwright.sync_api import sync_playwright

def collect_page_data(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        data = {
            "url": url,
            "title": page.title(),
            "html": page.content(),
            "links": page.eval_on_selector_all(
                "a", "els => els.map(e => e.href)"
            ),
            "buttons": page.eval_on_selector_all(
                "button", "els => els.map(e => e.innerText)"
            ),
            "text": page.inner_text("body")[:3000]  # limit size
        }

        browser.close()
        return data