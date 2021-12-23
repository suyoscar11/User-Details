import PySimpleGUI as sg
import pandas as pd

# We have added a Colour Themes to the windows.
sg.theme('DarkTeal9')

EXCEL_FILE = 'excel.xlsx'
df=pd.read_excel(EXCEL_FILE)
layout = [
   [sg.Text('Please fill out the following fields to know the weather condition of your area:')],
   [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
   [sg.Text('Country',size = (15,1)), sg.Combo([Nepal,India,USA,China,United Kingdom,Pakistan]), (key='Choose your Country')],
   [sg.Text('City', size=(15,1)), sg.InputText(key='City')]
   [sg.Text('Enter your E-mail', size=(15,1)), sg.InputText(key='Enter your E-mail')]
   [sg.Submit(), sg.Exit()]
        ]

window = sg.Window('Simple Data Entry Form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
       df=df.append(values,ignore_index=True)
       df.to_excel(EXCEL_FILE,index=False)
       sg.popup("Thanks. You will get your Area's Weather information in a moment.")