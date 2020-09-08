############################################################################
# Author : Onpinya Phokhahutthakosol
# File Name : demo-1.py
############################################################################
import PySimpleGUI as sg 

sg.theme('DarkGreen5')

digit_button = {'size':(4, 1), 'font':('Consolas', 30)}
operator_button = {'size':(4, 1), 'font':('Consolas', 30)}
special_button = {'size':(9, 1), 'font':('Consolas', 29)}

layout =  [ [sg.Text('0', size=(14, 1), justification='right', background_color='white',
                        text_color='black', font=('Consolas', 49), key='DISPLAY')],
            [sg.Button('{}'.format(str(i)), **digit_button)for i in range(7, 10)] + 
                [sg.Button('DEL', **operator_button, button_color=('white', 'black')), 
                    sg.Button('AC', **operator_button, button_color=('white', '#800000'))],
            [sg.Button('{}'.format(str(i)), **digit_button)for i in range(4, 7)] + 
                [sg.Button('*', **operator_button, button_color=('white', '#00ba82')), 
                    sg.Button('/', **operator_button, button_color=('white', '#00ba82'))],
            [sg.Button('{}'.format(str(i)), **digit_button)for i in range(1, 4)] + 
                [sg.Button('+', **operator_button, button_color=('white', '#00ba82')), 
                    sg.Button('-', **operator_button, button_color=('white', '#00ba82'))],
            [sg.Button('0', **special_button),
                sg.Button('.', **operator_button),
                sg.Button('=', **special_button, button_color=('white', 'orange'))]    ] 

window = sg.Window('Simple Calculator', layout=layout, background_color="#272533", return_keyboard_events=True)

running = True
var = ''
front = ''
operator = ''
back = ''
while running:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in '0123456789.':
        if event == '0':
            if var == '' or var == '0':
                var = '0'
                window['DISPLAY'].update(var)
        if var == '0':
            var = ''
        var += event
        window['DISPLAY'].update(var)

    if event == 'AC':
        var = '0'
        operator = ''
        window['DISPLAY'].update(var)

    if event == 'DEL':
        if var == '' or var == '0':
            var = '0'
            window['DISPLAY'].update(var)
        var = var.strip(var[-1])
        window['DISPLAY'].update(var)

    if event == '+':
        operator = event
    
    






window.close()
# comming soon
