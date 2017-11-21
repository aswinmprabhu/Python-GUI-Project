print("Hello World")
from Tkinter import *
import ttk
from ttk import *




def valueErrorHandler(s):
    try:
        return float(s)
    except ValueError:
        return NONE

def convertCurrency(event):
    r = valueErrorHandler(rupeesEntry.get())
    y = valueErrorHandler(yenEntry.get())
    p = valueErrorHandler(poundEntry.get())
    d = valueErrorHandler(dollarEntry.get())
    e = valueErrorHandler(euroEntry.get())

    if r==NONE and y==NONE and p==NONE and d==NONE:
        rupeesEntry.delete(0,'end')
        poundEntry.delete(0,'end')
        yenEntry.delete(0,'end')
        dollarEntry.delete(0,'end')


        rupeesEntry.insert(0, str(e*76.57))
        yenEntry.insert(0, str(e * 132))
        poundEntry.insert(0, str(e * 0.89))
        dollarEntry.insert(0, str(e * 1.18))

    if r==NONE and y==NONE and p==NONE and e==NONE:
        rupeesEntry.delete(0, 'end')
        poundEntry.delete(0, 'end')
        yenEntry.delete(0, 'end')
        euroEntry.delete(0, 'end')

        rupeesEntry.insert(0, str(d*65.04))
        yenEntry.insert(0, str(d * 113))
        poundEntry.insert(0, str(d * 0.75))
        euroEntry.insert(0, str(d * 0.85))

    if r==NONE and y==NONE and d==NONE and e==NONE:
        rupeesEntry.delete(0, 'end')
        yenEntry.delete(0, 'end')
        dollarEntry.delete(0, 'end')
        euroEntry.delete(0, 'end')

        rupeesEntry.insert(0, str(p*86.16))
        yenEntry.insert(0, str(p * 149))
        dollarEntry.insert(0, str(p * 1.32))
        euroEntry.insert(0, str(p * 1.13))

    if r==NONE and p==NONE and d==NONE and e==NONE:
        rupeesEntry.delete(0, 'end')
        poundEntry.delete(0, 'end')
        dollarEntry.delete(0, 'end')
        euroEntry.delete(0, 'end')

        rupeesEntry.insert(0, str(y*0.58))
        poundEntry.insert(0, str(y * 0.0067))
        dollarEntry.insert(0, str(y * 0.0089))
        euroEntry.insert(0, str(y * 0.0076))

    if y == NONE and p == NONE and d == NONE and e == NONE:
        poundEntry.delete(0, 'end')
        yenEntry.delete(0, 'end')
        dollarEntry.delete(0, 'end')
        euroEntry.delete(0, 'end')

        yenEntry.insert(0, str(r * 1.73))
        poundEntry.insert(0, str(r * 0.012))
        dollarEntry.insert(0, str(r * 0.015))
        euroEntry.insert(0, str(r * 0.013))


def convertLength(event):
    m = valueErrorHandler(meterEntry.get())
    y = valueErrorHandler(yardEntry.get())
    mi = valueErrorHandler(mileEntry.get())
    i = valueErrorHandler(inchEntry.get())
    f = valueErrorHandler(footEntry.get())

    if m==NONE and y==NONE and mi==NONE and i==NONE:
        meterEntry.delete(0,'end')
        yardEntry.delete(0,'end')
        mileEntry.delete(0,'end')
        inchEntry.delete(0,'end')



        meterEntry.insert(0, str(f*0.3048))
        yardEntry.insert(0, str( f*0.33333))
        mileEntry.insert(0, str( f*0.000189394))
        inchEntry.insert(0, str(f*12))

    if f==NONE and y==NONE and mi==NONE and i==NONE:
            footEntry.delete(0,'end')
            yardEntry.delete(0,'end')
            mileEntry.delete(0,'end')
            inchEntry.delete(0,'end')



            footEntry.insert(0, str(m*3.280))
            yardEntry.insert(0, str( m*1.09))
            mileEntry.insert(0, str( m*0.00062))
            inchEntry.insert(0, str(m*39.37))

    if m==NONE and f==NONE and mi==NONE and i==NONE:
        meterEntry.delete(0,'end')
        footEntry.delete(0,'end')
        mileEntry.delete(0,'end')
        inchEntry.delete(0,'end')



        meterEntry.insert(0, str(y*0.9144))
        footEntry.insert(0, str( y*3))
        mileEntry.insert(0, str( y*0.00056182))
        inchEntry.insert(0, str(y*36))


    if m==NONE and y==NONE and f==NONE and i==NONE:
        meterEntry.delete(0,'end')
        yardEntry.delete(0,'end')
        footEntry.delete(0,'end')
        inchEntry.delete(0,'end')



        meterEntry.insert(0, str(mi*1609.344))
        yardEntry.insert(0, str( mi*1760))
        footEntry.insert(0, str( mi*5280))
        inchEntry.insert(0, str(mi*63360))

    if m==NONE and y==NONE and mi==NONE and f==NONE:
        meterEntry.delete(0,'end')
        yardEntry.delete(0,'end')
        mileEntry.delete(0,'end')
        footEntry.delete(0,'end')



        meterEntry.insert(0, str(i*0.0254))
        yardEntry.insert(0, str( i*0.0277))
        mileEntry.insert(0, str( i*0.0000157828))
        footEntry.insert(0, str(i*0.08333))




