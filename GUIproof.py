import PySimpleGUI as sg
from Button import *


def interfazInicial():
    
    layout= [
        [sg.Text('0', font='Italic 15', size=(26,1), justification='right', key='screen', background_color=('#000'))],
        [sg.Button('7',font='Italic 20',size=(3,1),key='7'),
            sg.Button('8',font='Italic 20',size=(3,1),key='8'),
            sg.Button('9',font='Italic 20',size=(3,1),key='9'),
            sg.Button('*',font='Italic 20',size=(3,1),key='*')],
             [sg.Button('4',font='Italic 20',size=(3,1),key='4'),
              sg.Button('5',font='Italic 20',size=(3,1),key='5'),
               sg.Button('6',font='Italic 20',size=(3,1),key='6'),
               sg.Button('/',font='Italic 20',size=(3,1),key='/')],
               [sg.Button('1',font='Italic 20',size=(3,1),key='1'),
              sg.Button('2',font='Italic 20',size=(3,1),key='2'),
               sg.Button('3',font='Italic 20',size=(3,1),key='3'),
               sg.Button('-',font='Italic 20',size=(3,1),key='-')],
               [sg.Button('0',font='Italic 20',size=(3,1),key='0'),
              sg.Button('.',font='Italic 20',size=(3,1),key='.'),
               sg.Button('=',font='Italic 20',size=(3,1),key='='),
               sg.Button('+',font='Italic 20',size=(3,1),key='+')],
               [sg.Button('Clear',font='Italic 20',size=(3,1),key='clear')]
               
    ]
    salir = [[sg.Button('Salir',font='Italic 20',size=(12,3),key='salir')]]
    return layout + salir

def principal():
    alto = 500
    ancho = 900    
    ventana = sg.Window ('',interfazInicial(), size = (ancho,alto),element_justification='center')
    ventana.Finalize()
    cad= ''
    firstOperator=''
    secondOperator=''
    
    while True:
        event, value = ventana.read()
        if (event == None or event == 'salir') :
            break
        if (event!='salir'):
            try:
                if(int(event) or event == '0'):
                    cad= buttonNumber(event,cad)
                    firstOperator=int(cad)
                    ventana ['screen'].Update(firstOperator)     
            except:
                print('operation') 
            #cad= buttonNumber(event,cad)
            #ventana ['screen'].Update(cad)
        if (event=='+'):
            n1=cad
            cad=''
            ventana ['screen'].Update(cad+n1)
        if (event=='clear'):
            cad= ''
            ventana['screen'].Update(0)
        
    ventana.Close()
principal()