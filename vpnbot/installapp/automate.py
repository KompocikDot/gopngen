from pywinauto.application import Application
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


class AutomateBot:
    def __init__(self, download_url: str) -> None:
        self.playwright = sync_playwright().start()
        self.chromium = self.playwright.chromium
        self.download_url = download_url
        self.browser = None
        self.filename = None

    def __del__(self):
        self.playwright.stop()

    def install_vpn(self) -> None:
        pass

    def run_vpn(self) -> None:
        pass

    def download_vpn(self) -> None:
        self.browser = self.chromium.launch()
        page = self.browser.new_page()
        stealth_sync(page)
        page.goto(self.download_url)

        with page.expect_download() as download:
            page.locator("css=[href^=#elementor-action*]").click()
            self.filename = download.value
            if err := download.failure():
                raise err
