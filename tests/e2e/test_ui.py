import pytest
from axe_playwright_python.sync_playwright import Axe
from tests.e2e.pages.portal_page import PortalPage
from playwright.sync_api import expect

# @pytest.fixture(scope="module", autouse=True)
# def run_server():
#     import subprocess
#     import time
#     process = subprocess.Popen(
#         ["uv", "run", "uvicorn", "src.main:app", "--port", "8000"],
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE
#     )
#     time.sleep(2) # Aguarda o servidor subir
#     if process.poll() is not None:
#         out, err = process.communicate()
#         raise RuntimeError(f"Falha ao iniciar Uvicorn:\nErro: {err.decode('utf-8', errors='ignore')}")
#     yield
#     process.terminate()

@pytest.mark.e2e
def test_keyboard_navigation(page):
    portal = PortalPage(page)
    portal.navigate()
    
    # Valida foco via teclado (Tab)
    page.keyboard.press("Tab")
    expect(portal.hostname_input).to_be_focused()
    
    page.keyboard.press("Tab")
    expect(portal.os_input).to_be_focused()
    
    page.keyboard.press("Tab")
    expect(portal.submit_button).to_be_focused()

@pytest.mark.accessibility
def test_accessibility_wcag(page):
    portal = PortalPage(page)
    portal.navigate()
    
    axe = Axe()
    results = axe.run(page)
    
    # Falha o teste se houver violações críticas ou sérias de acessibilidade
    assert results.violations_count == 0, f"Violações de acessibilidade:\n{results.generate_report()}"