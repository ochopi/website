# main.py
import flet as ft

def main(page: ft.Page):
    page.title = "ochopi"
    page.add(ft.Text("Hola Mundo!, Esto es ochopi.com 🎉"))

ft.app(target=main)