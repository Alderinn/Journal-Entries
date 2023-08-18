"""
#00c4ff 
#004155
#0083aa
"""
import customtkinter as ctk

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
        print("Made it")   

    def EntryPage(self):
        print('MADE IT')
        self.grid_columnconfigure((0,1), weight=1)

        self.textbox = ctk.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="ew",columnspan=2)
        self.textbox.insert("0.0", "")

        self.label2 = ctk.CTkLabel(master=self,text='Please enter your signature:')
        self.label2.grid(row=2,column=0,sticky='w',padx=10)

        self.entry = ctk.CTkEntry(master=self, width=350)
        self.entry.grid(row=3,column=0,padx=20,pady=5,sticky='ew',columnspan=2)

        self.button = ctk.CTkButton(self, text="Submit", command=self.Submit, width=160, height=40, fg_color='#004155')
        self.button.grid(row=4, column=0, padx=20, pady=5)
        self.button = ctk.CTkButton(self, text="Back", command=App, width=160, height=40, fg_color='#004155')
        self.button.grid(row=5, column=0, padx=20, pady=5)

    def Submit(self):
        print(self.textbox.get(str))





class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #Frame
        self.title("my app")
        self.geometry("600x400")
        
        self.grid_columnconfigure((0), weight=1)

        


        self.frame1 = MyFrame(self)
        self.frame1.grid(row=0, column=0, padx=10, pady=(0), sticky='nwes')


app = App()
app.mainloop()