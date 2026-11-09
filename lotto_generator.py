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
        self.grid_columnconfigure(1, weight=1)

        # --- Sidebar Frame ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(
            4, weight=1
        )  # Pushes bottom elements down

        self.sidebar_title = ctk.CTkLabel(
            self.sidebar_frame,
            text="Navigation",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.sidebar_title.grid(row=0, column=0, padx=20, pady=20)

        self.btn_1 = ctk.CTkButton(
            self.sidebar_frame, text="Powerball", command=self.Powerball_pressed
        )
        self.btn_1.grid(row=1, column=0, padx=20, pady=10)

        self.btn_2 = ctk.CTkButton(
            self.sidebar_frame, text="Multi-Match", command=self.Multi_Match_pressed
        )
        self.btn_2.grid(row=2, column=0, padx=20, pady=10)

        # unfinished buttons

        #self.btn_3 = ctk.CTkButton(
        #   self.sidebar_frame, text="Multi-Match", command=self.Multi_Match_pressed
        #)
        #self.btn_3.grid(row=2, column=0, padx=20, pady=10)

        #self.btn_4= ctk.CTkButton(
        #    self.sidebar_frame, text="Multi-Match", command=self.Multi_Match_pressed
        #)
        #self.btn_4.grid(row=2, column=0, padx=20, pady=10)

        

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

        self.main_title = ctk.CTkLabel(
            self.main_frame,
            text="Multi Lottery Number Generator",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        self.main_title.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.main_number_display = ctk.CTkLabel(
            self.main_frame,
            
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        self.main_number_display.grid(row=1, column=0, padx=20, pady=20, sticky="w")


    # --- Callbacks / Event Handlers ---
    def Powerball_pressed(self):
        main_nums = random.sample(range(1,75),5)
        power_play = random.randint(1,26)

        text = " ".join(map(str,main_nums))
        final_text = f"picks: {text} | Power Play: {power_play}"
        self.main_number_display.configure(text=final_text)

    def Multi_Match_pressed(self):
        main_nums = random.sample(range(1,75),5)
        power_play = random.randint(1,26)
        
        text = " ".join(map(str,main_nums))
        final_text = f"picks: {text} | Power Play: {power_play}"
        self.main_number_display.configure(text=final_text)
        
    def action_btn_callback(self):
        user_input = self.entry.get()
        print(f"User entered: {user_input}")

    def change_appearance_mode_callback(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)



if __name__ == "__main__":
    app = App()
    app.mainloop()