import PySimpleGUI as sg 

sg.theme('DarkGreen5')

layout =  [ [sg.Text('0', size=(17, 1), justification='right', background_color='white',
                        text_color='black', font=('Consolas', 50), key='DISPLAY')],
            [sg.Button('{}'.format(str(i)), size=(5, 1), font=('Consolas', 30))for i in range(7, 10)] + 
                [sg.Button('DEL', size=(5, 1), font=('Consolas', 30)), 
                    sg.Button('AC', size=(5, 1), font=('Consolas', 30))],
            [sg.Button('{}'.format(str(i)), size=(5, 1), font=('Consolas', 30))for i in range(4, 7)] + 
                [sg.Button('*', size=(5, 1), font=('Consolas', 30)), 
                    sg.Button('/', size=(5, 1), font=('Consolas', 30))],
            [sg.Button('{}'.format(str(i)), size=(5, 1), font=('Consolas', 30))for i in range(1, 4)] + 
                [sg.Button('+', size=(5, 1), font=('Consolas', 30)), 
                    sg.Button('-', size=(5, 1), font=('Consolas', 30))],
            [sg.Button('0', size=(10, 1), font=('Consolas', 30)),
                sg.Button('.', size=(5, 1), font=('Consolas', 30)),
                sg.Button('=', size=(10, 1), font=('Consolas', 30))]    ] 

window = sg.Window('Calculator', layout)

running = True

while running:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()