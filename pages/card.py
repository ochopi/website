import flet as ft
from components.icons import icon_widget

GRADIENT = ft.LinearGradient(
    begin=ft.Alignment.TOP_CENTER,
    end=ft.Alignment.BOTTOM_CENTER,
    colors=["#5b2c8e", "#3d1a66"],
)

# ---------- datos del card ----------
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

def build_icon(icon=ft.Icons.CHECK, url=None, size=16, color="white", bgcolor="#7cb342", width=24, height=24, border=ft.Border.all(1, "#20164d"), border_radius=6, alignment=ft.Alignment.CENTER, ink=True) -> ft.Container:
    return ft.Container(
        content=icon_widget(icon, size=size, color=color),
        bgcolor=bgcolor,
        width=width,
        height=height,
        border=border,
        border_radius=border_radius,
        alignment=alignment,
        url=url,
        ink=ink,
    )

def icons_row(spacing=12, alignment=ft.MainAxisAlignment.CENTER, size=16, color="white", bgcolor="#7cb342", width=24, height=24, border=ft.Border.all(1, "#20164d"), border_radius=6, icon_alignment=ft.Alignment.CENTER, ink=True) -> ft.Row:
    controls_list = []
    for icon, url in SOCIAL_LINKS:
        row = build_icon(
            icon=icon,
            url=url, 
            size=size, 
            color=color, 
            bgcolor=bgcolor,
            width=width,
            height=height,
            border=border,
            border_radius=border_radius,
            alignment=icon_alignment,
            ink=ink,
        )
        controls_list.append(row)

    return ft.Row(
        spacing=spacing,
        alignment=alignment,
        controls=controls_list,
    )

def checklist_row(text_str, spacing=10, size=14, color="white", icon_bgcolor="#7cb342", icon=ft.Icons.CHECK, icon_width=20, icon_height=20, icon_border_radius=6, icon_alignment=ft.Alignment.CENTER) -> ft.Row:
    return ft.Row(
        spacing=spacing,
        controls=[
            build_icon(icon=icon, size=size, color=color, bgcolor=icon_bgcolor, width=icon_width, height=icon_height, border_radius=icon_border_radius, alignment=icon_alignment),
            ft.Text(text_str,  size=size, color=color, weight=ft.FontWeight.BOLD, italic=True),
        ],
    )

def checklist_column(c_spacing=10) -> ft.Column:
    controls_list = []
    for item in CHECKLIST_ITEMS:
        row = checklist_row(
            item,  
            size=14, 
            color="white", 
            icon_bgcolor="#7cb342", 
            icon=ft.Icons.CHECK, 
            icon_width=20, 
            icon_height=20,
        )
        controls_list.append(row)

    return ft.Column(
        spacing=c_spacing,
        controls=controls_list,
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


def brand_row(alignment=ft.MainAxisAlignment.CENTER) -> ft.Row:
    return ft.Column(
        alignment=alignment,
        horizontal_alignment=alignment,
        spacing=0,
        controls=[
            ft.Text("+503 7419 6446", size=18, color="white", weight=ft.FontWeight.BOLD),
            ft.Row(
                alignment=alignment,
                controls=[
                    ft.Text("Servicios Informáticos:", color="white", size=16),
                    ft.Text("ochopi tech", color="white", size=16, weight=ft.FontWeight.BOLD, italic=True),
                ],
            ),
        ],
    )


def paragraph(text_str, align=ft.TextAlign.CENTER, size=16, color="white") -> ft.Text:
    return ft.Text(text_str, text_align=align, size=size, color=color)


# ---------- narrow layout (móvil) ----------

def build_card_narrow(max_width: int = 380) -> ft.Container:
    return ft.Container(
        width=max_width,
        padding=30,
        border_radius=28,
        gradient=GRADIENT,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                avatar(150),
                ft.Text("RAFAEL", size=38, color="white", weight=ft.FontWeight.W_300),
                brand_row(),
                icons_row(spacing=12, alignment=ft.MainAxisAlignment.CENTER, size=20, width=40, height=40, border=ft.Border.all(1, "#00000000"), border_radius=24, bgcolor="#00000000"),
                paragraph(PARAGRAPH_1, align=ft.TextAlign.CENTER, size=14, color="white"),
                paragraph(PARAGRAPH_2, size=14),
                checklist_column(),
            ],
        ),
    )


# ---------- wide layout (pc / tablet) ----------

def build_card_wide(max_width: int = 900) -> ft.Container:
    header = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=8,
                expand=True,
                controls=[
                    ft.Text("RAFAEL", size=42, color="white", weight=ft.FontWeight.W_300),
                    brand_row(alignment=ft.MainAxisAlignment.START),
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
                    paragraph(PARAGRAPH_1, align=ft.TextAlign.CENTER, size=14, color="white"),
                    paragraph(PARAGRAPH_2, size=14),
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
                icons_row(spacing=12, alignment=ft.MainAxisAlignment.CENTER, size=20, width=40, height=40, border_radius=24),
                body,
            ],
        ),
    )

# ---------- punto de entrada único ----------
 
# WIDE_BREAKPOINT < 700 usa el layout vertical (móvil/tablet en retrato);
# igual o por encima, el layout horizontal (pc/tablet apaisada).
WIDE_BREAKPOINT = 700
 
 
def build_card(screen_width: float) -> ft.Control:
    """Construye el card narrow/wide según el ancho de pantalla disponible."""
    screen_width = screen_width or 380
    is_wide = screen_width >= WIDE_BREAKPOINT
 
    if is_wide:
        # deja margen a los lados, tope de 900px para que no se estire demasiado en monitores enormes
        card_width = min(900, screen_width - 64)
        card = build_card_wide(max_width=card_width)
    else:
        card_width = min(480, screen_width - 32)
        card = build_card_narrow(max_width=card_width)
 
    return ft.Container(
        content=card,
        alignment=ft.Alignment.CENTER,
        expand=True,
        padding=ft.Padding.symmetric(vertical=24, horizontal=16),
    )
