from os import write
import tkinter
from tkinter import Button, messagebox
from tkinter import font
from tkinter.constants import CENTER, E, RAISED, S, W
from typing import Counter
from PIL import Image, ImageTk
from datetime import datetime

fg_color = '#ffffff'
bg_color = '#89cff0'
root = tkinter.Tk()
root.state('zoomed')
root.configure(background=bg_color)
root.title('Complete health')


def check_range(value, min_limit,  max_limit='no'):
    if max_limit == 'no':
        return min_limit <= value
    return min_limit <= value <= max_limit


def checkReturn_type_num(value):
    try:
        return value.get()
    except:
        ''


def sleep_menu():
    def write():
        h1 = checkReturn_type_num(h_bed)
        m1 = checkReturn_type_num(m_bed)
        h2 = checkReturn_type_num(h_wake)
        m2 = checkReturn_type_num(m_wake)
        ok = True

        if not (type(h1) in [int, float] and check_range(h1, 0, 23)):
            ok = False
            bedtimeh_entry.config(background='red')
        else:
            bedtimeh_entry.config(background='white')

        if not (type(m1) in [int, float] and check_range(m1, 0, 60)):
            ok = False
            bedtimem_entry.config(background='red')
        else:
            bedtimem_entry.config(background='white')

        if not(type(h2) in [int, float] and check_range(h2, 0, 23)):
            ok = False
            wakeuph_entry.config(background='red')
        else:
            wakeuph_entry.config(background='white')

        if not(type(m2) in [int, float] and check_range(m2, 0, 60)):
            ok = False
            wakeupm_entry.config(background='red')
        else:
            wakeupm_entry.config(background='white')

        if ok:
            f_sleep = open('sleep_data.txt', 'a', encoding='utf-8')
            now = datetime.now()
            now = now.strftime('%d/%m/%Y %H:%M:%S')
            sleep_str = now + ', ' + str(h1) + ', ' + str(m1) + ', ' + \
                str(h2) + ', ' + str(m2) + '\n'
            f_sleep.write(sleep_str)

    window_sleep = tkinter.Toplevel(root)
    window_sleep.configure(background=bg_color, width=root.winfo_screenwidth(
    )/2, height=root.winfo_screenheight()/2)

    h_bed = tkinter.IntVar()
    m_bed = tkinter.IntVar()
    h_wake = tkinter.IntVar()
    m_wake = tkinter.IntVar()

    bedtime_label = tkinter.Label(window_sleep, text='Bedtime:', fg=fg_color, bg=bg_color,
                                  font=('roboto', 30, 'bold'))
    bedtime_label.place(relx=0.05, rely=0.2)
    bedtimeh_entry = tkinter.Entry(window_sleep, textvariable=h_bed)
    bedtimeh_entry.place(relx=0.35, rely=0.25)

    bedtimem_entry = tkinter.Entry(window_sleep, textvariable=m_bed)
    bedtimem_entry.place(relx=0.48, rely=0.25)

    wakeup_label = tkinter.Label(window_sleep, text='Wake-up time:', fg=fg_color, bg=bg_color,
                                 font=('roboto', 30, 'bold'))
    wakeup_label.place(relx=0.05, rely=0.4)
    wakeuph_entry = tkinter.Entry(window_sleep, textvariable=h_wake)
    wakeuph_entry.place(relx=0.35, rely=0.45)

    wakeupm_entry = tkinter.Entry(window_sleep, textvariable=m_wake)
    wakeupm_entry.place(relx=0.48, rely=0.45)

    ok_but = Button(window_sleep, text='OK', font=('roboto', 50),
                    bg=bg_color, command=write)
    ok_but.place(relx=0.5, rely=0.8, width=100, height=100, anchor=CENTER)


