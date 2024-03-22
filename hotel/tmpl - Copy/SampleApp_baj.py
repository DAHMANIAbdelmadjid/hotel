from tkinter import messagebox
from customtkinter import *
# from date_li_user import *
from PIL import Image
from CTkXYFrame import *
from  CTkMessagebox import CTkMessagebox
import StartPageAdmin_baj
import StartPageUSER_baj
import os
set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("blue.json")  # Themes: "blue" (standard), "green", "dark-blue"
class SampleApp(CTk):
    def __init__(self):
        CTk.__init__(self)
        self._frame = None

        self.geometry("600x480") 
        self.switch_frame(LoginPage)
        self.resizable(0,0)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class LoginPage(CTkFrame):
    
    def __init__(self, master):
        self.new_appearance_mode=get_appearance_mode()
        CTkFrame.__init__(self, master)
        set_appearance_mode(f"{self.new_appearance_mode}")

        side_img_data = Image.open(f"{os.path.dirname(__file__)}//imageHo.png")
        email_icon_data = Image.open(f"{os.path.dirname(__file__)}//side-img.png")
        password_icon_data = Image.open(f"{os.path.dirname(__file__)}//password-icon.png")

        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

        CTkLabel(master=self, text="", image=side_img).pack(expand=True, side="left")

        frame = CTkFrame(master=self, width=300, height=480)
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")
            
        
        CTkLabel(master=frame, text="welcome Back to!", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Sign in to your account", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Email :", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))

        self.username_entry = CTkEntry(master=frame, width=225, border_width=1)
        self.username_entry.pack(anchor="w", padx=(25, 0))
        CTkLabel(master=frame, text="  Password :", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))

        self.password_entry = CTkEntry(master=frame, width=225, border_width=1, show="*")
        self.password_entry.pack(anchor="w", padx=(25,0))

        self.login_button = CTkButton(master=frame, text="Login", font=("Arial Bold", 12), width=225)
        self.login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))
        self.login_button.bind("<Button-1>", self.check_login)
    def newMode(self,mode):
        self.mode=mode
        return self.mode
    def getMode(self):
        return self.mode
    def check_login(self,event):
            username = self.username_entry.get()
            password = self.password_entry.get()
            # connection=create_connection()
            user=[["Title","Room ID", "Author", "Publisher", "category"],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]
            f=0
            for i in user : 
                
                if username == i[-1] and password== i[0] and( i[1]in [1,2,3]):
                    f=1
                    self.master.switch_frame(StartPageAdmin_baj.StartPageAdmin)
                    break
                elif username == i[-1] and password == i[0]and (not i[1]in [1,2,3]): 
                    self.master.switch_frame(StartPageUSER_baj.StartPageUSER)
                    f=1
                if username =="1" :
                    f=1
                    self.master.switch_frame(StartPageAdmin_baj.StartPageAdmin)
                    break    

                if username =="2" :
                    f=1
                    self.master.switch_frame(StartPageUSER_baj.StartPageUSER)
                    break    
                        
            if f==0:
                messagebox.showerror("Error", "Invalid username or password")


if __name__ == "__main__":
   
    app = SampleApp()
    app.mainloop()
