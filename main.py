# Periodic Table Information Finder

from pyscript import display, document

def check_details(e):
    document.getElementById('output').innerHTML = ' '
    user_input = document.getElementById('input1').value

    nonmetal_elements = {
    'H': {'Element':'Hydrogen','Atomic Number':'1', 'Atomic Mass':'1.008',}, 
    'C':{'Element':'Carbon', 'Atomic Number':'12', 'Atomic Mass':'12.01'},
    'N': {'Element':'Nitrogen', 'Atomic Number':'7', 'Atomic Mass':'14.01'},
    'O':{'Element':'Oxygen', 'Atomic Number':'8', 'Atomic Mass':'16.00'},
    'F':{'Element':'Fluorine', 'Atomic Number':'9', 'Atomic Mass':'19.00'},
    'Ne':{'Element':'Neon', 'Atomic Number':'10', 'Atomic Mass':'20.18'},
    'P':{'Element':'Phosphorous', 'Atomic Number':'15', 'Atomic Mass':'30.97'},
    'S':{'Element':'Sulfur', 'Atomic Number':'16', 'Atomic Mass':'32.07'},
    'Cl':{'Element':'Chlorine', 'Atomic Number':'17', 'Atomic Mass':'35.45'},
    'Ar':{'Element':'Argon', 'Atomic Number':'18', 'Atomic Mass':'39.95'},
    'Se':{'Element':'Selenium', 'Atomic Number':'34', 'Atomic Mass':'78.96'},
    'Br':{'Element':'Bromine', 'Atomic Number':'35', 'Atomic Mass':'79.90'},
    'Kr':{'Element':'Krypton', 'Atomic Number':'36', 'Atomic Mass':'83.80'},
    'I':{'Element':'Iodine', 'Atomic Number':'53', 'Atomic Mass':'126.9'},
    'Xe':{'Element':'Xenon', 'Atomic Number':'54', 'Atomic Mass':'131.3'},
    'Rn':{'Element':'Radon', 'Atomic Number':'86', 'Atomic Mass':'222'},
    'He':{'Element':'Helium', 'Atomic Number':'2', 'Atomic Mass':'4.003'},
    'Og':{'Element':'Oganesson', 'Atomic Number':'118', 'Atomic Mass':'294'}
    }

    elements_checker = user_input in nonmetal_elements

    display_message = (f'Sorry, no {user_input} in the non-metal list', f'Symbol: {user_input}, Element: {user_input}, Atomic Number: {user_input}, Atomic Mass: {user_input}')
    display(display_message[elements_checker], target='output')