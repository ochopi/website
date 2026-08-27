import flet as ft
from pages.card import build_card_narrow, build_card_wide

# Breakpoint: por debajo de esto se usa el layout vertical (móvil/tablet en retrato); 
# igual o por encima, el layout horizontal (pc/tablet apaisada).
WIDE_BREAKPOINT = 700

def main(page: ft.Page):
    page.title = "ochopi.com"
    page.bgcolor = "#1a0f2e"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0

    def card_page_content() -> ft.Control:
        screen_width = page.width or 380
        is_wide = screen_width >= WIDE_BREAKPOINT

        if is_wide:
            # deja margen a los lados, tope de 900px para que no se estire demasiado en monitores enormes
            card_width = min(900, screen_width - 64)
            card = build_card_wide(max_width=card_width)
        else:
            card_width = min(380, screen_width - 32)
            card = build_card_narrow(max_width=card_width)

        return ft.Container(
            content=card,
            alignment=ft.Alignment.CENTER,
            expand=True,
            padding=ft.Padding.symmetric(vertical=24, horizontal=16),
        )

    def route_change():
        page.views.clear()

        # "/" -> landing temporal (por ahora es el card; a futuro será un landing real y el card quedará solo en /card)
        page.views.append(
            ft.View(
                route="/",
                controls=[card_page_content()],
                bgcolor="#1a0f2e",
                padding=0,
                scroll=ft.ScrollMode.AUTO,
            )
        )

        # /card -> el card como página independiente
        if page.route == "/card":
            page.views.append(
                ft.View(
                    route="/card",
                    controls=[card_page_content()],
                    bgcolor="#1a0f2e",
                    padding=0,
                    scroll=ft.ScrollMode.AUTO,
                )
            )

        # Ejemplos para cuando agregues /links y /contact:
        # if page.route == "/links":
        #     page.views.append(ft.View(route="/links", controls=[...]))

        page.update()

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    def on_resize(e):
        # Recalcula ancho Y layout (narrow/wide) cuando cambia el tamaño
        # de la ventana -- esto es lo que hace el "media query" en vivo.
        route_change()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.on_resize = on_resize

    route_change()


ft.run(main, assets_dir="assets")