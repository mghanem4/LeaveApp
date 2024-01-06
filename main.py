import tkinter as tk
from typing import Optional, Tuple, Union
import customtkinter as ctk 
from msac import * 
from tkcalendar import Calendar, DateEntry
from datetime import datetime 
import time
from PIL import Image, ImageTk
import os


# msac.py is a file that manages database and data inputs, it checks whether 
#the password and username are true before taking users into the next desired page



file_path= os.path.dirname(os.path.realpath(__file__))
	
# Screen size variables:
root=ctk.CTk()
rootwidth=root.winfo_screenwidth()
rootheight=root.winfo_screenheight()


# Some global constants for fonts

LARGEFONT =("Arial", 35)
MEDFONT= ("Arial", 22)
NORMALFONT= ("Arial", 16)
SMALLFONT = ("Arial", 9)




class GuiApp(ctk.CTk):
	
	# __init__ function for class tkinterApp 
	def __init__(self): 
		
		# __init__ function for class Tk
		ctk.CTk.__init__(self)
		

		self.geometry(f"{rootwidth}x{rootheight}")

		container = ctk.CTkFrame(self) 
		container.pack() 

		# initializing frames to an empty array
		self.pages = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (EmployeeLogin,EmployeeFormScreen):

			page = F(container, self)
			self.pages[F] = page 

			page.grid(row = 0, column = 0, sticky ="nsew")
		self.protocol("WM_DELETE_WINDOW", self.on_closing)

		self.switch_page(EmployeeLogin)

# Adding a function to manage closing the app with a pop up dialog
# This serves two purposes, it is useful in real life applications, and it stops the program from running in the background whenever the GUI is closed.
		
	def on_closing(self):
		message_box= ctk.CTkToplevel()
		message_box.geometry("300x100")
		message_box.title("Quit")
		message_box.resizable(False, False)
		message_box.grab_set()
		message_box.focus_set()
		message_box.grab_release()
		message_box.protocol("WM_DELETE_WINDOW", message_box.destroy)
		message_box_label= ctk.CTkLabel(message_box, text="Are you sure you want to quit?")
		message_box_label.pack(padx=10, pady=10)
		msg_quit_btn= ctk.CTkButton(message_box, text="Yes", command=self.destroy and self.quit_app)
		msg_quit_btn.pack(side=tk.LEFT,padx= 5)
		msg_not_quit_btn= ctk.CTkButton(message_box, text="No", command=message_box.destroy)
		msg_not_quit_btn.pack(side=tk.LEFT, padx= 5)
		message_box.mainloop()
		
	def quit_app(self):
		self.destroy()
		exit()
		

	# to display the current frame passed as
	# parameter
	def switch_page(self, frame):
		page = self.pages[frame]
		page.tkraise()


		


# Employee Login Page
class EmployeeLogin(ctk.CTkFrame):
	def __init__(self, parent, controller):
		ctk.CTkFrame.__init__(self, parent, width= rootwidth, height=rootheight)

		welc_page_frame= ctk.CTkFrame(self, width=rootwidth, height=rootwidth)
		self.title= ctk.CTkLabel(welc_page_frame,text="Welcome",font=LARGEFONT)
		self.title.grid(row= 1, column= 5)
		self.username_entry= ctk.CTkEntry(welc_page_frame, 
		width=400,height=50,font=MEDFONT,
		placeholder_text=("Username"))
		self.username_entry.grid(row= 4, column= 5, padx= 10, pady=10)
		self.password_entry = ctk.CTkEntry(welc_page_frame,width=400,height=50,font=MEDFONT,
		placeholder_text=("Password"), show="*")
		self.password_entry.grid(row= 6, column= 5, padx= 10, pady=10)
		self.login_btn= ctk.CTkButton(welc_page_frame,width=280,height=48,corner_radius=20,
		hover_color=("Light Blue", "Blue") ,text="Login", font=NORMALFONT, command= lambda: self.credentials_checker(controller))
		self.login_btn.grid(row= 8, column= 5)
		welc_page_frame.place(in_=self, anchor="c", relx=.5, rely=.5)

		




# Check the password and username of the login, if true switch to page ()		
	def credentials_checker(self,controller): 
		
		username = self.username_entry.get()
		password = self.password_entry.get()
		
		if creds_checker(username, password)== True:
			controller.switch_page(EmployeeFormScreen)
			self.username_entry.delete(0,"end")
			self.password_entry.delete(0,"end")
			print("Login successful")
		else:
			print("Login failed")
			self.username_entry.delete(0,"end")
			self.password_entry.delete(0,"end")
			failed_message_box= ctk.CTkToplevel()
			failed_message_box.geometry("300x100")
			failed_message_box.title("Quit")
			failed_message_box.resizable(False, False)
			failed_message_box.grab_set()
			failed_message_box.focus_set()
			failed_message_box.grab_release()
			failed_message_box.protocol("WM_DELETE_WINDOW", failed_message_box.destroy)
			failed_message_box_label= ctk.CTkLabel(failed_message_box, text="Incorrect Username or Password")
			failed_message_box_label.pack(padx=10, pady=10)
			msg_quit_btn= ctk.CTkButton(failed_message_box, text="Ok", command= lambda: failed_message_box.destroy())
			msg_quit_btn.pack()
			failed_message_box.mainloop()


			

    
