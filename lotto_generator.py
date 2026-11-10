import random
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Lotto Number Generator")
        self.geometry("800x600")
        self.minsize(600, 400)

        # Configure grid layout (1 row, 2 columns for a sidebar layout)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Sidebar Frame ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=0)

        #sidebar for buttons
        self.sidebar_title = ctk.CTkLabel(
            self.sidebar_frame,
            text="Navigation",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.sidebar_title.grid(row=0, column=0, padx=20, pady=20)

        #buttons for each game
        self.btn_1 = ctk.CTkButton(
            self.sidebar_frame, text="Powerball", command=self.Powerball_pressed
        )
        self.btn_1.grid(row=1, column=0, padx=10, pady=10)

        self.btn_2 = ctk.CTkButton(
            self.sidebar_frame, text="Multi-Match", command=self.Multi_Match_pressed
        )
        self.btn_2.grid(row=2, column=0, padx=10, pady=10)

        self.btn_3 = ctk.CTkButton(
            self.sidebar_frame, text="Mega Millions", command=self.Mega_Millions_pressed
        )
        self.btn_3.grid(row=3, column=0, padx=10, pady=10)

        self.btn_4 = ctk.CTkButton(
            self.sidebar_frame, text="Pick5", command=self.Pick5_Pressed
        )
        self.btn_4.grid(row=4, column=0, padx=10, pady=10)

        # Theme Switcher at the bottom of sidebar
        self.appearance_mode_label = ctk.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_callback,
        )
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(10, 20))
        self.appearance_mode_menu.set("System")

        # --- Main Content Frame ---
        self.main_frame = ctk.CTkFrame(
            self, corner_radius=10, fg_color="transparent"
        )
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0,weight=1)

        self.main_title = ctk.CTkLabel(
            self.main_frame,
            text="Multi Lottery Number Generator",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.main_title.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.main_number_display = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color="transparent",
            width=400,
            height=400,
        )
        self.main_number_display.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")


    # --- Callbacks / Event Handlers ---
    def clear_display(self): # clear display before generating numbers
        for widget in self.main_number_display.winfo_children():
            widget.destroy()

    def Powerball_pressed(self): # picks 5 numbers from 1-75 and a power play ball from 1-26
        self.clear_display()
        for i in range(1,28):
            main_nums = random.sample(range(1,75),5)
            power_play = random.randint(1,26)

            text = "  ".join(f"{num:02d}" for num in main_nums)
            final_text = f"Ticket {i}:   {text}   |   [ PB: {power_play:02d} ]"

            row_label = ctk.CTkLabel(
                self.main_number_display,
                text=final_text,
                font=ctk.CTkFont(family="Serif", size=18, weight="bold") # Courier matches widths evenly
                )
            row_label.pack(anchor="w",padx=20,pady=5)

    def Multi_Match_pressed(self):
        self.clear_display()
        for i in range(1,4):
            for j in range(1,4):
                main_nums = random.sample(range(1,43),6)
            
                text = "  ".join(f"{num:02d}" for num in main_nums)
                final_text = f"line {j}:   {text}"
                
                row_label = ctk.CTkLabel(
                    self.main_number_display,
                    text=final_text,
                    font=ctk.CTkFont(family="Serif", size=18, weight="bold") # Courier matches widths evenly
                    )
                row_label.pack(anchor="w",padx=20,pady=5)

            if i < 3:
                line_break = ctk.CTkLabel(
                    self.main_number_display,
                    text="------------------------------------------------------",
                    font=ctk.CTkFont(family="Serif", size=18, weight="bold"),
                )
                line_break.pack(anchor="w",padx=20,pady=5)


    def Mega_Millions_pressed(self):
        self.clear_display()
        for i in range(1,28):
            main_nums = random.sample(range(1,70),5)
            mega_ball = random.randint(1,24)
        
            text = "  ".join(f"{num:02d}" for num in main_nums)
            final_text = f"Ticket {i}: {text} | Mega Ball: {mega_ball:02d}"
        
            row_label = ctk.CTkLabel(
                self.main_number_display,
                text=final_text,
                font=ctk.CTkFont(family="Serif", size=18, weight="bold") # Courier matches widths evenly
                )
            row_label.pack(anchor="w",padx=20,pady=5)

    def Pick5_Pressed(self):
        self.clear_display()
        for i in range(1,6):
            main_nums = random.sample(range(1,9),5)
            text = " ".join(f"{num}" for num in main_nums)
            final_text = f"Ticket {i}: {text}"
                
            row_label = ctk.CTkLabel(
                self.main_number_display,
                text=final_text,
                font=ctk.CTkFont(family="Serif", size=18, weight="bold") # Courier matches widths evenly
            )
            row_label.pack(anchor="w",padx=20,pady=5)

    def change_appearance_mode_callback(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)



if __name__ == "__main__":
    app = App()
    app.mainloop()