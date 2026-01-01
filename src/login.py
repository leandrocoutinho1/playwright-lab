import os
from playwright.sync_api import Page
from dotenv import load_dotenv

load_dotenv()

DIO_LOGIN_URL = os.getenv("DIO_LOGIN_URL")
DIO_HOME_URL = "https://web.dio.me/home"

def login_dio(page: Page):
    email = os.getenv("EMAIL")
    senha = os.getenv("SENHA")

    if not email or not senha:
        raise Exception("EMAIL ou SENHA não definidos no .env")

    print("🔐 Navegando para login da DIO...")
    page.goto(DIO_LOGIN_URL)

    page.wait_for_selector('input[name="username"]', timeout=15000)

    page.fill('input[name="username"]', email)
    page.fill('input[name="password"]', senha)

    page.click('button[type="submit"]')

    page.wait_for_selector(
        'img[title]',
        timeout=20000
    )

    print("✅ Login realizado com sucesso")