class EmployeeFormScreen(ctk.CTkFrame):
	def __init__(self,parent,controller):
		ctk.CTkFrame.__init__(self,parent)
# -----------------------Back Button and Frame------------------------
		self.back_btn_frame= ctk.CTkFrame(self)
		self.back_btn= ctk.CTkButton(self.back_btn_frame, text="Back", command=lambda: controller.switch_page(EmployeeLogin))
		self.back_btn.grid(row=0, column = 0 ,padx=10, pady=10)
		self.back_btn_frame.grid(row= 0, column= 0,padx= 10, sticky="w")

# -----------------------Title and Progress Bar Frame------------------------

		self.title= ctk.CTkLabel( self,text=f"Leave Form",font=LARGEFONT)
		self.title.grid(row = 0, column = 10, padx = 10, pady = 10, sticky="")
		self.progress_bar_frame= ctk.CTkFrame(self)

		self.progression_bar(self.progress_bar_frame)
		self.progress_bar_frame.grid(row= 2, column= 0,padx= 10, sticky="w")

		self.form_frame= ctk.CTkFrame(self)
		self.name_field(self.form_frame)
		self.email_field(self.form_frame)
		self.reason_field(self.form_frame)
		self.start_date_field(self.form_frame)
		self.end_date_field(self.form_frame)
		self.leave_type_field(self.form_frame)
		self.total_leave_hours(self.form_frame)
		self.submit_form_btn(self.form_frame)
		self.form_frame.place(in_=self, anchor="c", relx=.5, rely=.5)
		self.form_frame.grid_columnconfigure(0, weight=1)
		self.form_frame.grid_rowconfigure(0, weight=1)


# -----------------------Functions------------------------

	def progression_bar(self, frame):
		self.formprogress_label= ctk.CTkLabel(frame, text="Form Progress",font=NORMALFONT)
		self.formprogress_label.grid(row=2, column=1, padx=5, pady=5)
		self.formprogress= ctk.CTkProgressBar(frame, orientation="horizontal",progress_color=("blue","orange"),border_color="gray",determinate_speed= 1)
		self.formprogress.grid(row=2, column=2, padx=10, pady=10)

	

	def name_field(self,frame):
		self.name_label= ctk.CTkLabel(frame,text="First and Last Name", font=MEDFONT)
		self.name_label.grid(row=0, column=2, padx=5, pady=5)
		self.name_entry= ctk.CTkEntry(frame,placeholder_text="Please enter your full Name",font=MEDFONT)
		self.name_entry.grid(row=0, column=4, padx=5, pady=5)

	
	def email_field(self,frame):
		self.email_label= ctk.CTkLabel(frame,text="Email", font=MEDFONT)
		self.email_label.grid(row=2, column=2, padx=5, pady=5)
		self.email_entry= ctk.CTkEntry(frame,placeholder_text="Please enter your email",font=MEDFONT)
		self.email_entry.grid(row=2, column=4, padx=5, pady=5)

 
	
	def reason_field(self, frame):
		self.reason_entry_label= ctk.CTkLabel(frame,text="Reason of Leave", font=MEDFONT, width= 20)
		self.reason_entry_label.grid(row=4, column=2, padx=5, pady=5)
		self.reason_entry= ctk.CTkEntry(frame,placeholder_text="Reason",font=MEDFONT)
		self.reason_entry.grid(row=4, column=4, padx=5, pady=5)
		if len(self.reason_entry.get()) > 0:
			self.formprogress.step()

	def start_date_field(self, frame):
		self.start_date_label= ctk.CTkLabel(frame,text="Start Date", font=MEDFONT)
		self.start_date_label.grid(row=6, column=2, padx=5, pady=5)
		self.start_date_entry= DateEntry(frame,height=3 ,width=7, background='darkblue',
                    foreground='white', borderwidth=2, font=MEDFONT)
		self.start_date_entry.configure(state='normal')
		self.start_date_entry.bind("<<DateEntrySelected>>",  self.calc_total_hours)
		self.start_date_entry.grid(row=6, column=4, padx=5, pady=5)
		
	def end_date_field(self, frame):
		self.end_date_label= ctk.CTkLabel(frame, text="End Date (Optional)", font= MEDFONT)
		self.end_date_label.grid(row=8, column=2, padx=5, pady=5)
		self.end_date_entry= DateEntry(frame,height=3 ,width=7, background='darkblue',
                    foreground='white', borderwidth=2, font=MEDFONT)
		self.end_date_entry.grid(row=8, column=4, padx=5, pady=5)
		self.end_date_entry.configure(state='normal')
		self.end_date_entry.bind("<<DateEntrySelected>>",  self.calc_total_hours)


	def leave_type_field(self, frame):
		self.leave_type_label= ctk.CTkLabel(frame, text="Leave Type", font= MEDFONT)
		self.leave_type_label.grid(row=10, column=2, padx=5, pady=5)
		
		self.leave_type_entry= ctk.CTkOptionMenu(frame,font=MEDFONT,values=["Annual","Sick","Bereavement","Other"],
		hover=True,dropdown_hover_color="blue",button_hover_color="light gray"
		,dynamic_resizing=True, anchor="center", corner_radius=20)
		get_value= self.leave_type_entry.get()
		self.leave_type_entry.set("Please choose a leave type")
		self.leave_type_entry.bind("<<OptionMenuSelected>>",  lambda event: self.formprogress.step())
		self.leave_type_entry.grid(row=10, column=4, padx=5, pady=5)

	def submit_form_btn(self,frame):

		submit_btn= ctk.CTkButton(frame, width=250, height=40,text="Submit Leave",corner_radius=20, command= self.get_form)
		submit_btn.grid(row=18, column=3, padx=5, pady=5)

	def total_leave_hours(self,frame):

		self.total_hours_label= ctk.CTkLabel(frame, text="Total Hours", font=MEDFONT)
		self.total_hours_label.grid(row=12, column=2, padx=5, pady=5)
		self.total_hours_box= ctk.CTkLabel(frame,text="Please select dates",font=MEDFONT,state="disabled")
		
		self.total_hours_box.grid(row=12, column=4, padx=5, pady=5)

	def calc_total_hours(self,event):
		self.start_dt= self.start_date_entry.get_date()
		self.end_dt= self.end_date_entry.get_date()
		self.total_hours= (self.end_dt - self.start_dt).days
		self.total_hours= (self.total_hours+1) * 7
		if self.total_hours >= 0:
			self.total_hours_box.configure(text= self.total_hours)
		else:
			self.total_hours_box.configure(text="Please select dates")


	def get_form(self):
		self.name= self.name_entry.get()
		self.email= self.email_entry.get()
		self.reason= self.reason_entry.get()
		self.start_dt=self.start_date_entry.get_date()
		self.end_dt=self.end_date_entry.get_date()
		print(self.start_date_entry)
		print(self.end_date_entry)
		self.leave_type= self.leave_type_entry.get()
		leave_values=["Annual","Sick","Bereavement","Other"]

