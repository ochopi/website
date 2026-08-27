# ochopi.com

Sitio personal — landing, tarjeta de presentación, links, contacto y más.

Construido con [Flet](https://flet.dev) (Python), compilado a un bundle estático (WebAssembly + Pyodide) y desplegado en Cloudflare Pages. Sin backend.

## Stack

- [Flet](https://flet.dev) — UI en Python, compilada a web estático
- Cloudflare Pages — hosting y deploys automáticos por rama

## Desarrollo local

Requisitos: Python 3.12+.

```bash
git clone https://github.com/ochopi/website.git
cd website

python3 -m venv .venv
source .venv/bin/activate
pip install flet flet-desktop

flet run --web --port 3000 main.py
```

Esto levanta la app en el navegador con hot reload en el puerto 3000.

## Build de producción

```bash
flet build web
```

Genera el sitio estático en `build/web/`. 
Se puede servir localmente para verificarlo:

```bash
python3 -m http.server --directory build/web 5000
```

## Build de producción (LEGACY)
Si llegamos a tener problemas con el comando `flet build web` o la build en general (pagina no carga)
Podemos usar el comando legacy `flet publish` que en lugar de publicar el contenido en `build/web/` lo hace en la carpeta `dist`

Luego basta con levantar el server en esa carpeta para comprobar y listo

```bash
python3 -m http.server --directory dist 5000
```

## Deploy

- Push a `dev` → deploy de preview automático.
- Push/merge a `main` → deploy a producción (`ochopi.com`).

## Estructura

```
website/
├── main.py             # punto de entrada de la app Flet
├── pages               # subcarpetas para cada pagina
|   └──── card.py           # pagina para /card
├── build/web/          # salida del build (generada, no versionada)
└── dist/               # salida del build (modo legacy)
```