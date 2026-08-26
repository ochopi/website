# main.py
import flet as ft

def main(page: ft.Page):
    page.title = "ochopi"
    page.add(ft.Text("Hola Mundo!, Esto es ochopi.com 2.0 🎉"))

ft.app(target=main)