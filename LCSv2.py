import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window
from math import *


def InitialInterface():
    #Layout                             #Create GUI
    layout= [
        [sg.Text('0', font='Italic 15', size=(29,2), justification='right', key='input', background_color=('#000'))],
        [sg.Button('+/-',font='Italic 20',size=(3,1),key='+/-'),sg.Button('7',font='Italic 20',size=(3,1),key=7),sg.Button('8',font='Italic 20',size=(3,1),key=8), sg.Button('9',font='Italic 20',size=(3,1),key=9),sg.Button('*',font='Italic 20',size=(3,1),key='*')],
        [sg.Button('x!',font='Italic 20',size=(3,1),key='x!'),sg.Button('4',font='Italic 20',size=(3,1),key=4),sg.Button('5',font='Italic 20',size=(3,1),key=5),sg.Button('6',font='Italic 20',size=(3,1),key=6),sg.Button('/',font='Italic 20',size=(3,1),key='/')],
        [sg.Button('xⁿ',font='Italic 20',size=(3,1),key='xⁿ'),sg.Button('1',font='Italic 20',size=(3,1),key=1),sg.Button('2',font='Italic 20',size=(3,1),key=2),sg.Button('3',font='Italic 20',size=(3,1),key=3),sg.Button('-',font='Italic 20',size=(3,1),key='-')],
        [sg.Button('√',font='Italic 20',size=(3,1),key='√'),sg.Button('0',font='Italic 20',size=(3,1),key=0),sg.Button('.',font='Italic 20',size=(3,1),key='.'),sg.Button('=',font='Italic 20',size=(3,1),key='='),sg.Button('+',font='Italic 20',size=(3,1),key='+')],
        [sg.Button('(',font='Italic 20',size=(3,1),key='('),sg.Button(')',font='Italic 20',size=(3,1),key=')'), sg.Button('Clear',font='Italic 20',size=(7,1),key='clear'),sg.Button('<<',font='Italic 20',size=(3,1),key='<<')],
        ]
    return layout

    # Set PySimpleGUI
def principal():
    hight = 400
    width = 400   
    body = sg.Window ('LCS v2.0',InitialInterface(), size = (width,hight),element_justification='center')
    body.Finalize()
    
    # Set Operators
    equal= ''
    operators=['+','-','*','/','(',')','.']
    specialOperators=['√','x!','xⁿ','+/-']
    
    #Loop GUI
    while True:
        event, values = body.read()
        
    #Buttons event        
        if (event == None) :
            break
        elif (event=='clear'):
            equal=equal=''
            body ['input'].Update(equal)
        elif (event== '<<'):
            equal=equal[:-1]
            body ['input'].Update(equal)
        elif (event in range(0,10) or event in operators):
            equal+=str(event)
            body['input'].Update(equal)
    
    #Buttons event in special cases
        elif event in specialOperators:                                 
            if '√' in event :
                equal=str(sqrt(float(equal)))
                body['input'].Update(equal)
            if 'x!' in event :
                if  int(equal)>3200:
                    body ['input'].Update('Overflow') 
                else:
                    equal=str(factorial(float(equal)))
                    body['input'].Update(equal)
            if 'xⁿ' in event :
                equal+='**'
                body['input'].Update(equal)
            if '+/-' in event :
                if '-' in equal[0]:
                    equal=equal[1 : : ]
                    body['input'].Update(equal)
                else:
                    equal=('-'+equal)
                    body['input'].Update(equal)
        
    #Math core
        elif (event == '=' ):
            try:
                body ['input'].Update(equal)
                equal=str(eval(equal))
                body ['input'].Update(equal)
            except:
                equal=equal=''
                body ['input'].Update('Math Error') 
    
    body.Close()
principal()