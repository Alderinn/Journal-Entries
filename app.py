"""
#00c4ff 
#004155
#0083aa
"""
import customtkinter as ctk
from datetime import date
from journal import writeNewFile

class MyFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0), weight=1)
        self.label = ctk.CTkLabel(
            self,
            text='Journal Entries', 
            fg_color='transparent',
            font=("",48)
            )
        self.label.grid(row=0, column=0, padx=20, pady=(40,0), columnspan=2)
        
        # Today's Entry
        self.button = ctk.CTkButton(self, text="Today's Entry", command=self.WipePage, width=160, height=40, fg_color='#0083aa')
        self.button.grid(row=1, column=0, padx=20, pady=(50,0), columnspan=2)
        # Entry Search
        self.button = ctk.CTkButton(self, text="Entry Search", command=self.WipePage, width=160, height=40, fg_color='#004155')
        self.button.grid(row=2, column=0, padx=20, pady=5, columnspan=2)
        # All Entries
        self.button = ctk.CTkButton(self, text="All Entries", command=self.WipePage, width=160, height=40, fg_color='#004155')
        self.button.grid(row=3, column=0, padx=20, pady=5, columnspan=2)
        # EXIT
        self.button = ctk.CTkButton(self, text="EXIT", command=quit, width=80, height=20, fg_color='red')
        self.button.grid(row=4, column=0, padx=20, pady=(15,100), columnspan=2)

    def WipePage(self):
        print("button pressed")
        for widget in MyFrame.winfo_children(self):
            widget.destroy()
        self.EntryPage()

    def EntryPage(self):
        self.grid_columnconfigure((0,1), weight=1)

        # TITLE: How was your day?
        self.label3 = ctk.CTkLabel(master=self,text='How was your day?',font=("",36))
        self.label3.grid(row=0,column=0,sticky='w',padx=(10,0),pady=(5,0))
        
        # BODY TEXTBOX
        self.textbox = ctk.CTkTextbox(master=self, width=400, corner_radius=10)
        self.textbox.grid(row=1, column=0, sticky="ew",columnspan=2, padx=20,pady=20 )
        self.textbox.insert("0.0", "")

        # Rating
        self.rate = ctk.CTkComboBox(
            master=self, 
            values=['1','2','3','4','5']
            )
        self.rate.grid(row=3,column=0,sticky='w',padx=10)

        # Signature TEXT
        self.label2 = ctk.CTkLabel(master=self,text='Please enter your signature:')
        self.label2.grid(row=4,column=0,sticky='w',padx=10)

        # Signature ENTRY
        self.entry = ctk.CTkEntry(master=self, width=350)
        self.entry.grid(row=5,column=0,padx=20,pady=5,sticky='ew',columnspan=2)

        #SUBMIT BUTTON
        self.button = ctk.CTkButton(self, text="Submit", command=self.Submit, width=160, height=40, fg_color='#004155')
        self.button.grid(row=6, column=0, padx=20, pady=5)

        #BACK
        self.button = ctk.CTkButton(self, text="Back", command=App, width=160, height=40, fg_color='#004155')
        self.button.grid(row=7, column=0, padx=20, pady=5)

    def Submit(self):
        t = self.textbox.get("1.0",'end-1c')
        s = self.entry.get()
        r = self.rate.get()
        data = {
            'rate': 0,
            'desc':'',
            'date': '', # YYYY-MM-DD
            'signature': '',
            'time': ''
            }
        data['desc']=t
        data['signature']=s
        data['rate']=r
        data['date']="2023-08-17"
        todays_date = str(date.today())
      
        print(f"Entry was: {t}")
        print(f"Sig was: {s}")
        print(f"Rate is: {r}")
        writeNewFile(data)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
  
        #Frame
        self.title("my app")
        self.geometry("700x450")
        self.grid_columnconfigure((0), weight=1)
        self.frame1 = MyFrame(self)
        self.frame1.grid(row=0, column=0, padx=10, pady=(0), sticky='nwes')

app = App()
app.mainloop()