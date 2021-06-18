import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import database
import motocicleta
import vendas

def menu():
    sg.theme('Dark')

    layout = [
        [sg.Text('MENU PRINCIPAL', justification='center', font=("Unispace", 30), size=(20,1))],
        [sg.Button('Controle de Clientes', size=(25,1), button_color=('white', 'black'), key = 'clientes')],
        [sg.Button('Controle de Motocicletas', size=(25,1), button_color=('white', 'black'), key = 'motocicletas')],
        [sg.Button('Efetuar Venda', size=(25,1), button_color=('white', 'black'), key = 'venda')],
        [sg.Button('Vendas', size=(25,1), button_color=('white', 'black'), key = 'listaVendas')],
        [sg.Button('Sair', size=(25,1), button_color=('white', 'black'))]
    ]
    window = sg.Window('Concessionária Falcões', layout=layout, element_padding=(0,2),element_justification='c', font=("Unispace", 15), modal=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        elif event == 'clientes':
            window.close()
            controleCliente()
            break
        elif event == 'motocicletas':
            window.close()
            controleMotocicleta()
        elif event == 'venda':
            window.close()
            venda()
        elif event == 'listaVendas':
            window.close()
            listaVendas()
    window.close()

###################################### CONTROLE CLIENTE ######################################

def controleCliente():
    sg.theme('Dark')

    layout = [
        [sg.Text('Controle de Clientes', justification='center', font=("Unispace", 30), size=(20, 1))],
        [sg.Button('Lista de clientes', size=(25,1), button_color=('white', 'black'), key = 'listaCliente')],
        [sg.Button('Cadastrar cliente', size=(25,1), button_color=('white', 'black'), key = 'cadCliente')],
        [sg.Button('Voltar', size=(25,1), button_color=('white', 'black'), key = 'voltar')]
    ]
    window = sg.Window('Concessionária Falcões', layout, element_padding=(0,2), element_justification='c', font=("Unispace", 15), modal=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'voltar':
            window.close()
            menu()
            break
        elif event == 'cadCliente':
            window.close()
            cadCliente()
            break
        elif event == 'listaCliente':
            window.close()
            listaCliente()
            break

def cadCliente():
    sg.theme('Dark')

    name = database.read_task()

    layout = [
        [sg.Text('Cadastrar Cliente', justification='center', font=("Unispace", 30), size=(28, 1))],
        [sg.Text('Nome:', size = (5,0), relief=sg.RELIEF_FLAT), sg.InputText('', size = (45,0), pad=(3,5), key='-Nome-')],
        [sg.Text('Idade:', size = (6,0), relief=sg.RELIEF_FLAT), sg.InputText('', size = (3,0), pad=(3,5), key='-Idade-'), sg.Text('Telefone:', pad = (6,0), size = (9,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (15,0), key='-Tel-')],
        [sg.Text('Email:', size = (6,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (30,0), pad=(3,5),key='-Email-')],
        [sg.Text('CPF:', size = (4,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (15,0), pad=(3,5), key='-Cpf-')],
        [sg.Text('Endereço:', size = (9,1), relief=sg.RELIEF_FLAT), sg.InputText('', pad=(3,5), key='-End-')],
        [sg.Text('Cidade:', size = (7,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (25,0), pad=(3,5), key='-Cid-'), sg.Text('UF:', pad=(3,0), size = (3,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (3,0), key='-UF-')],
        [sg.Button('Cadastrar', pad=(5,10), border_width=3, button_color=('white', 'black')), sg.Button('Voltar', pad=(5,10),border_width=3, button_color=('white', 'black'))]
    ]
    window = sg.Window('Concessionária Falcões', layout, element_padding=(0,2), font=('Unispace', 15), modal=True)

    while True:
        event, values = window.read()

        if event == 'Voltar':
            window.close()
            controleCliente()
            break
    
        elif event == 'Cadastrar':
            [sg.Popup('Cadastro realizado com sucesso!')]
            name = values['-Nome-']
            idade = values['-Idade-']
            telefone = values['-Tel-']
            email = values['-Email-']
            cpf = values['-Cpf-']
            endereco = values['-End-']
            cidade = values['-Cid-']
            uf = values['-UF-']

            if name != '':
                database.write(name, idade, telefone, email, cpf, endereco, cidade, uf)

            name = database.read_task()

            window.find_element('-Nome-').Update('')
            window.find_element('-Idade-').Update('')
            window.find_element('-Tel-').Update('')
            window.find_element('-Email-').Update('')
            window.find_element('-Cpf-').Update('')
            window.find_element('-End-').Update('')
            window.find_element('-Cid-').Update('')
            window.find_element('-UF-').Update('')

            window.close()
            controleCliente()
            break

def listaCliente():
    sg.theme('Dark')

    name = database.read_task()

    layout = [
        [sg.Text('Lista de Clientes', justification='center', font=("Unispace", 25), size=(25,1), pad=(0,5))],
        [sg.Listbox(name, size = (30,5), font=('CommicSans', 20), key = '-BOX-')],
        [sg.Button('Remover cliente', size=(16,1), button_color=('white', 'black'), pad = (5,5), key = 'remover'), sg.Button('Voltar', size=(16,1), button_color=('white', 'black'))]
    ]

    window = sg.Window('Concessionária Falcões', layout, element_justification='c', element_padding=(0,2), font=('Unispace', 15), modal=True)

    while True:
        button, values = window.read()

        if button == 'remover':
            if name:
                x = values['-BOX-'][0]
                database.delete(x)
                name = database.read_task()
                window.find_element('-BOX-').Update(name)

        elif button == 'Voltar':
            window.close()
            controleCliente()
            break

###################################### CONTROLE MOTOCICLETA ######################################

def controleMotocicleta():
    sg.theme('Dark')

    layout = [
        [sg.Text('Controle de Motocicletas', justification='center', font=("Unispace", 27), size=(24, 1))],
        [sg.Button('Lista de Motocicletas', size=(25,1), button_color=('white', 'black'), key = 'listaMotocicleta')],
        [sg.Button('Cadastrar Motocicleta', size=(25,1), button_color=('white', 'black'), key = 'cadMotocicleta')],
        [sg.Button('Voltar', size=(25,1), button_color=('white', 'black'), key = 'voltar')]
    ]
    window = sg.Window('Concessionária Falcões', layout, element_padding=(0,2), element_justification='c', font=("Unispace", 15), modal=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'voltar':
            window.close()
            menu()
            break
        elif event == 'cadMotocicleta':
            window.close()
            cadMotocicleta()
            break
        elif event == 'listaMotocicleta':
            window.close()
            listaMotocicleta()
            break

def cadMotocicleta():
    sg.theme('Dark')

    model = motocicleta.read_task()

    layout = [
        [sg.Text('Cadastrar Motocicleta', justification='center', font=("Unispace", 30), size=(23, 1))],
        [sg.Text('Marca:', size = (7,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (35,0), pad=(3,5), key='-Marca-')],
        [sg.Text('Modelo:', size = (7,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (35,0), pad=(3,5), key='-Modelo-')],
        [sg.Text('Versão:', size = (7,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (35,0), pad=(3,5),key='-Versao-')],
        [sg.Text('Ano:', size = (4,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (8,0), pad=(3,5), key='-Ano-')],
        [sg.Text('Preço:', size = (6,1), relief=sg.RELIEF_FLAT), sg.InputText('', size = (8,0), pad=(3,5), key='-Preco-')],
        [sg.Button('Cadastrar', pad=(5,10), border_width=3, button_color=('white', 'black')), sg.Button('Voltar', pad=(5,10),border_width=3, button_color=('white', 'black'))]
    ]
    window = sg.Window('Concessionária Falcões', layout, element_padding=(0,2), font=('Unispace', 15), modal=True)

    while True:
        event, values = window.read()

        if event == 'Voltar':
            window.close()
            controleMotocicleta()
            break
    
        elif event == 'Cadastrar':
            [sg.Popup('Motocicleta cadastrada com sucesso!')]
            marca = values['-Marca-']
            modelo = values['-Modelo-']
            versao = values['-Versao-']
            ano = values['-Ano-']
            preco = values['-Preco-']

            if model != '':
                motocicleta.write(marca, modelo, versao, ano, preco)

            model = motocicleta.read_task()

            window.find_element('-Marca-').Update('')
            window.find_element('-Modelo-').Update('')
            window.find_element('-Versao-').Update('')
            window.find_element('-Ano-').Update('')
            window.find_element('-Preco-').Update('')

            window.close()
            controleMotocicleta()
            break

def listaMotocicleta():
    sg.theme('Dark')

    model = motocicleta.read_task()

    layout = [
        [sg.Text('Lista de Motocicletas', justification='center', font=("Unispace", 25), size=(24,1), pad=(0,5))],
        [sg.Listbox(model, size = (30,5), font=('CommicSans', 20), key = '-BOX-')],
        [sg.Button('Remover motocicleta', size=(21,1), button_color=('white', 'black'), pad = (5,5), key = 'remover'), sg.Button('Voltar', size=(16,1), button_color=('white', 'black'))]
    ]

    window = sg.Window('Concessionária Falcões', layout, element_justification='c', element_padding=(0,2), font=('Unispace', 15), modal=True)

    while True:
        button, values = window.read()

        if button == 'remover':
            if model:
                x = values['-BOX-'][0]
                motocicleta.delete(x)
                model = motocicleta.read_task()
                window.find_element('-BOX-').Update(model)

        elif button == 'Voltar':
            window.close()
            controleMotocicleta()
            break

###################################### EFETUAR VENDA ######################################

def venda():
    sg.theme('Dark')

    venda = vendas.read_task()

    layout = [
        [sg.Text('Efetuar Venda', justification='center', font=("Unispace", 25), size=(26, 1), pad = (0,5))],
        [sg.Text('Marca:', size=(7,1)), sg.InputText('', size=(35,1), pad = (3,5), key = '-Marca-')],
        [sg.Text('Modelo:', size=(7,1)), sg.InputText('', size=(35,1), pad = (3,5), key = '-Modelo-')],
        [sg.Text('Versão:', size=(7,1)), sg.InputText('', size=(35,1), pad = (3,5), key = '-Versao-')],
        [sg.Text('Ano:', size=(4,1)), sg.InputText('', size=(8,1), pad = (3,5), key = '-Ano-')],
        [sg.Text('Preço:', size=(6,1)), sg.InputText('', size=(8,1), pad = (3,5), key = '-Preco-')],
        [sg.Text('Pagamento:', size=(10,1)), sg.Checkbox('Cartão de Crédito', font=("Unispace", 11)), sg.Checkbox('Dinheiro', font=("Unispace", 11))], 
        [sg.Button('Finalizar Venda', button_color=('white', 'black'), pad=(5,5), key = 'finalizar'), sg.Button('Voltar', button_color=('white', 'black'), pad=(0,1))]
    ]
    window = sg.Window('Concessionária Falcões', layout=layout, element_padding=(0,2), font=("Unispace", 14), modal=True)

    while True:
        event, values = window.read()

        if event == 'finalizar':
            [sg.Popup('Venda Realizada!')]
            marca = values['-Marca-']
            modelo = values['-Modelo-']
            versao = values['-Versao-']
            ano = values['-Ano-']
            preco = values['-Preco-']

            if venda != '':
                vendas.write(marca, modelo, versao, ano, preco)

            venda = vendas.read_task()

            window.close()
            break
        elif event == 'Voltar':
            window.close()
            break
    menu()

###################################### LISTA DE VENDAS ######################################

def listaVendas():
    sg.theme('Dark')

    venda = vendas.read_task()

    layout = [
        [sg.Text('Lista de Vendas', justification='center', font=("Unispace", 25), size=(24,1), pad=(0,5))],
        [sg.Listbox(venda, size = (30,5), font=('CommicSans', 20), key = '-BOX-')],
        [sg.Button('Voltar', size=(16,1), button_color=('white', 'black'))]
    ]

    window = sg.Window('Concessionária Falcões', layout, element_justification='c', element_padding=(0,2), font=('Unispace', 15), modal=True)

    while True:
        event, values = window.read()

        if event == 'Voltar':
            window.close()
            break
    menu()

###################################### CHAMAR MENU ######################################
menu()