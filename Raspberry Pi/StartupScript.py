import tkinter

import customtkinter
import tkinter


# Function for sending button input to authentication API
def send_input():
    input_text = entry.get()


# Selecting GUI theme - dark, light , system (for system default)
customtkinter.set_appearance_mode("light")

# Colours for the GUI
hex_green = "#009579"
hex_green_hover = "#006e59"

app = customtkinter.CTk(fg_color=hex_green)
app.geometry("300x200")
app.title("GardenEye Setup")
app.resizable(0, 0)
app.eval('tk::PlaceWindow . center')

frame = customtkinter.CTkFrame(app,
                               bg_color=hex_green_hover,
                               )
frame.pack(fill="both", expand=True, padx=20, pady=20)

entry = customtkinter.CTkEntry(master=frame,
                               width=120,
                               height=30,
                               bg_color=hex_green_hover,
                               corner_radius=200)
entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=frame,
                                 width=50,
                                 corner_radius=200,
                                 text="Send",
                                 command=send_input(),

                                 fg_color=hex_green,
                                 hover_color=hex_green_hover)

button.pack(side="bottom",
            pady=50)

app.mainloop()
