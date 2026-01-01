from playwright.sync_api import Page

PLAY_URL = "https://web.dio.me/play"

def collect_courses(page: Page):
    print("📚 Indo para página de cursos...")
    page.goto(PLAY_URL)

    page.wait_for_selector("li.sc-fJmHDK.gAFmrX", timeout=30000)

    courses = []

    all_cards = page.locator("li.sc-fJmHDK.gAFmrX")
    
    fourth_section_cards = all_cards.nth(3).locator("..").locator("li.sc-fJmHDK.gAFmrX")

    total_cards = fourth_section_cards.count()
    print(f"🟢 Encontrados {total_cards} cursos na 4ª seção")

    for i in range(total_cards):
        card = fourth_section_cards.nth(i)
        try:
            card.click()
            page.wait_for_selector("h2 span", timeout=30000)

            course_name = page.locator("h2 span").first.inner_text().strip()
            course_url = page.url

            resources = []
            inner_items = page.locator("ul.sc-jwGauN.dJbGaK > li.sc-iPyqbM.hprRax")
            for j in range(inner_items.count()):
                item = inner_items.nth(j)
                img = item.locator("img")
                if img.count() > 0:
                    resources.append(img.first.get_attribute("src"))
                else:
                    svg = item.locator("svg")
                    if svg.count() > 0:
                        resources.append("SVG encontrado")

            courses.append({
                "name": course_name,
                "url": course_url,
                "resources": resources
            })

            print(f"   📘 {course_name} coletado!")

            page.goto(PLAY_URL)
            page.wait_for_selector("li.sc-fJmHDK.gAFmrX", timeout=30000)

        except Exception as e:
            print(f"   ⚠️ Erro ao coletar curso {i + 1}: {e}")

    print("✅ Todos os cursos da 4ª seção coletados!")

    return courses