def convertTemperature(event):
    k = valueErrorHandler(kelvinEntry.get())
    c = valueErrorHandler(celsiusEntry.get())
    f = valueErrorHandler(fahrenheitEntry.get())

    if k==NONE and c==NONE :
        kelvinEntry.delete(0,'end')
        celsiusEntry.delete(0,'end')



        kelvinEntry.insert(0, str((5/9)*(f-32))+273)
        celsiusEntry.insert(0, str( (5/9)*(f-32)))

    if f== NONE and c == NONE:
        fahrenheitEntry.delete(0, 'end')
        celsiusEntry.delete(0, 'end')

        fahrenheitEntry.insert(0, str((9/5(k-273))+32))
        celsiusEntry.insert(0, str(k-273))

    if k == NONE and f == NONE:
        kelvinEntry.delete(0, 'end')
        fahrenheitEntry.delete(0, 'end')

        kelvinEntry.insert(0, str(((9/5)*c)+32))
        fahrenheitEntry.insert(0, str(c+273))

"""
def converterweight(event):
    k = valueErrorHandler(kilogramEntry.get())
    p = valueErrorHandler(poundEntry.get())
    

    if k==NONE :
        poundEntry.delete(0,'end')
       


        poundEntry.insert(0, str())
       
    """
root = Tk()
root.title("ConvertKing")

notebook = ttk.Notebook(root)
notebook.grid(row=0,column=0,columnspan=50,rowspan=49,sticky='NESW')

currencyFrame=Frame(notebook)
currencyFrame.grid(row=1,column=0,sticky='NESW')

lengthFrame=Frame(notebook)
lengthFrame.grid(row=1,column=0,sticky='NESW')

temperatureFrame=Frame(notebook)
temperatureFrame.grid(row=1,column=0,sticky='NESW')



label1=Label(currencyFrame, text="Rupees", ).grid(row=2,column=0,sticky=E,ipady=10)
rupeesEntry=Entry(currencyFrame)
rupeesEntry.grid(row=2,column=1,sticky=W)

label2=Label(currencyFrame, text="Yen").grid(row=3,column=0,sticky=E,ipady=10)
yenEntry=Entry(currencyFrame)
yenEntry.grid(row=3,column=1,sticky=W)

label3=Label(currencyFrame, text="Dollar").grid(row=4,column=0,sticky=E,ipady=10)
dollarEntry=Entry(currencyFrame)
dollarEntry.grid(row=4,column=1,sticky=W)

label4=Label(currencyFrame, text="Euro").grid(row=5,column=0,sticky=E,ipady=10)
euroEntry=Entry(currencyFrame)
euroEntry.grid(row=5,column=1,sticky=W)

label5=Label(currencyFrame, text="Pound").grid(row=6,column=0,sticky=E,ipady=10)
poundEntry=Entry(currencyFrame)
poundEntry.grid(row=6,column=1,sticky=W)

convertButton=Button(currencyFrame, text="Convert")
convertButton.bind("<Button-1>",convertCurrency)
convertButton.grid(row=7,column=1)


label1=Label(lengthFrame, text="Metre").grid(row=2,column=0,sticky=E,ipady=10)
meterEntry=Entry(lengthFrame)
meterEntry.grid(row=2,column=1,sticky=W)

label2=Label(lengthFrame, text="Yard").grid(row=3,column=0,sticky=E,ipady=10)
yardEntry=Entry(lengthFrame)
yardEntry.grid(row=3,column=1,sticky=W)

label3=Label(lengthFrame, text="Mile").grid(row=4,column=0,sticky=E,ipady=10)
mileEntry=Entry(lengthFrame)
mileEntry.grid(row=4,column=1,sticky=W)

label4=Label(lengthFrame, text="Inch").grid(row=5,column=0,sticky=E,ipady=10)
inchEntry=Entry(lengthFrame)
inchEntry.grid(row=5,column=1,sticky=W)

label5=Label(lengthFrame, text="Foot").grid(row=6,column=0,sticky=E,ipady=10)
footEntry=Entry(lengthFrame)
footEntry.grid(row=6,column=1,sticky=W)

convertButton=Button(lengthFrame, text="Convert")
convertButton.bind("<Button-1>",convertLength)
convertButton.grid(row=7,column=1)


label1=Label(temperatureFrame, text="celsius").grid(row=2,column=0,sticky=E,ipady=10)
celsiusEntry=Entry(temperatureFrame)
celsiusEntry.grid(row=2,column=1,sticky=W)

label2=Label(temperatureFrame, text="kelvin").grid(row=3,column=0,sticky=E,ipady=10)
kelvinEntry=Entry(temperatureFrame)
kelvinEntry.grid(row=3,column=1,sticky=W)

label3=Label(temperatureFrame, text="fahrenheit").grid(row=4,column=0,sticky=E,ipady=10)
fahrenheitEntry=Entry(temperatureFrame)
fahrenheitEntry.grid(row=4,column=1,sticky=W)

convertButton=Button(temperatureFrame, text="Convert")
convertButton.bind("<Button-1>",convertTemperature)
convertButton.grid(row=7,column=1)


notebook.add(currencyFrame, text="Currency")
notebook.add(lengthFrame, text="Length")
notebook.add(temperatureFrame, text="Temperature")



root.mainloop()


