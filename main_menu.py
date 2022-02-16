from os import write
import tkinter
from tkinter import Button, messagebox
from tkinter import font
from tkinter.constants import ACTIVE, CENTER, E, HORIZONTAL, RAISED, S, W
from typing import Counter
from PIL import Image, ImageTk
from datetime import datetime

fg_color = '#ffffff'
bg_color = '#89cff0'
root = tkinter.Tk()
root.state('zoomed')
root.configure(background=bg_color)
root.title('Complete health')
root.minsize(1024, 768)


def check_range(value, min_limit,  max_limit='no'):
    if max_limit == 'no':
        return min_limit <= value
    return min_limit <= value <= max_limit


def checkReturn_type_num(value):
    try:
        return value.get()
    except:
        ''


# imaginile trebuie deschise global, căci altfel procesul de garbage collection le face inaccesibile
ok_but_img = Image.open('graphics/ok_btn.png')  # imaginea aferantă butonului
ok_but_img = ok_but_img.resize((100, 100), Image.ANTIALIAS)
ok_but_img = ImageTk.PhotoImage(ok_but_img)


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
    bedtimeh_entry.place(relx=0.40, rely=0.25)

    bedtimem_entry = tkinter.Entry(window_sleep, textvariable=m_bed)
    bedtimem_entry.place(relx=0.55, rely=0.25)

    wakeup_label = tkinter.Label(window_sleep, text='Wake-up time:', fg=fg_color, bg=bg_color,
                                 font=('roboto', 30, 'bold'))
    wakeup_label.place(relx=0.05, rely=0.4)
    wakeuph_entry = tkinter.Entry(window_sleep, textvariable=h_wake)
    wakeuph_entry.place(relx=0.40, rely=0.45)

    wakeupm_entry = tkinter.Entry(window_sleep, textvariable=m_wake)
    wakeupm_entry.place(relx=0.55, rely=0.45)

    ok_but = Button(window_sleep, image=ok_but_img,
                    bg=bg_color, borderwidth=0, command=write)
    ok_but.place(relx=0.5, rely=0.75, width=100, height=100, anchor=CENTER)


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

    ok_but = Button(weight_window, image=ok_but_img,  # butonul pentru introducearea datelor
                    bg=bg_color, borderwidth=0, command=write)
    ok_but.place(relx=0.5, rely=0.75, width=100, height=100,
                 anchor=CENTER)  # plasarea butonului


# imaginile trebuie deschise global, căci altfel procesul de garbage collection le face inaccesibile
sub_but_img = Image.open('graphics/sub_btn.png')  # imaginea aferantă butonului
sub_but_img = sub_but_img.resize((100, 100), Image.ANTIALIAS)
sub_but_img = ImageTk.PhotoImage(sub_but_img)
add_but_img = Image.open('graphics/add_btn.png')  # imaginea aferantă butonului
add_but_img = add_but_img.resize((100, 100), Image.ANTIALIAS)
add_but_img = ImageTk.PhotoImage(add_but_img)


def water_menu():
    count = 0

    def change_up():
        nonlocal count
        count += 1
        water_label.config(text=f'{count}')
        f_sleep = open('water_data.txt', 'a', encoding='utf-8')
        now = datetime.now()
        now = now.strftime('%d/%m/%Y %H:%M:%S')
        water_str = now + ', ' + str(count) + '\n'
        f_sleep.write(water_str)

    def change_down():
        nonlocal count
        if count > 0:
            count -= 1
            water_label.config(text=f'{count}')
            f_sleep = open('water_data.txt', 'a', encoding='utf-8')
            now = datetime.now()
            now = now.strftime('%d/%m/%Y %H:%M:%S')
            water_str = now + ', ' + str(count) + '\n'
            f_sleep.write(water_str)

    water_window = tkinter.Toplevel(root)  # deschide o fereastră nouă
    water_window.configure(background=bg_color, width=root.winfo_screenwidth(
    )/3, height=root.winfo_screenheight()/3)  # dimensiuni in funcție de cea principală
    water_label = tkinter.Label(water_window, text='0', fg=fg_color, bg=bg_color,  # numărătoarea
                                font=('roboto', 100, 'bold'))
    water_label.place(relx=0.5, rely=0.5, anchor=CENTER)  # locația textului

    # butonul pentru incrementarea valorii
    add_but = Button(water_window, image=add_but_img,
                     bg=bg_color, borderwidth=0, command=change_up)
    add_but.place(relx=0.75, rely=0.5, width=100, height=100,
                  anchor=CENTER)  # plasarea butonului

    # butonul pentru decrementarea valorii
    sub_but = Button(water_window, image=sub_but_img,
                     bg=bg_color, borderwidth=0, command=change_down)
    sub_but.place(relx=0.25, rely=0.5, width=100, height=100,
                  anchor=CENTER)  # plasarea butonului


