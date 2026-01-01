from browser import create_page
from login import login_dio
from courses import collect_courses

def main():
    playwright, browser, context, page = create_page(headless=False)

    try:
        print("🚀 Iniciando automação")
        login_dio(page)

        courses = collect_courses(page)

        print("\n📊 Cursos encontrados:")
        for course in courses:
            print(f"- {course['name']} → {course['url']}")

    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        raise

    finally:
        print("🧹 Encerrando browser")
        context.close()
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    main()
