import flet as ft
from components.icons import icon_widget

GRADIENT = ft.LinearGradient(
    begin=ft.Alignment.TOP_CENTER,
    end=ft.Alignment.BOTTOM_CENTER,
    colors=["#5b2c8e", "#3d1a66"],
)

SOCIAL_LINKS = [
    (ft.Icons.PHONE, "tel:+50374196446"),
    ("sh:whatsapp-light.png", "https://wa.me/50374196446"),
    (ft.Icons.SEND, "https://t.me/ochopitech"),
    (ft.Icons.EMAIL, "mailto:rafael@ochopi.com"),
    ("di:github-light.png", "https://github.com/ochopi"),
    (ft.Icons.LANGUAGE, "https://ochopi.com"),
]

CHECKLIST_ITEMS = [
    "Diagnóstico",
    "Mantenimiento",
    "Automatización",
    "Windows OS",
    "Linux OS",
    "Self-Hosting",
]

PARAGRAPH_1 = (
    "Trabajo con sistemas informáticos, realizando diagnóstico "
    "y resolución de problemas de software y hardware."
)
PARAGRAPH_2 = (
    "Me interesa la automatización y optimización de procesos, "
    "así como la creación de soluciones prácticas para "
    "problemas técnicos."
)


# ---------- piezas compartidas ----------

def social_icon(icon_ref, url=None):
    return ft.Container(
        content=icon_widget(icon_ref, size=22, color="white"),
        width=48,
        height=48,
        border_radius=24,
        # bgcolor necesario para que el círculo entero capture el click,
        # no solo los pixeles del ícono.
        bgcolor="#18d341",
        border=ft.Border.all(1, "#20164d"),
        alignment=ft.Alignment.CENTER,
        url=url,
        ink=True,
    )


def icons_row() -> ft.Row:
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=12,
        controls=[social_icon(icon, url) for icon, url in SOCIAL_LINKS],
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


def checklist_column() -> ft.Column:
    return ft.Column(
        spacing=10,
        controls=[check_item(t) for t in CHECKLIST_ITEMS],
    )


def avatar(size: int = 180) -> ft.Container:
    return ft.Container(
        width=size,
        height=size,
        border_radius=size // 2,
        content=ft.Image(
            src="rafael.jpg",
            fit=ft.BoxFit.COVER,
            border_radius=ft.BorderRadius.all(size // 2),
        ),
    )


def services_row(alignment=ft.MainAxisAlignment.CENTER) -> ft.Row:
    return ft.Row(
        alignment=alignment,
        controls=[
            ft.Text("Servicios Informáticos:", color="white", size=16),
            ft.Text("ochopi tech", color="white", size=16,
                    weight=ft.FontWeight.BOLD, italic=True),
        ],
    )


def paragraph(text_str, align=ft.TextAlign.CENTER) -> ft.Text:
    return ft.Text(text_str, color="white", size=16, text_align=align)


# ---------- layout angosto (móvil / retrato) ----------

def build_card_narrow(max_width: int = 380) -> ft.Container:
    return ft.Container(
        width=max_width,
        padding=30,
        border_radius=28,
        gradient=GRADIENT,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,
            controls=[
                avatar(180),
                ft.Text("RAFAEL", size=42, color="white", weight=ft.FontWeight.W_300),
                ft.Text("+503 7419 6446", size=20, color="white",
                        weight=ft.FontWeight.BOLD),
                services_row(),
                icons_row(),
                paragraph(PARAGRAPH_1),
                paragraph(PARAGRAPH_2),
                checklist_column(),
            ],
        ),
    )


# ---------- layout ancho (pc / tablet horizontal) ----------

def build_card_wide(max_width: int = 900) -> ft.Container:
    header = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=8,
                expand=True,
                controls=[
                    ft.Text("RAFAEL", size=42, color="white",
                            weight=ft.FontWeight.W_300),
                    ft.Text("+503 7419 6446", size=20, color="white",
                            weight=ft.FontWeight.BOLD),
                    services_row(alignment=ft.MainAxisAlignment.START),
                ],
            ),
            avatar(170),
        ],
    )

    body = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.START,
        spacing=50,
        controls=[
            ft.Container(content=checklist_column(), expand=1),
            ft.Column(
                expand=2,
                controls=[
                    paragraph(PARAGRAPH_1),
                    paragraph(PARAGRAPH_2),
                ],
            ),
        ],
    )

    return ft.Container(
        width=max_width,
        padding=40,
        border_radius=28,
        gradient=GRADIENT,
        content=ft.Column(
            spacing=28,
            controls=[
                header,
                icons_row(),
                body,
            ],
        ),
    )