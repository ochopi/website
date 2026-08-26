import flet as ft


def social_icon(page: ft.Page, icon_name, url=None):
    return ft.Container(
        content=ft.Icon(icon_name, color="white", size=22),
        width=48,
        height=48,
        border_radius=24,
        border=ft.BorderRadius(1,1,1,1),
        alignment=ft.Alignment.CENTER,
        on_click=(lambda e: page.launch_url(url)) if url else None,
        ink=True,
    )


def check_item(text_str):
    return ft.Row(
        controls=[
            ft.Container(
                content=ft.Icon(ft.Icons.CHECK, color="white", size=16),
                width=24,
                height=24,
                bgcolor="#7cb342",
                border_radius=6,
                alignment=ft.Alignment.CENTER,
            ),
            ft.Text(text_str, color="white", size=18, weight=ft.FontWeight.BOLD,
                     italic=True),
        ],
        spacing=10,
    )


def build_card(page: ft.Page) -> ft.Container:
    """Construye y devuelve el Container de la tarjeta de perfil."""
    return ft.Container(
        width=380,
        padding=30,
        border_radius=28,
        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_CENTER,
            end=ft.Alignment.BOTTOM_CENTER,
            colors=["#5b2c8e", "#3d1a66"],
        ),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,
            controls=[
                ft.Container(
                    width=180,
                    height=180,
                    border_radius=90,
                    content=ft.Image(
                        src="rafael.jpg",
                        fit=ft.BoxFit.COVER,
                        border_radius=ft.BorderRadius(90, 90, 90, 90), 
                    ),
                ),

                ft.Text("RAFAEL", size=42, color="white", weight=ft.FontWeight.W_300),

                ft.Text("+503 7419 6446", size=20, color="white",
                        weight=ft.FontWeight.BOLD),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Servicios Informáticos:", color="white", size=16),
                        ft.Text("ochopi tech", color="white", size=16,
                                weight=ft.FontWeight.BOLD, italic=True),
                    ],
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=12,
                    controls=[
                        social_icon(page, ft.Icons.PHONE, "tel:+50374196446"),
                        social_icon(page, ft.Icons.MESSAGE, "https://wa.me/50374196446"),
                        social_icon(page, ft.Icons.SEND, "https://t.me/ochopitech"),
                        social_icon(page, ft.Icons.EMAIL, "mailto:rafael@ochopi.com"),
                        social_icon(page, ft.Icons.CODE, "https://github.com/ochopi"),
                        social_icon(page, ft.Icons.LANGUAGE, "https://ochopi.com"),
                    ],
                ),

                ft.Text(
                    "Trabajo con sistemas informáticos, realizando diagnóstico "
                    "y resolución de problemas de software y hardware.",
                    color="white", size=16, text_align=ft.TextAlign.CENTER,
                ),

                ft.Text(
                    "Me interesa la automatización y optimización de procesos, "
                    "así como la creación de soluciones prácticas para "
                    "problemas técnicos.",
                    color="white", size=16, text_align=ft.TextAlign.CENTER,
                ),

                ft.Column(
                    spacing=10,
                    controls=[
                        check_item("Diagnóstico"),
                        check_item("Mantenimiento"),
                        check_item("Automatización"),
                        check_item("Windows OS"),
                        check_item("Linux OS"),
                        check_item("Self-Hosting"),
                    ],
                ),
            ],
        ),
    )