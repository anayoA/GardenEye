import tkinter
import CTkMessagebox as msgbox
import customtkinter
import requests
from PIL import Image

# from PlantReader import *

# Constants for the GUI
HEX_GREEN = "#009579"
HEX_GREEN_HOVER = "#006e59"
POPPINS = "/fonts/Poppins-Regular.otf"


valid_credentials = {}


def create_warning(title, message):
    return msgbox.CTkMessagebox(title=title, message=message,
                                icon="warning",
                                option_1="OK",
                                bg_color="white",
                                fg_color="white",
                                text_color="black",
                                button_hover_color=HEX_GREEN_HOVER,
                                button_color=HEX_GREEN,
                                font=("Poppins", 14),
                                header=True)


def input_warning():
    return create_warning("Alert", "Error: No input.")


def auth_warning(message):
    return create_warning("Alert", f"Authentication failed: {message}")


def auth_success(message):
    popup = msgbox.CTkMessagebox(title="Success",
                                 message=message,
                                 icon="check",
                                 option_1="OK",
                                 bg_color="white",
                                 fg_color="white",
                                 text_color="black",
                                 button_hover_color=HEX_GREEN_HOVER,
                                 button_color=HEX_GREEN,
                                 font=("Poppins", 14),
                                 header=True)
    response = popup.get()
    if response:
        print(f"reponse: {valid_credentials}")

        # read_data()
        # send_data()


def authenticate(username, token):
    # API endpoint for authentication
    auth_endpoint = "http://localhost/gardeneye/api/authentication/authenticateUser.php"

    # Parameters for the authentication request
    params = {
        "username": username,
        "token": token

    }

    try:
        response = requests.get(auth_endpoint, params)
        data = response.json()

        if data["success"]:
            print("authenticate():", data["message"])
            auth_success(data["message"])
            return username, token
        else:
            print("Authentication failed:", data["message"])
            auth_warning(data["message"])
            return False
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return False


# Function for sending button input to authentication API
def send_input():
    token = token_entry.get()
    username = username_entry.get()

    token_entry.delete(0, "end")  # Clears entry from text box
    username_entry.delete(0, "end")  # Clears entry from text box

    if token and username:  # Check if input_text is not empty
        print(f"send_input(): {username} + {token}")
        valid_user, valid_token = authenticate(username, token)
        print(f"if token and username: {valid_user},{valid_token}")
        if valid_user and valid_token:
            valid_credentials["username"] = valid_user
            valid_credentials["token"] = valid_token
            print(f'if valid_user and valid_token: {valid_credentials}')
    else:
        print("Please enter a non-blank input.")
        input_warning()


# Selecting GUI theme - dark, light , system (for system default)
customtkinter.set_appearance_mode("light")

# GUI window setup. Contains all the elements you see in the window.
app = customtkinter.CTk(fg_color=HEX_GREEN)
app.geometry("300x400")
app.title("GardenEye Setup")
app.resizable(0, 0)
app.eval('tk::PlaceWindow . center')
app.attributes("-topmost", True)

# GUI Embedded Fonts
poppins12 = customtkinter.CTkFont(family="Poppins", size=16, weight="normal")

frame = customtkinter.CTkFrame(master=app,
                               fg_color="white")
frame.pack(fill="both",
           expand=True,
           padx=10,
           pady=10)

element_frame = customtkinter.CTkFrame(master=frame,
                                       fg_color="transparent")
element_frame.pack(fill="both",
                   expand=True,
                   padx=10,
                   pady=10)
element_frame.place(relx=0.5,
                    rely=0.8,
                    anchor=tkinter.S)

label = customtkinter.CTkLabel(master=element_frame,
                               text="Please enter your details below:",
                               fg_color="transparent",
                               font=("Poppins", 16),
                               text_color="black",
                               wraplength=200)
label.place(relx=0.5,
            rely=0.25,
            anchor=tkinter.CENTER)

token_entry = customtkinter.CTkEntry(master=element_frame,
                                     width=150,
                                     height=30,
                                     bg_color="white",
                                     corner_radius=10,
                                     font=("Poppins", 12),
                                     placeholder_text="Authentication Token",
                                     placeholder_text_color="grey")
token_entry.place(relx=0.5,
                  rely=0.7,
                  anchor=tkinter.CENTER)

username_entry = customtkinter.CTkEntry(master=element_frame,
                                        width=150,
                                        height=30,
                                        bg_color="white",
                                        corner_radius=10,
                                        font=("Poppins", 12),
                                        placeholder_text="Username",
                                        placeholder_text_color="grey")
username_entry.place(relx=0.5,
                     rely=0.5,
                     anchor=tkinter.CENTER)

# Send button
button = customtkinter.CTkButton(master=element_frame,
                                 width=50,
                                 corner_radius=15,
                                 text="Send",
                                 font=("Poppins", 14),
                                 command=send_input,
                                 fg_color=HEX_GREEN,
                                 text_color="white",
                                 hover_color=HEX_GREEN_HOVER)

button.place(relx=0.5,
             rely=0.9,
             anchor=tkinter.CENTER)

# Logo image
logo = customtkinter.CTkImage(light_image=Image.open(
    r"files/Logo.png"),
    dark_image=Image.open(
        r"files/Logo.png"),
    size=(60, 60))
# Label to display the logo
logo_label = customtkinter.CTkLabel(master=frame,
                                    image=logo,
                                    text="",
                                    width=60,
                                    height=60,
                                    fg_color="transparent")
logo_label.place(relx=0.5,
                 rely=0.15,
                 anchor=tkinter.CENTER)


app.mainloop()
