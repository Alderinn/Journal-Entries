"""
#00c4ff 
#004155
#0083aa

"""

import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("600x400")
        self.grid_columnconfigure((0, 1), weight=1)
        self.label = ctk.CTkLabel(
            self, 
            text='Journal Entries', 
            fg_color='transparent',
            justify='center',
            font=("",48)
            )
        self.label.grid(row=0,column=0, padx=20,pady=20, sticky='ew', columnspan=2)

        # Today's Entry
        self.button = ctk.CTkButton(self, text="Today's Entry", command=self.entriesPage, width=160, height=40, fg_color='#0083aa')
        self.button.grid(row=1, column=0, padx=20, pady=5, columnspan=2)
        # Entry Search
        self.button = ctk.CTkButton(self, text="Entry Search", command=self.entriesPage, width=160, height=40, fg_color='#004155')
        self.button.grid(row=2, column=0, padx=20, pady=5, columnspan=2)
        # All Entries
        self.button = ctk.CTkButton(self, text="All Entries", command=self.entriesPage, width=160, height=40, fg_color='#004155')
        self.button.grid(row=3, column=0, padx=20, pady=5, columnspan=2)
        # EXIT
        self.button = ctk.CTkButton(self, text="EXIT", command=quit, width=80, height=20, fg_color='red')
        self.button.grid(row=4, column=0, padx=20, pady=5, columnspan=2)


    def entriesPage(self):
        print("button pressed")
        self.button = ctk.CTkButton(self, text="Submit", command=self.__init__)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

app = App()
app.mainloop()