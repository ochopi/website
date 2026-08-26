import flet as ft


def social_icon(icon_name, url=None):
    return ft.Container(
        content=ft.Icon(icon_name, color="white", size=25),
        width=48,
        height=48,
        border_radius=24,
        # bgcolor es necesario para que el círculo entero capture el click,
        # no solo los pixeles del ícono (Flutter no "ve" un fondo transparente
        # para hit-testing si no se declara explícitamente).
        bgcolor="#18d341",
        border=ft.Border.all(1, "#20164d"),
        alignment=ft.Alignment.CENTER,
        # url abre el link de forma nativa (sin pasar por Python), evita
        # el bloqueo de popup por delay que sí ocurre con on_click+launch_url.
        url=url,
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


def build_card(max_width: int = 380) -> ft.Container:
    """Construye y devuelve el Container de la tarjeta de perfil.
    No llama a ft.app() ni depende de `page` -- eso lo maneja main.py."""
    return ft.Container(
        width=max_width,
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
                        border_radius=ft.BorderRadius.all(90),
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
                    spacing=8,
                    controls=[
                        social_icon(ft.Icons.PHONE, "tel:+50374196446"),
                        social_icon(ft.Icons.MESSAGE, "https://wa.me/50374196446"),
                        social_icon(ft.Icons.SEND, "https://t.me/ochopitech"),
                        social_icon(ft.Icons.EMAIL, "mailto:rafael@ochopi.com"),
                        social_icon(ft.Icons.CODE, "https://github.com/ochopi"),
                        social_icon(ft.Icons.LANGUAGE, "https://ochopi.com"),
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