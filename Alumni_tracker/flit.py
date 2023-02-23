import flet as ft
import sqlite3
from extract import test
from email_check import solve
# print(dir(ft))

def main(page:ft.page):
    page.window_width=300
    page.window_height=500
    page.scroll=ft.ScrollMode.ALWAYS
    # page.bgcolor=ft.colors.BLUE_GREY_900
    connection=sqlite3.connect('AlumniTrack.db',check_same_thread=False)
    cursor=connection.cursor()

    dlg = ft.AlertDialog(
        title=ft.Text("Email you entered is not correct",
                      color=ft.colors.ERROR,italic=True)
    )
    dlg_pass=ft.AlertDialog(
        title=ft.Text("password not matches",
                      color=ft.colors.ERROR,italic=True)
    )
    dlg_Url=ft.AlertDialog(
        title=ft.Text("LinkedIn Url is not valid",
                      color=ft.colors.ERROR,italic=True)
    )
    dlg_login=ft.AlertDialog(
        title=ft.Text("Email or Password is Not correct",
                      color=ft.colors.ERROR,italic=True)
    )
    dlg_info = ft.AlertDialog(
        title=ft.Text(f'NAN',
                      color=ft.colors.ERROR, italic=True)
    )
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
    def open_dlg_pass(e):
        page.dialog = dlg_pass
        dlg_pass.open = True
        page.update()

    def open_dlg_Url(e):
        page.dialog = dlg_Url
        dlg_Url.open = True
        page.update()
    def open_dlg_login(e):
        page.dialog = dlg_login
        dlg_login.open = True
        page.update()

    def addTask(p):
        p.page.add(ft.ProgressRing())
        Company.value,Name.value=test(Url.value)
        if Company.value!='NAN':
            print(Name.value)
            p.page.go('/signupdetails')
        else:
            open_dlg_Url(p)

    def done(e):
        query='''
        INSERT INTO USERS(Name,Year,Branch,Email,password,Company,LinkedinURL)
        values(?,?,?,?,?,?,?)
        '''
        values=[
            (f'{Name.value}',f'{Year_pass_out.value}',f'{Branch.value}',f'{email.value}',f'{password_i.value}',f'{Company.value}',f'{Url.value}')
        ]
        cursor.executemany(query,values)
        connection.commit()
    def Added(e):
        if solve(email.value):
            if password_i.value == C_password.value:
                done(e)
                e.page.go('/login')
            else:
                print(password_i.value)
                open_dlg_pass(e)
                print(C_password.value)
        else:
            open_dlg(e)
    def check(e):
        cursor.execute("SELECT * FROM USERS")
        data=cursor.fetchall()
        for i,user in enumerate(data):
            if data[i][3]==username.value:
                if data[i][4]== password.value:
                    e.page.go('/AlumniDetails')
                    break
        else:
            open_dlg_login(e)
    def show_info(e,i):
        print(i)


    def change_route(route):
        if page.route=='/':
            page.views.clear()
            page.views.append(
                ft.View(
                    route='/',
                    controls=[
                        ft.ElevatedButton(
                            text='LOGIN',
                            on_click=lambda e:e.page.go('/login')
                        ),
                        ft.ElevatedButton(
                            text='SIGNUP',
                            on_click=lambda e: e.page.go('/signup'),
                        ),

                    ],
                    bgcolor=ft.colors.BLUE_GREY,
                    padding=ft.padding.all(100)
                )
            )
        if page.route == '/signup':
            # page.views.clear()
            page.views.append(
                ft.View(
                    # bgcolor=ft.colors.INDIGO_300,
                    appbar=ft.AppBar(
                        title=ft.Text(
                            'signup page'
                        )
                    ),
                    controls=[Url, Year_pass_out, Branch, bt]
                )
            )
        if page.route == '/login':
            # page.views.clear()
            page.views.append(
                ft.View(
                    appbar=ft.AppBar(
                        title=ft.Text(
                            'LogIn page'
                        )
                    ),
                    controls=[username,password,bot]
                )
            )
        if page.route == '/signupdetails':
            page.views.append(
                ft.View(
                    appbar=ft.AppBar(
                        title=ft.Text(
                            'SignUpdetails'
                        )
                    ),
                    controls=[email, password_i, C_password, but]
                )
            )
        if page.route =='/AlumniDetails':
            page.views.append(
                ft.View(
                    bgcolor=ft.colors.INDIGO_200,
                    appbar=ft.AppBar(
                        title=ft.Text(
                            'Alumni Page'
                        )
                    ),

                    controls=[gv],
                    scroll=True
                ),
            )
            # for i in range(5):
            #     page.add(Alumni)

    def pop_view(route):
        page.views.pop()
        top_page=page.views[-1]
        page.go(top_page.route)
    ##for person's name and company
    Name=ft.Text(value="NAN")
    Company=ft.Text(value="NAN")
    #For Signup Page
    Url =ft.TextField(label="Give LinkedIn url",
                      border_radius=ft.border_radius.only(topLeft=20,bottomRight=30),
                      border_width=5,
                      border_color=ft.colors.BLUE_GREY_200,
                      focused_border_color=ft.colors.BLUE,
                      icon=ft.icons.PERSON_2)
    Year_pass_out = ft.TextField(label="Year of pass out",
                                 border_radius=ft.border_radius.only(topLeft=20,bottomRight=30),
                      border_width=5,
                      border_color=ft.colors.BLUE_GREY_200,
                      focused_border_color=ft.colors.BLUE,
                      icon=ft.icons.CALENDAR_MONTH,
                      keyboard_type='number')
    Branch = ft.TextField(label="Branch",
                          border_radius=ft.border_radius.only(topLeft=20,bottomRight=30),
                      border_width=5,
                      border_color=ft.colors.BLUE_GREY_200,
                      focused_border_color=ft.colors.BLUE,
                      icon=ft.icons.BOOK_SHARP)
    bt= ft.ElevatedButton(text='Sumbit', on_click=addTask,icon=ft.icons.CLOUD_DONE)
    ##For Login Page
    username=ft.TextField(label="Email",
                          border_radius=ft.border_radius.only(topLeft=20,bottomRight=30),
                         border_width=5,
                            border_color=ft.colors.BLUE_GREY_200,
                          focused_border_color=ft.colors.BLUE,
                      icon=ft.icons.PERSON)
    password = ft.TextField(label="Password",
                            border_radius=ft.border_radius.only(topLeft=20, bottomRight=30),
                            border_width=5,
                            border_color=ft.colors.BLUE_GREY_200,
                            focused_border_color=ft.colors.BLUE,
                            icon=ft.icons.PASSWORD,
                            password=True,
                            can_reveal_password=True)
    bot=ft.ElevatedButton(text='Sumbit',on_click=check,icon=ft.icons.CLOUD_DONE)
    ##For Signup Details
    email = ft.TextField(label="Email",
                         border_radius=ft.border_radius.only(topLeft=20, bottomRight=30),
                         border_width=5,
                         border_color=ft.colors.BLUE_GREY_200,
                         focused_border_color=ft.colors.BLUE,
                         icon=ft.icons.EMAIL)
    password_i= ft.TextField(label="Password",
                            border_radius=ft.border_radius.only(topLeft=20, bottomRight=30),
                            border_width=5,
                            border_color=ft.colors.BLUE_GREY_200,
                            focused_border_color=ft.colors.BLUE,
                            icon=ft.icons.PASSWORD,
                            password=True,
                            can_reveal_password=True)
    C_password = ft.TextField(label="Confirm Password",
                         border_radius=ft.border_radius.only(topLeft=20, bottomRight=30),
                         border_width=5,
                         border_color=ft.colors.BLUE_GREY_200,
                         focused_border_color=ft.colors.BLUE,
                         icon=ft.icons.PASSWORD,
                              password=True,
                              can_reveal_password=True)
    but=ft.ElevatedButton(text='Sumbit',on_click=Added,icon=ft.icons.CLOUD_DONE)
    # # com=ft.Column(controls=[
    # #     Url,Year_pass_out,Branch
    # # ])
    # bar=ft.AppBar(title=ft.Text('hello'))
    # # page.update()
    # page.add(Url,Year_pass_out,Branch,bt)
    ##For Alumni Page
    # about=[]

    cursor.execute("SELECT * FROM USERS")
    data = cursor.fetchall()
    Alum=[]
    Alumni=''
    gv = ft.GridView(expand=False, max_extent=270,run_spacing=100,padding=ft.padding.only(right=20,left=20),height=1000)
    for i,info in enumerate(data):
        gv.controls.append(ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.PERSON_ADD),
                        title=ft.Text(data[i][0],max_lines=2,overflow=ft.TextOverflow.ELLIPSIS,size=15),
                        subtitle=ft.Text(
                            data[i][5],max_lines=2,overflow=ft.TextOverflow.ELLIPSIS,

                        ),
                        content_padding=ft.padding.all(30)
                    ),
                    ft.Row(
                        [ft.Text(value=f'{data[i][1]}', color=ft.colors.BLACK87),
                         ft.Text(value=f'{data[i][2]}')],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                    ft.Row(
                        [ft.ElevatedButton(text="LinkedIN", icon=ft.icons.PERSON_2, color=ft.colors.BLACK87),
                         ft.TextButton("CHAT")],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),
            width=100,
            height=100,
            padding=ft.padding.only(right=30,bottom=30),
            bgcolor=ft.colors.BLUE_GREY_100,
            border_radius=ft.border_radius.only(topLeft=30, bottomRight=50),
            # alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            # on_click=lambda e:show_info(e,i)


        )
        )
        Alum.append(Alumni)
                # bgcolor=ft.colors.BLACK87
    # Alum.append(Alum)
    Alumm=[ft.Row(Alum,
                  alignment=ft.MainAxisAlignment.SPACE_AROUND),
           ft.Row(Alum,
                  alignment=ft.MainAxisAlignment.SPACE_EVENLY)]
    page.update()
    page.on_route_change= change_route
    page.on_view_pop=pop_view
    page.go(page.route)





ft.app(target=main,view=ft.FLET_APP)