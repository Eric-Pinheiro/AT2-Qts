from playwright.sync_api import Page

class PortalPage:
    def __init__(self, page: Page):
        self.page = page
        self.hostname_input = page.get_by_label("Hostname da Máquina")
        self.os_input = page.get_by_label("Versão do Sistema Operacional")
        self.submit_button = page.get_by_role("button", name="Provisionar")
        self.result_alert = page.get_by_role("alert")

    def navigate(self):
        self.page.goto("http://localhost:8000")

    def fill_form(self, hostname: str, os_version: str):
        self.hostname_input.fill(hostname)
        self.os_input.fill(os_version)