from customtkinter import *
from CTkTable import CTkTable
# from date_li_borrow import *
from CTkXYFrame import *
from PIL import Image
import StartPageAdmin_baj 
import StartPageAdmin_use_baj
from  CTkMessagebox import CTkMessagebox
from SampleApp_baj import LoginPage
set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("blue.json")  # Themes: "blue" (standard), "green", "dark-blue"

class StartPageAdmin_Borrow(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        master.pack_propagate(0)
        master.geometry("856x645") 
        master.resizable(0,0)
        set_appearance_mode("light")

        self.sidebar_frame = CTkFrame(master=self, width=176, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        
        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}\\mode.png"), size=(20,20))
        CTkButton(master=self.sidebar_frame, width=5,image=button_image,text="", font=("Arial Bold", 14),  anchor="w",command=self.change_appearance_mode_event).pack(anchor="sw", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}\\receptionniste.png"), size=(100,100))
        CTkLabel(self.sidebar_frame,text="",image=button_image).pack(anchor="center", padx=5, pady=(16, 0))       
        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}\\hotel.png"), size=(16,16))

        
        CTkButton(master=self.sidebar_frame, image=button_image,text="Rooms", font=("Arial Bold", 14) ,anchor="w",command=self.to_Book).pack(anchor="center", padx=5, pady=(16, 0))
        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}\\profil.png"), size=(16, 16))

        CTkButton(master=self.sidebar_frame, text="Users", image=button_image, font=("Arial Bold", 14) , anchor="w",command=self.to_user).pack(anchor="center", padx=5, pady=(16, 0))
        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}\\service.png"), size=(20,20))

        CTkButton(master=self.sidebar_frame, text="Borrow", image=button_image, font=("Arial Bold", 14), anchor="w",command=self.to_now).pack(anchor="center", padx=5, pady=(16, 0))
        
        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}\\service.png"), size=(20,20))

                
        
        
        
        self.sidebar_frame.pack(anchor="w", side="left", fill="y", expand=True)

        self.main_view = CTkFrame(master=self, corner_radius=0, width=680, height=650)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.title_frame = CTkFrame(master=self.main_view, fg_color="transparent")
        self.title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        CTkLabel(master=self.title_frame, text="Borrow", font=("Arial Black", 25)).pack(anchor="nw", side="left")

        self.search_container = CTkFrame(master=self.main_view, height=50)
        self.search_container.pack(fill="x", pady=(45, 0), padx=27)
        
        CTkButton(master=self.title_frame, text="Borrow Book", font=("Arial Black", 15),command=self.Borrow_Book).pack(anchor="ne", side="right",padx=12)

        self.Search_Entry=CTkEntry(master=self.search_container, width=305 , border_width=2, placeholder_text="Search Book")
        self.Search_Entry.pack(side="left", padx=(13, 0), pady=15)

        CTkButton(master=self.search_container, text="Search", font=("Arial Black", 15),command=self.to_search).pack(anchor="ne",padx=13, pady=15)
        # connection=create_connection()
        self.table_data=[["Title","Room ID", "Author", "Publisher", "category"],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]
        self.table_frame = CTkXYFrame(master=self.main_view)
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data)#, header_color="#765827", hover_color="#B4B4B4")

        self.table.edit_row(0)
        self.table.pack(expand=True)
        self.main_view.pack(side="left", fill="both", expand=True)
        self.toplevel_window = None
    def change_appearance_mode_event(self):
        new_mode=get_appearance_mode()
        if new_mode=="Light":
            # LoginPage.newMode("Dark")
            set_appearance_mode("Dark")
        else:
            set_appearance_mode("Light")
            # LoginPage.newMode("Light")

    def to_user(self):
        self.master.switch_frame(StartPageAdmin_use_baj.StartPageAdmin_use)
    def to_Book(self):
        self.master.switch_frame(StartPageAdmin_baj.StartPageAdmin)
    def to_now(self):
        self.master.switch_frame(StartPageAdmin_Borrow)
    def to_search(self):
        pass
        # connection=create_connection()
        # self.tab=self.Search_Entry.get()
        # self.args1=search_borrow(connection,self.tab)
        # self.args2=select_all_borrows(connection)
        # index=[]
        # for value in  self.args2:
        #     if not value in  self.args1:
        #         index.append( self.args2.index(value))
        # self.table.delete_rows(index)
    # def select_and_search(self):
    #     connection=create_connection()
    #     self.text=self.Search_Entry.get()
    #     if self.text=="":
    #         return select_all_books(connection)
    #     else:
    #         return search_book(connection,self.text)
        
    def Borrow_Book(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindowBor_boo(self,self.master)  
            else:
                self.toplevel_window.focus() 
            
class ToplevelWindowBor_boo(CTkToplevel):
    def __init__(self,master, *args, **kwargs):
        self.master=master
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Borrow")
        self.geometry("550x160")
        self.resizable(width = False ,height = False)
        self.configure(bg='#fff')

        set_appearance_mode("light")

        self.title = CTkEntry(
            master=self,

            placeholder_text='ID User',
            width= 200,
            height=35,
        )
        self.Entry1 = CTkEntry(
            master=self,

            placeholder_text='ID Book',
            width= 200,
            height=35,
        )

        Button1 = CTkButton(
            master=self,
            text="New",
            font=("Arial Black", 15),
            text_color="white",
            hover= True,

            height=35,
            width= 200,
            border_width=2,
            corner_radius=4,
            command=self.new_
        )
        Button= CTkButton(
            master=self,
            text="Delete",
            font=("Arial Black", 15),
            text_color="white",
            hover= True,

            height=35,
            width= 200,
            border_width=2,
            corner_radius=4,
 

        command=self.dele
        )

        self.title.place(x= 18, y= 20)
        self.Entry1.place(x= 236, y= 20)
        Button1.place(x= 236, y= 110)
        Button.place(x= 18, y= 110)
    def dele(self):
            pass
            # connection=create_connection()
            # self.tes=self.Entry1.get()
            # delete_borrow(connection,self.tes)
            # self.destroy()
            # self.master.switch_frame(StartPageAdmin_Borrow)
    def new_(self):
            pass
            # connection=create_connection()
            # self.tes1=self.title.get()            
            # self.tes=self.Entry1.get()
            # insert_borrow(connection,self.tes1,self.tes)
            # self.destroy()
            # self.master.switch_frame(StartPageAdmin_Borrow)