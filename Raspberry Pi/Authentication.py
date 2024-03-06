import tkinter
import customtkinter


# Function for sending button input to authentication API
def send_input():

    input_text = entry.get()
    if input_text:  # Check if input_text is not empty
        print(input_text)
    else:
        print("Please enter a non-blank input.")

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
app.attributes("-topmost", True)

frame = customtkinter.CTkFrame(app,
                               fg_color="white")
frame.pack(fill="both", expand=True, padx=10, pady=10)

element_frame = customtkinter.CTkFrame(master= frame,
                                       fg_color="transparent"
                                       )
element_frame.pack(fill= "both",
                   expand= True,
                   padx = 10,
                   pady= 10)
element_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master= element_frame,
                               text="Please enter your authentication token below:",
                               fg_color="transparent",
                               font=("Poppins", 14),
                               text_color="black",
                               wraplength=200)
label.place(relx = 0.5,
            rely= 0.3,
            anchor= tkinter.CENTER)

entry = customtkinter.CTkEntry(master=element_frame,
                               width=150,
                               height=30,
                               bg_color="white",
                               corner_radius=10,
                               font=("Poppins", 12),
                               placeholder_text="Authentication Token",
                               placeholder_text_color="grey")
entry.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=element_frame,
                                 width=50,
                                 corner_radius=15,
                                 text="Send",
                                 font=("Poppins", 14),
                                 command=send_input,
                                 fg_color=hex_green,
                                 text_color="white",
                                 hover_color=hex_green_hover)

button.place(relx= 0.5,
             rely= 0.8,
             anchor=tkinter.CENTER)

app.mainloop()