def weight_menu():
    def write():
        w = checkReturn_type_num(weight)
        bf = checkReturn_type_num(body_fat)
        ok = True

        if not (type(w) in [int, float] and check_range(w, 0)):
            ok = False
            weight_entry.config(background='red')
        else:
            weight_entry.config(background='white')

        if not (type(bf) in [int, float] and check_range(bf, 0)):
            ok = False
            body_fat_entry.config(background='red')
        else:
            body_fat_entry.config(background='white')

        if ok:
            # deschide fișierul local pentru scrierea datelor
            f_weight = open('weight_data.txt', 'a', encoding='utf-8')
            # crează string-ul de afișat
            now = datetime.now()  # data scrierii
            now = now.strftime('%d/%m/%Y %H:%M:%S')
            weight_str = now + ', ' + str(w) + ', ' + str(bf) + '\n'
            f_weight.write(weight_str)  # afișează string-ul

    weight_window = tkinter.Toplevel(root)  # deschide o fereastră nouă
    weight_window.configure(background=bg_color, width=root.winfo_screenwidth(
    )/3, height=root.winfo_screenheight()/3)  # dimensiuni in funcție de cea principală

    weight = tkinter.DoubleVar()    # variabila pentru greutate
    body_fat = tkinter.DoubleVar()  # variabila pentru procentajul de grăsime corporală

    weight_label = tkinter.Label(weight_window, text='Weight:', fg=fg_color, bg=bg_color,
                                 font=('roboto', 30, 'bold'))  # mesajul afișat pentru utilizator
    weight_label.place(relx=0.05, rely=0.2)  # locația textului
    weight_entry = tkinter.Entry(
        weight_window, textvariable=weight)  # textbox-ul pentru input
    weight_entry.place(relx=0.35, rely=0.25)    # plasarea textbox-ului

    body_fat_label = tkinter.Label(weight_window, text='Body:', fg=fg_color, bg=bg_color,  # mesajul afișat pentru utilizator
                                   font=('roboto', 30, 'bold'))
    body_fat_label.place(relx=0.05, rely=0.4)  # locația textului
    body_fat_entry = tkinter.Entry(
        weight_window, textvariable=body_fat)  # textbox-ul pentru input
    body_fat_entry.place(relx=0.35, rely=0.45)  # plasarea textbox-ului

    ok_but = Button(weight_window, text='OK', font=('roboto', 50),  # butonul pentru introducearea datelor
                    bg=bg_color, command=write)
    ok_but.place(relx=0.5, rely=0.8, width=100, height=100,
                 anchor=CENTER)  # plasarea butonului

add_but_img = Image.open('graphics/add_btn.png') # imaginea aferantă butonului
add_but_img = add_but_img.resize((50, 50), Image.ANTIALIAS)
add_but_img = ImageTk.PhotoImage(add_but_img)

def water_menu():
    frame0.pack_forget()

    water_window = tkinter.Frame(root, height=root.winfo_screenheight(
    ), width=root.winfo_screenwidth(), background=bg_color)

    water_window.pack()
    #water_window = tkinter.Toplevel(root)  # deschide o fereastră nouă
    #water_window.configure(background=bg_color, width=root.winfo_screenwidth(
    #)/3, height=root.winfo_screenheight()/3)  # dimensiuni in funcție de cea principală

    water_label = tkinter.Label(water_window, text='ok', image = add_but_img, fg=fg_color, bg=bg_color,  # numărătoarea
                                font=('roboto', 50, 'bold'))
    water_label.place(relx=0.5, rely=0.5, anchor=CENTER)  # locația textului




def sport_menu():
    print('SPORT')


def food_menu():
    print('FOOD')


def mood_menu():
    print('MOOD')


def profile_menu():
    print('PROFILE')


