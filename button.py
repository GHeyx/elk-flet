import flet as ft

def main(page):
    page.title = "Flet Buttons example"


    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    def login_click(e):
        if not txt_username.value:
            txt_username.error_text = "Please enter your username"
            page.update()
        else:
            name = txt_username.value
            # page.clean()
            page.add(ft.Text(f"Welcome to the family, {name}!"))

    def signup_click(e):
        page.add(ft.Text(f"Sign Up button clicked"))
    def quit_click(e):
        page.window_close()

    txt_username = ft.TextField(label="Username")
    txt_password = ft.TextField(label="Password")

    page.add(txt_username,txt_password)
    login = ft.ElevatedButton("Login", on_click=login_click)
    sign_up = ft.ElevatedButton("Signup", on_click=signup_click)
    page.add(login, sign_up)
    page.add(ft.ElevatedButton("Quit", on_click=quit_click))
    page.window_center()

    
ft.app(target=main)