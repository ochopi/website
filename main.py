import flet as ft
from pages.card import build_card


def main(page: ft.Page):
    page.title = "ochopi.com"
    page.bgcolor = "#1a0f2e"
    # Sin esto, el contenido que no cabe en la pantalla del celular
    # simplemente se recorta y no se puede hacer scroll.
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0

    def card_page_content() -> ft.Control:
        """Ancho del card limitado al ancho de pantalla disponible (con margen),
        para que no se corte ni fuerce scroll horizontal en móvil."""
        max_width = min(380, (page.width or 380) - 32)
        return ft.Container(
            content=build_card(max_width=max_width),
            alignment=ft.Alignment.CENTER,
            expand=True,
            padding=ft.Padding.symmetric(vertical=24, horizontal=16),
        )

    def route_change():
        page.views.clear()

        # "/" -> landing temporal (por ahora es el card; a futuro será
        # un landing real y el card quedará solo en /card)
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
        # Recalcula el ancho del card cuando cambia el tamaño de ventana
        route_change()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.on_resize = on_resize

    # Construye las vistas para la ruta con la que se cargó la página,
    # sin necesitar page.go() (deprecado).
    route_change()


ft.run(main, assets_dir="assets")