def sport_menu():
    print('SPORT')


def food_menu():
    print('FOOD')


sad2_img = Image.open('graphics/sad2_btn.png')  # imaginea aferantă butonului
sad2_img = sad2_img.resize((125, 125), Image.ANTIALIAS)
sad2_img = ImageTk.PhotoImage(sad2_img)

sad1_img = Image.open('graphics/sad1_btn.png')  # imaginea aferantă butonului
sad1_img = sad1_img.resize((125, 125), Image.ANTIALIAS)
sad1_img = ImageTk.PhotoImage(sad1_img)

neutral_img = Image.open('graphics/neutral_btn.png')  # imaginea aferantă butonului
neutral_img = neutral_img.resize((125, 125), Image.ANTIALIAS)
neutral_img = ImageTk.PhotoImage(neutral_img)

happy1_img = Image.open('graphics/happy1_btn.png')  # imaginea aferantă butonului
happy1_img = happy1_img.resize((125, 125), Image.ANTIALIAS)
happy1_img = ImageTk.PhotoImage(happy1_img)

happy2_img = Image.open('graphics/happy2_btn.png')  # imaginea aferantă butonului
happy2_img = happy2_img.resize((125, 125), Image.ANTIALIAS)
happy2_img = ImageTk.PhotoImage(happy2_img)

def mood_menu():
    mood = ''

    def sad2():
        nonlocal mood
        mood = 'very sad'

    def sad1():
        nonlocal mood
        mood = 'sad'

    def neutral():
        nonlocal mood
        mood = 'neutral'

    def happy1():
        nonlocal mood
        mood = 'happy'

    def happy2():
        nonlocal mood
        mood = 'very happy'

    def write():
        if mood != '':
            f_sleep = open('mood_data.txt', 'a', encoding='utf-8')
            now = datetime.now()
            now = now.strftime('%d/%m/%Y %H:%M:%S')
            mood_str = now + ', ' + mood + '\n'
            f_sleep.write(mood_str)

    window_mood = tkinter.Toplevel(root)
    window_mood.configure(background=bg_color, width=root.winfo_screenwidth(
    )*2/5, height=root.winfo_screenheight()/3)

    mood_sad2_but = Button(window_mood, image=sad2_img, bg=bg_color, borderwidth=0, command=sad2).place(relx=0.1, rely=0.3, anchor=CENTER)

    mood_sad1_but = Button(window_mood, image=sad1_img, bg=bg_color, borderwidth=0, command=sad1).place(relx=0.3, rely=0.3, anchor=CENTER)

    mood_neutral_but = Button(window_mood, image=neutral_img, bg=bg_color, borderwidth=0, command=neutral).place(relx=0.5, rely=0.3, anchor=CENTER)

    mood_happy1_but = Button(window_mood, image=happy1_img, bg=bg_color, borderwidth=0, command=happy1).place(relx=0.7, rely=0.3, anchor=CENTER)

    mood_happy2_but = Button(window_mood, image=happy2_img, bg=bg_color, borderwidth=0, command=happy2).place(relx=0.9, rely=0.3, anchor=CENTER)

    ok_but = Button(window_mood, image=ok_but_img,
                    bg=bg_color, borderwidth=0, command=write)
    ok_but.place(relx=0.5, rely=0.75, width=100, height=100, anchor=CENTER)


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
