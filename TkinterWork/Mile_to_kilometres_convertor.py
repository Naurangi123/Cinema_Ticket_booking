from tkinter import *

def miles_to_km():
    miles=float(miles_input.get())
    km=round(miles*1.609)
    kilomters_result_label.config(text=f"{km}")

window=Tk()
window.title("Mile to kilometer converter")
window.config(padx=500,pady=400,bg="blue")

miles_input=Entry(width=20,bg="blue")
miles_input.grid(column=1,row=0)


miles_label=Label(text="Miles",bg="blue")
miles_label.grid(column=2,row=0)

is_equal_label=Label(text="is equal to",bg="blue")
is_equal_label.grid(column=0,row=1)

kilomters_result_label=Label(text="0",bg="blue")
kilomters_result_label.grid(column=1,row=1)

kilometer_label=Label(text="Km",bg="blue")
kilometer_label.grid(column=2,row=1)

calculate_button=Button(width=20,text="Calculate",bg="blue",command=miles_to_km)
calculate_button.grid(column=1,row=2 )

window.mainloop()

