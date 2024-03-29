# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:59:12 2023

@author: ehele
"""

from tkinter import messagebox
from hashlib import pbkdf2_hmac
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")



class PasswordManager(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        ### variables for the log-in window
        self.name = tk.StringVar(value='', name='name')
        self.password = tk.StringVar(value='', name='password')
        self.salt = tk.StringVar(value='', name='salt')
        self.pepper = tk.StringVar(value='', name='pepper')
        
        

class PasswordManagerTopLevel (ctk.CTkToplevel):
    def __init__(self, master):
        ctk.CTkToplevel.__init__(self)
        
        ### main app
        self.first_name = tk.StringVar(value='', name='first_name')
        self.last_name = tk.StringVar(value='', name='last_name')
        self.person_title = tk.StringVar(value='', name='title')
        self.age = tk.IntVar(value=0, name='age')
        self.gender = tk.StringVar(value='', name='gender')
        self.nationality = tk.StringVar(value='', name='nationality')
        self.registration = tk.StringVar(value='0', name='registration')
        self.num_courses = tk.IntVar(value='', name='num_courses')
        self.num_semester = tk.IntVar(value='', name='num_semesters')
        self.terms_variable = tk.StringVar(value='0', name='terms_variable')
        self.database_id = tk.IntVar(value='', name='database_id')
        



class LogIn(PasswordManager):
    def __init__(self):
        super().__init__()

        
        self.title('Data entry form | Log In')
        self.frame = ctk.CTkFrame(self.master,
                                  width=200,
                                  height=200,
                                  corner_radius=10)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        ### user name
        user_label = ctk.CTkLabel(master=self.frame,
                                       text='User name',
                                       corner_radius=8)
        user_label.grid(row=0, column=0)
        user_name = ctk.CTkEntry(master=self.frame,
                                       textvariable=self.name,
                                       width=120,
                                       height=25,
                                       border_width=2,
                                       corner_radius=10)
        user_name.grid(row=1, column=0)

        ### password
        password_label = ctk.CTkLabel(master=self.frame,
                                       text='Password',
                                       corner_radius=8)
        password_label.grid(row=2, column=0)
        user_password = ctk.CTkEntry(master=self.frame,
                                          textvariable=self.password,
                                          width=120,
                                          height=25,
                                          border_width=2,
                                          show='*',
                                          corner_radius=10)
        user_password.grid(row=3, column=0)

        ### salt
        salt_label = ctk.CTkLabel(master=self.frame,
                                           text='Salsst',
                                           corner_radius=8)
        salt_label.grid(row=4, column=0)
        user_salt = ctk.CTkEntry(master=self.frame,
                                          textvariable=self.salt,
                                          width=120,
                                          height=25,
                                          border_width=2,
                                          show='$',
                                          corner_radius=10)
        user_salt.grid(row=5, column=0)

        ### pepper
        pepper_label = ctk.CTkLabel(master=self.frame,
                                       text='Pepper',
                                       corner_radius=8)
        pepper_label.grid(row=6, column=0)
        user_pepper = ctk.CTkEntry(master=self.frame,
                                      textvariable=self.pepper,
                                      width=120,
                                      height=25,
                                      border_width=2,
                                      show='#',
                                      corner_radius=10)
        user_pepper.grid(row=7, column=0)

        submit_button = ctk.CTkButton(master=self.frame,
                               text="Submit",
                               border_width=0,
                               corner_radius=8,
                               command=self.submit)
        submit_button.grid(row=8, column=0, padx=20, pady=20)


    def submit(self):
        #print(pbkdf2_hmac('sha256', self.user_password.get().encode('utf-8'), self.user_salt.get().encode('utf-8'), int(self.user_pepper.get())).hex())
        if self.password.get() != '1234':
            messagebox.showerror("Login failed", "Your login credentials are incorrect. Please try again.")
            #self.close_current_window()
        else:
            #self.newWindow = tk.Toplevel(self.master)
            self.app = MainApp(self)




class MainApp (PasswordManagerTopLevel):
    def __init__(self, master):
        super().__init__(master)


        self.title("Data entry form")
        self.frame = ctk.CTkFrame(self, corner_radius=10)
        self.frame.pack()

        ### save the user info
        self.user_info_frame = tk.LabelFrame(self.frame, text='User information')
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=20)


        ### first name label and entry
        self.first_name_label = ctk.CTkLabel(master=self.frame,
                                             text='First name',
                                             corner_radius=8)
        self.first_name_label.grid(row=0, column=0, padx=2, pady=2)
        self.user_name = ctk.CTkEntry(master=self.frame,
                                      textvariable=self.first_name,
                                      border_width=2,
                                      corner_radius=10)
        self.user_name.grid(row=1, column=0, padx=2, pady=2)

        ### last name label and entry
        self.last_name_label = ctk.CTkLabel(master=self.frame,
                                             text='Last name',
                                             corner_radius=8)
        self.last_name_label.grid(row=0, column=1, padx=2, pady=2)
        self.last_name = ctk.CTkEntry(master=self.frame,
                                      textvariable=self.last_name,
                                      border_width=2,
                                      corner_radius=10)
        self.last_name.grid(row=1, column=1, padx=2, pady=2)

        ### person's title label and entry
        self.title_label = ctk.CTkLabel(master=self.frame,
                                             text='Title',
                                             corner_radius=8)
        self.title_label.grid(row=0, column=2, padx=2, pady=2)
        self.title = ctk.CTkComboBox(master=self.frame,
                                     values=['', 'Mr.', 'Mrs.', 'Miss', 'Dr.'],
                                     variable=self.person_title)
        self.title.grid(row=1, column=2, padx=2, pady=2)
        self.title.set('')


        ### age label and entry
        def get_age_current_value(self):
            return self.age.get()

        def age_slider_changed():
            self.age_label.configure(text=f'Age: {get_age_current_value()}')

        age = ctk.CTkSlider(master=self.frame, from_=12, to=18, variable=self.age, number_of_steps=6, command=age_slider_changed)
        age.grid(row=3, column=0, padx=2, pady=2)

        self.age_label = ctk.CTkLabel(master=self.frame,
                                      text=f'Age: {"NA"}',
                                      corner_radius=8)
        self.age_label.grid(row=2, column=0, padx=2, pady=2)


        self.gender_label = ctk.CTkLabel(master=self.frame,
                                        text='Gender',
                                        corner_radius=8)
        self.gender_label.grid(row=2, column=1, padx=2, pady=2)



        female_gender = ctk.CTkRadioButton(master=self.frame, text="Female", variable=self.gender, value='Female')
        male_gender = ctk.CTkRadioButton(master=self.frame, text="Male", variable=self.gender, value='Male')

        female_gender.grid(row=3, column=1, padx=2, pady=2)
        male_gender.grid(row=4, column=1, padx=2, pady=2)


        self.quit_button = ctk.CTkButton(master=self.frame,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Quit",
                                 command=self.close_windows)
        self.quit_button.grid(row=999, column=0)

        def print_age(var):
            print(var.get())

        self.save_button = ctk.CTkButton(master=self.frame,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Save",
                                 command=lambda: print_age(self.gender))
        self.save_button.grid(row=999, column=1)


    def close_windows(self):
        self.destroy()
