# main.py
import flet as ft
from pages.card import build_card
 
 
def main(page: ft.Page):
    page.title = "ochopi.com"
    page.bgcolor = "#1a0f2e"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20
 
    page.add(build_card(page))
 
 
ft.app(target=main, assets_dir="assets")
 