"""
Resolución de íconos externos estilo Glance ("di:whatsapp.png",
"sh:whatsapp-light.png") + wrapper para usarlos como cualquier ft.Icon.

Uso en cualquier página:

    from components.icons import icon_widget

    icon_widget(ft.Icons.PHONE, size=22, color="white")   # ícono nativo
    icon_widget("di:whatsapp.png", size=22)                # dashboard-icons (PNG)
    icon_widget("sh:github-light.png", size=22)            # selfh.st (PNG)
    icon_widget("si:simplenote", size=22)                  # simpleicons (SVG, color de marca)
    icon_widget("si:simplenote/3361CC", size=22)           # simpleicons (SVG, color fijo)
    icon_widget("https://otra-cdn.com/logo.png", size=22)  # URL directa

Nota sobre "si:" (Simple Icons): a diferencia de "di:" y "sh:", el CDN de
Simple Icons (cdn.simpleicons.org) SOLO sirve SVG, no PNG -- no hay opción
de elegir formato. El soporte de Flet para SVG por red es menos confiable
que para PNG/JPG (existe incluso una extensión aparte, flet-svg, hecha
justo para resolver esto). Pruébalo primero; si el ícono no aparece,
lo cambiamos a la extensión flet-svg en vez de ft.Image.
"""

import flet as ft

# Agrega aquí nuevos proveedores cuando los necesites -- solo hace falta
# el prefijo corto y la plantilla de URL con {name}.
ICON_PROVIDERS = {
    "di": "https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/png/{name}",
    "sh": "https://cdn.jsdelivr.net/gh/selfhst/icons/png/{name}",
    # {name} puede incluir el color: "si:simplenote/3361CC" -> .../simplenote/3361CC
    "si": "https://cdn.simpleicons.org/{name}",
}


def resolve_icon_src(ref: str) -> str:
    """Convierte 'di:whatsapp.png' o 'sh:whatsapp-light.png' en la URL
    completa del CDN. Si ya es una URL completa, la deja igual."""
    if ref.startswith(("http://", "https://")):
        return ref
    if ":" in ref:
        prefix, name = ref.split(":", 1)
        base = ICON_PROVIDERS.get(prefix)
        if base:
            return base.format(name=name)
    return ref  # fallback: se usa tal cual (probablemente rompa, avisa)


def is_external_icon(ref) -> bool:
    """True si 'ref' es un string tipo 'di:x.png' / 'sh:x.png' / URL,
    False si es un ft.Icons.* (esos no son str, son IconData)."""
    return isinstance(ref, str) and (
        ref.startswith(("http://", "https://"))
        or any(ref.startswith(f"{p}:") for p in ICON_PROVIDERS)
    )


def icon_widget(icon_ref, size: int = 24, color: str = "white") -> ft.Control:
    """Devuelve un control listo para usar: ft.Image si es ícono externo,
    ft.Icon si es un ft.Icons.* nativo. Úsalo en vez de ft.Icon(...) cada
    vez que el ícono pueda venir de afuera."""
    if is_external_icon(icon_ref):
        return ft.Image(
            src=resolve_icon_src(icon_ref),
            width=size,
            height=size,
            fit=ft.BoxFit.CONTAIN,
        )
    return ft.Icon(icon_ref, color=color, size=size)