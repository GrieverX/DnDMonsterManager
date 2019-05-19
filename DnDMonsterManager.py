try:
    from Tkinter import *
    import tkMessageBox
except:
    from tkinter import *
    from tkinter import messagebox

import MonsterATK

iniziativa_list = []
testo = ""


def add_initiative():
    if nome_iniz.get() == "":
        try:
            tkMessageBox.showinfo("Error", "Inserisci un nome")
            return 0
        except:
            messagebox.showinfo("Error", "Inserisci un nome")
            return 0
    global iniziativa_list
    diz = {}
    diz['nome'] = nome_iniz.get()
    diz['iniziativa'] = val_iniz.get()
    iniziativa_list.append(diz)
    global testo
    testo += nome_iniz.get() + ": " + str(val_iniz.get()) + "\n"
    esito.config(text=testo)


def ordina():
    global iniziativa_list
    iniziativa_list = ordinalista(iniziativa_list)
    testo = ""
    for elemento in iniziativa_list:
        testo += (elemento['nome'] + ": " + str(elemento['iniziativa']) + "\n")
    esito.config(text=testo)


def ordinalista(lista):
    listaordinata = []
    while len(lista) > 0:
        elem_max = lista[0]
        for elemento in lista:
            if elemento['iniziativa'] > elem_max['iniziativa']:
                elem_max = elemento
        listaordinata.append(elem_max)
        lista.remove(elem_max)
    return listaordinata


def clear_iniziativa():
    global iniziativa_list
    iniziativa_list = []
    global testo
    testo = ""
    esito.config(text=testo)


def finestra_mostro():
    mostro = MonsterATK.Monster()
    print('fatto!')
    print(mostro)


finestra = Tk()
finestra.title('DnD Monster Manager v1.0')

griglia_iniziativa = Label(finestra, text="Iniziativa:")
nome_iniz = StringVar(value="")
entry_nome_iniz = Entry(finestra, textvariable=nome_iniz)
val_iniz = IntVar(value=0)
entry_iniz = Entry(finestra, textvariable=val_iniz)
inserisci_iniz = Button(finestra, text="inserisci", command=add_initiative)
clear_iniz = Button(finestra, text="clear", command=clear_iniziativa)
finito_iniz = Button(finestra, text="ordina", command=ordina)
esito = Label(finestra, text="")

nuova_finestra = Button(finestra, text="aggiungi mostro", command=finestra_mostro)

griglia_iniziativa.grid(row=0, column=0)
entry_nome_iniz.grid(row=1, column=0)
inserisci_iniz.grid(row=1, column=3)
clear_iniz.grid(row=1, column=4)
entry_iniz.grid(row=1, column=1)
finito_iniz.grid(row=2, column=3)
esito.grid(row=3, column=0)
nuova_finestra.grid(row=4, column=4)

finestra.mainloop()

