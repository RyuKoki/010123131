############################################################################
# Author : Onpinya Phokhahutthakosol
# File Name : calculator_program_(complete_version).py
############################################################################
############################################################################
# Before you use this code
# INSTALL 'PySimpleGUI' library first!
# by this command
# python -m pip install PySimpleGUI
# I wish you're funny ^^
############################################################################

import PySimpleGUI as sg 

# set theme
sg.theme('DarkGreen5')

# set all propertise each of button
digit_button = {'size':(4, 1), 'font':('Consolas', 30)}
operator_button = {'size':(4, 1), 'font':('Consolas', 30)}
special_button = {'size':(9, 1), 'font':('Consolas', 29)}

# draw all of buttons
layout =  [ [sg.Text('', size=(5, 1), justification='center', background_color='white',
                        text_color='black', font=('Consolas', 20), key='DISPLAY_OP')],
            [sg.Text('0', size=(14, 1), justification='right', background_color='white',
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
                sg.Button('=', **special_button, button_color=('white', 'orange'), bind_return_key=True)]    ] 

# keep all button on window
window = sg.Window('Simple Calculator', layout=layout, background_color="#272533", return_keyboard_events=True)

running = True

# 'var' for showing what button user click or type
var = ''

# 'equation' for giving to solve problem
equation = ''

####################WHILE RUNNING PROGRAM####################
while running:

    # giving input from GUI user
    event, values = window.read()
    # print(event)
    if event == sg.WIN_CLOSED or event == 'Escape:27':
        break

    # if don't have any vars, always 'set zero'
    if len(var) == 0:
        window['DISPLAY'].update('0')

    ##################PART WHAT USER CLICK###################
    # if it is digit(s) or dot (.)
    if event in '0123456789':
        # limit number only 10 digits
        if len(var) < 10:
            if event == '0' and var == '':
                # if press '0' firstly
                window['DISPLAY'].update('0')
            elif event == '0' and len(var) > 0:
                # if press '0' in number
                var += event
                equation += event
                window['DISPLAY'].update(var)
            # press 1-9 case
            elif event != '0':
                var += event
                equation += event
                window['DISPLAY'].update(var)
        # if press digits over 10 digits, don't do anything
        elif len(var) > 10:
            window['DISPLAY'].update(var)
    
    # dot (.) in decimal numbers
    elif event == '.':
        if var.count(event) == 0:
            var += event
            equation += event
            window['DISPLAY'].update(var)

    # set 'zero' when click 'AC' or type on keyboard End
    elif event == 'AC' or event == 'End:35':
        # initial 'var', 'equation' and all of display
        var = ''
        equation = ''
        window['DISPLAY'].update('0')
        window['DISPLAY_OP'].update('')

    # if click 'DEL' or type 'Back Space' delete the last input
    elif event == 'DEL' or event == 'BackSpace:8':
        if var != '':
            var = var.rstrip(var[-1])
            equation = equation.rstrip(equation[-1])
            window['DISPLAY'].update(var)

    elif event in '+-*/':
        # reset 'var' for showing on 'display'
        var = ''
        # make complete equation
        equation += event
        #####showing operator on 'display_op' stands for display operator
        if event in '+-':
            window['DISPLAY_OP'].update(event)
        elif event == '*':
            window['DISPLAY_OP'].update('x')
        elif event == '/':
            window['DISPLAY_OP'].update('÷')

    elif event == '=':
        try:
            # if click '=' or type 'enter' on keyboard 
            window['DISPLAY_OP'].update('') # reset 'var'
            calculate = eval(equation) # convert string equation to math equation
            ##########check integer (.0000) or float (.9999) by modulatate 2##########
            decimal = calculate % 2
            # odd or even answer
            if decimal == 0 or decimal == 1:
                # if answer '0' is even, otherhand answer '1' is odd
                total = str(int(calculate))
                window['DISPLAY'].update(total)
            else:
                # other case is decimal number
                total = float('%.4f'%calculate) # limit only 4 decimal
                window['DISPLAY'].update(str(total))
        # except Syntax error
        except SyntaxError:
            var = 'Syntax Error!'
            window['DISPLAY'].update(var)

window.close()
############################################################################
############################################################################
# This code is making from 'PySimpleGUI' 
# This is the most completely code of mine.
# This code is for 'Software Delvelopment I' subject.
# Thank you 'Dr.Rawat', Teacher!
# I wish you can use my code
# Finally, Thank you everybody to read, use and comment my code. ;)
############################################################################
############################################################################