#------------------Date validation block--------------------
		leave_type_validation=self.leave_type in leave_values
		if self.start_dt== self.end_dt:
			dte_validation= True
		elif self.start_dt < self.end_dt:
			dte_validation= True
		else:
			dte_validation= False

		str_reason_validation= len(self.reason) > 1
		name_validation= len(self.name) > 0

#-----------------Email validation block---------------------
		if "@" and".com" in self.email:
			email_validation= True
		else:
			email_validation= False
#-----------------Form validation block-----------------------
		if (str_reason_validation) and (dte_validation) and (leave_type_validation) and name_validation and email_validation:
			form_insert(self.name , self.email , self.reason ,self.start_dt ,self.end_dt ,self.leave_type ,self.total_hours )
			self.form_success()
			self.clear_form()
		else:
			self.form_validation()

	def form_validation(self):
			form_validation_msg= ctk.CTkToplevel()
			form_validation_msg.geometry("300x100")
			form_validation_msg.title("Form Validation Error")
			form_validation_msg.resizable(False, False)
			form_validation_msg.grab_set()
			form_validation_msg.focus_set()
			form_validation_msg.grab_release()
			form_validation_msg.protocol("WM_DELETE_WINDOW", form_validation_msg.destroy)
			form_validation_msg_label= ctk.CTkLabel(form_validation_msg, text="There are errors in the form",text_color="red")
			form_validation_msg_label.pack(padx=10, pady=10)
			msg_quit_btn= ctk.CTkButton(form_validation_msg, text="Ok", command= lambda: form_validation_msg.destroy())
			msg_quit_btn.pack()
			form_validation_msg.mainloop()

	def form_success(self):
			form_success_msg= ctk.CTkToplevel()
			form_success_msg.geometry("300x100")
			form_success_msg.title("Form Submitted")
			form_success_msg.resizable(False, False)
			form_success_msg.grab_set()
			form_success_msg.focus_set()
			form_success_msg.grab_release()
			form_success_msg.protocol("WM_DELETE_WINDOW", form_success_msg.destroy)
			form_success_msg_label= ctk.CTkLabel(form_success_msg, text="Form submitted successfully, thank you!")
			form_success_msg_label.pack(padx=10, pady=10)
			msg_quit_btn= ctk.CTkButton(form_success_msg, text="Ok", command= lambda: form_success_msg.destroy())
			msg_quit_btn.pack()
			form_success_msg.mainloop()
	def clear_form(self):
		self.name_entry.delete(0,tk.END)
		self.email_entry.delete(0,tk.END)
		self.reason_entry.delete(0,tk.END)
		self.start_date_entry.set_date(datetime.today())
		self.end_date_entry.set_date(datetime.today())
		self.leave_type_entry.set("Please choose a leave type")
		self.total_hours_box.configure(text="Please select dates")
		self.formprogress.step(-100)
		



# Driver Code
if __name__ =="__main__":
    app = GuiApp()
    app.mainloop()

	