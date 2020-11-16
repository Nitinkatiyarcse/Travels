from tkinter import *
root = Tk()
def getvals():
    print("Submitted form")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")

    with open("records.text", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")


root.geometry("445x255")
root.title("Nitin Travels")
# Heading
Label(root, text="Welcome to Nitin Travels", font="comicsansns 13 bold", pady=10, padx=2).grid(row=0, column=3)
#text for form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency contact")
paymentmode = Label(root, text="Payment Mode")
#text for form pake
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# tkinter variable for storing entry
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

#Entry for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# packing the entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

#Checkbox
foodservice = Checkbutton(text= "want to prebook your meals",variable =foodservicevalue )
foodservice.grid(row=6, column=3)

#Button and packing
Button(text="Submit to Nitin travels",font="comicsansns 8 bold", bg = "yellow", command=getvals).grid(row=7, column=3)



root.mainloop()