from CTkMessagebox import CTkMessagebox
import customtkinter

# Constants for the GUI
HEX_GREEN = "#009579"
HEX_GREEN_HOVER = "#006e59"

def show_info():
    # Default messagebox for showing some information
    CTkMessagebox(title="Info", message="This is a CTkMessagebox!",
                  bg_color="white",
                  fg_color="white",
                  text_color="black",
                  button_hover_color=HEX_GREEN_HOVER,
                  button_color=HEX_GREEN,
                  font=("Poppins", 14),
                  header=True)


def show_checkmark():
    # Show some positive message with the checkmark icon
    CTkMessagebox(message="Authentication successful.",
                  icon="check", option_1="OK",
                  bg_color="white",
                  fg_color="white",
                  text_color="black",
                  button_hover_color=HEX_GREEN_HOVER,
                  button_color=HEX_GREEN,
                  font=("Poppins", 14),
                  header=True)


def show_error():
    # Show some error message
    CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel",
                  bg_color="white",
                  fg_color="white",
                  text_color="black",
                  button_hover_color=HEX_GREEN_HOVER,
                  button_color=HEX_GREEN,
                  font=("Poppins", 14),
                  header=True)



def show_warning():
    # Show some retry/cancel warnings
    msg = CTkMessagebox(title="Warning Message!", message="Unable to connect!",
                        icon="warning", option_1="Cancel", option_2="Retry",
                        bg_color="white",
                        fg_color="white",
                        text_color="black",
                        button_hover_color=HEX_GREEN_HOVER,
                        button_color=HEX_GREEN,
                        font=("Poppins", 14),
                        header=True)


    if msg.get() == "Retry":
        show_warning()


def ask_question():
    # get yes/no answers
    msg = CTkMessagebox(title="Exit?", message="Do you want to close the setup?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes",
                        bg_color="white",
                        fg_color="white",
                        text_color= "black",
                        button_hover_color=HEX_GREEN_HOVER,
                        button_color=HEX_GREEN,
                        font=("Poppins", 14),
                        header=True)
    response = msg.get()

    if response == "Yes":
        app.destroy()
    else:
        print("Click 'Yes' to exit!")


app = customtkinter.CTk()
app.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
app.columnconfigure(0, weight=1)
app.minsize(200, 250)


customtkinter.CTkLabel(app, text="CTk Messagebox Examples").grid(padx=20)
customtkinter.CTkButton(app, text="Check CTkMessagebox", command=show_checkmark).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Info", command=show_info).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Error", command=show_error).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Warning", command=show_warning).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Ask Question", command=ask_question).grid(padx=20, pady=(10, 20), sticky="news")

app.mainloop()