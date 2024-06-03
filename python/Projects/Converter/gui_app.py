import tkinter
import customtkinter

def convert_function():
    print("Proceeding with calculation..")
    enteredNum = float(entry.get())
    itemFromFirstList = itemListOne.get()
    itemFromSecondList = itemListTwo.get()
    
    # I suck at this.. but at least my code is not AI generated
    # mm
    if itemFromFirstList == "mm" and itemFromSecondList == "mm":
        outputLabel.configure(text="Output: " + str(enteredNum) + "mm")

    if itemFromFirstList == "mm" and itemFromSecondList == "cm":
        outputLabel.configure(text="Output: " + str(enteredNum / 10) + "cm")

    if itemFromFirstList == "mm" and itemFromSecondList == "m":
        outputLabel.configure(text="Output: " + str(enteredNum / 1000) + "m")

    if itemFromFirstList == "mm" and itemFromSecondList == "km":
        outputLabel.configure(text="Output: " + str(enteredNum / 1000000) + "km")

    #cm
    if itemFromFirstList == "cm" and itemFromSecondList == "mm":
        outputLabel.configure(text="Output: " + str(enteredNum * 10) + "mm")

    if itemFromFirstList == "cm" and itemFromSecondList == "cm":
        outputLabel.configure(text="Output: " + str(enteredNum) + "cm")

    if itemFromFirstList == "cm" and itemFromSecondList == "m":
        outputLabel.configure(text="Output: " + str(enteredNum / 100) + "m")

    if itemFromFirstList == "cm" and itemFromSecondList == "km":
        outputLabel.configure(text="Output: " + str(enteredNum / 100000) + "km")

    #m
    if itemFromFirstList == "m" and itemFromSecondList == "mm":
        outputLabel.configure(text="Output: " + str(enteredNum * 1000) + "mm")

    if itemFromFirstList == "m" and itemFromSecondList == "cm":
        outputLabel.configure(text="Output: " + str(enteredNum * 10) + "cm")

    if itemFromFirstList == "m" and itemFromSecondList == "m":
        outputLabel.configure(text="Output: " + str(enteredNum) + "m")

    if itemFromFirstList == "m" and itemFromSecondList == "km":
        outputLabel.configure(text="Output: " + str(enteredNum / 1000) + "km")

    #km
    if itemFromFirstList == "km" and itemFromSecondList == "mm":
        outputLabel.configure(text="Output: " + str(enteredNum * 1000000) + "mm")

    if itemFromFirstList == "km" and itemFromSecondList == "cm":
        outputLabel.configure(text="Output: " + str(enteredNum * 100000) + "cm")

    if itemFromFirstList == "km" and itemFromSecondList == "m":
        outputLabel.configure(text="Output: " + str(enteredNum * 1000) + "m")

    if itemFromFirstList == "km" and itemFromSecondList == "km":
        outputLabel.configure(text="Output: " + str(enteredNum) + "km")

app = customtkinter.CTk()
app.geometry("500x500")
app.title("Converter")

customtkinter.set_appearance_mode("Dark") # if you use macOS, stop using it.
#----------------------------------------
label = customtkinter.CTkLabel(master=app,
                               text="Convert your stuff here!",
                               font=("Courier", 25),
                               )
label.place(relx=0.5, rely=0.07, anchor=tkinter.CENTER)
#----------------------------------------
entry = customtkinter.CTkEntry(master=app,
                               width=200,
                               height=15,
                               font=("Courier", 18),
                               )
entry.place(relx=0.33, rely=0.2, anchor=tkinter.CENTER)
#----------------------------------------
itemListOne = customtkinter.CTkComboBox(master=app,
                                    values=["mm","cm", "m", "km"],
                                    width=60,
                                    height=20
)
itemListOne.place(relx=0.77, rely=0.2, anchor=tkinter.CENTER)
#----------------------------------------
arrow = customtkinter.CTkLabel(master=app,
                               text="↓",
                               font=("Courier", 25),
                               )
arrow.place(relx=0.77, rely=0.26, anchor=tkinter.CENTER)
#----------------------------------------
itemListTwo = customtkinter.CTkComboBox(master=app,
                                    values=["mm","cm", "m", "km"],
                                    width=60,
                                    height=20
)
itemListTwo.place(relx=0.77, rely=0.34, anchor=tkinter.CENTER)
#----------------------------------------
convertButton = customtkinter.CTkButton(master=app, text="Calculate", font=("Ubuntu", 21), fg_color="#215dd3",command=convert_function) #bloated font btw
convertButton.place(relx=0.33, rely=0.32, anchor=customtkinter.CENTER)
#----------------------------------------
outputLabel = customtkinter.CTkLabel(master=app,
                               text="Output: ",
                               font=("Courier", 25),
                               fg_color="#333333",
                               )
outputLabel.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
#----------------------------------------
app.mainloop()