if __name__ == '__main__':

    frame0 = tkinter.Frame(root, height=root.winfo_screenheight(
    ), width=root.winfo_screenwidth(), background=bg_color)
    frame0.pack()

    logo_img = Image.open('graphics/logo.png')
    logo_img = logo_img.resize((750, 250), Image.ANTIALIAS)
    logo_img = ImageTk.PhotoImage(logo_img)
    logo = tkinter.Label(frame0, image=logo_img, bg=bg_color)
    logo.place(relx=0.5, rely=0.15, anchor=CENTER)

    x_col_1 = 0.15
    x_col_2 = 0.5
    x_col_3 = 0.85

    y_row_1 = 0.4
    y_row_2 = 0.6
    y_row_3 = 0.8

    slp_but_img = Image.open('graphics/sleep_btn.png')
    slp_but_img = slp_but_img.resize((250, 100), Image.ANTIALIAS)
    slp_but_img = ImageTk.PhotoImage(slp_but_img)
    slp_but = Button(frame0, image=slp_but_img, bg=bg_color,
                     command=sleep_menu, borderwidth=0)
    slp_but.place(relx=(x_col_1 + x_col_2)/2, rely=y_row_1,
                  width=250, height=100, anchor=CENTER)

    wgt_but_img = Image.open('graphics/weight_btn.png')
    wgt_but_img = wgt_but_img.resize((250, 100), Image.ANTIALIAS)
    wgt_but_img = ImageTk.PhotoImage(wgt_but_img)
    wgt_but = Button(frame0, image=wgt_but_img, bg=bg_color,
                     command=weight_menu, borderwidth=0)
    wgt_but.place(relx=(x_col_2+x_col_3)/2, rely=y_row_1,
                  width=250, height=100, anchor=CENTER)

    wtr_but_img = Image.open('graphics/water_btn.png')
    wtr_but_img = wtr_but_img.resize((250, 100), Image.ANTIALIAS)
    wtr_but_img = ImageTk.PhotoImage(wtr_but_img)
    wtr_but = Button(frame0, image=wtr_but_img, bg=bg_color,
                     command=water_menu, borderwidth=0)
    wtr_but.place(relx=x_col_1, rely=y_row_2,
                  width=250, height=100, anchor=CENTER)

    sprt_but_img = Image.open('graphics/sport_btn.png')
    sprt_but_img = sprt_but_img.resize((250, 100), Image.ANTIALIAS)
    sprt_but_img = ImageTk.PhotoImage(sprt_but_img)
    sprt_but = Button(frame0, image=sprt_but_img, bg=bg_color,
                      command=sport_menu, borderwidth=0)
    sprt_but.place(relx=x_col_2, rely=y_row_2,
                   width=250, height=100, anchor=CENTER)

    food_but_img = Image.open('graphics/food_btn.png')
    food_but_img = food_but_img.resize((250, 100), Image.ANTIALIAS)
    food_but_img = ImageTk.PhotoImage(food_but_img)
    food_but = Button(frame0, image=food_but_img, bg=bg_color,
                      command=food_menu, borderwidth=0)
    food_but.place(relx=x_col_3, rely=y_row_2,
                   width=250, height=100, anchor=CENTER)

    mood_but_img = Image.open('graphics/mood_btn.png')
    mood_but_img = mood_but_img.resize((250, 100), Image.ANTIALIAS)
    mood_but_img = ImageTk.PhotoImage(mood_but_img)
    mood_but = Button(frame0, image=mood_but_img, bg=bg_color,
                      command=mood_menu, borderwidth=0)
    mood_but.place(relx=(x_col_1+x_col_2)/2, rely=y_row_3,
                   width=250, height=100, anchor=CENTER)

    jrnl_but_img = Image.open('graphics/journal_btn.png')
    jrnl_but_img = jrnl_but_img.resize((250, 100), Image.ANTIALIAS)
    jrnl_but_img = ImageTk.PhotoImage(jrnl_but_img)
    jrnl_but = Button(frame0, image=jrnl_but_img, bg=bg_color,
                      command=mood_menu, borderwidth=0)
    jrnl_but.place(relx=(x_col_2+x_col_3)/2, rely=y_row_3,
                   width=250, height=100, anchor=CENTER)

    prfl_but_img = Image.open('graphics/profile_btn.png')
    prfl_but_img = prfl_but_img.resize((100, 100), Image.ANTIALIAS)
    prfl_but_img = ImageTk.PhotoImage(prfl_but_img)
    prfl_but = Button(frame0, image=prfl_but_img, bg=bg_color,
                      command=profile_menu, borderwidth=0)
    prfl_but.place(relx=x_col_1-0.09, rely=y_row_3+0.1,
                   width=100, height=100, anchor=CENTER)

    root.mainloop()
