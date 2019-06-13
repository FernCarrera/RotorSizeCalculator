# Fernando Carrera
from Rotor_Sizer import findRadius
from commands import LabeledEntry
import tkinter as tk



def click():
    # mass,props,diskAF,solidity,cd0,machTip
    m = float(mass.get())
    p = float(props.get())
    DAF = float(diskAF.get())
    s = float(solidity.get())
    cdnot = float(cd0.get())
    mach = float(machTip.get())
    findRadius(m,p,DAF,s,cdnot,mach)


window = tk.Tk()
window.title('Rotor Sizer')
window.geometry('500x200')

#mass = Entry(window,width=10)
#mass.insert(END,'# of Props')
#mass.grid(column=1,row=0)
mass = LabeledEntry(window,"mass",width=7)
mass.grid(column=1,row=0)

props = LabeledEntry(window,"# of Props",width=10)
props.grid(column=2,row=0)

diskAF = LabeledEntry(window,"Disk Area Factor",width=15)
diskAF.grid(column=3,row=0)

solidity = LabeledEntry(window,"Solidity",width=10)
solidity.grid(column=4,row=0)

cd0 = LabeledEntry(window,"cd0",width=5)
cd0.grid(column=5,row=0)

machTip = LabeledEntry(window,"Mach Tip Speed",width=15)
machTip.grid(column=6,row=0)

enter = tk.Button(window,text="Enter",command=click)
enter.grid(column=7, row=0)



window.mainloop()

