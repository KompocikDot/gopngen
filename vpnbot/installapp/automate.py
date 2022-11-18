import os
import time

import pyautogui
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

pyautogui.FAILSAFE = False


class AutomateBot:
    def __init__(self, download_url: str) -> None:
        self.playwright = sync_playwright().start()
        self.chromium = self.playwright.chromium
        self.download_url = download_url
        self.browser = None
        self.filename = None

        self.download_vpn()
        self.close()
        self.install_and_run_vpn()

    def close(self):
        self.playwright.stop()

    def download_vpn(self) -> None:
        self.browser = self.chromium.launch(headless=False)
        page = self.browser.new_page()
        stealth_sync(page)
        page.goto(self.download_url, wait_until="domcontentloaded")

        with page.expect_download() as download:
            page.wait_for_selector('a[href^="#elementor-"]').click()
            download.value.save_as(download.value.suggested_filename)
            self.filename = download.value.suggested_filename

    def install_and_run_vpn(self) -> None:
        os.popen(f'cmd.exe /c "set __COMPAT_LAYER=RunAsInvoker && {self.filename}"')
        time.sleep(10)
        for _ in range(7):
            pyautogui.press("tab")
        pyautogui.press("enter")

        print("installing...")
        while True:
            app_installing = pyautogui.locateOnScreen("./install_text.png")
            if app_installing:
                print("waiting 10 seconds for an app to install")
                time.sleep(10)
                continue
            break

        print("waiting for an app to become visible")
        while True:
            app_turned_on = pyautogui.locateOnScreen("./installed_app.png")
            if not app_turned_on:
                print("waiting 10 seconds for an app to become visible")
                time.sleep(10)
                continue
            break

        print("Turning on a VPN")
        x, y = pyautogui.locateCenterOnScreen("./turn_on_btn.png", confidence=0.9)
        pyautogui.click(x, y)

        # send request to some kind of an API to know what's happening
