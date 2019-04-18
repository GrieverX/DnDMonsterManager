
from Tkinter import *
from random import randrange


def rolla(dado):
    return randrange(1, dado+1)


class Monster:

    def __init__(self):
        self.attack_result = ""
        self.finestra = Toplevel()
        self.finestra.title('Monster')

        self.label_nome = Label(self.finestra, text="nome")
        self.nome_mostro = StringVar(value="")
        self.entry_nome_mostro = Entry(self.finestra, textvariable=self.nome_mostro)

        self.label_pf = Label(self.finestra, text="punti ferita")
        self.pf_mostro = IntVar(value=0)
        self.entry_pf_mostro = Entry(self.finestra, textvariable=self.pf_mostro)

        self.punti_ferita = 0
        self.punti_ferita_momentanei = 0

        self.spazio_vuoto = Label(self.finestra, text="")

        self.label_subisci_danno = Label(self.finestra, text="subisci danno")
        self.val_danno_subito = IntVar(value=0)
        self.entry_danno = Entry(self.finestra, textvariable=self.val_danno_subito)

        self.subisci_danno = Button(self.finestra, text="go!", command=self.subisci_attacco)
        self.undo_danno_butt = Button(self.finestra, text="undo", command=self.undo_danno)

        self.spazio_vuoto2 = Label(self.finestra, text="")

        self.label_tpc = Label(self.finestra, text="modif. TPC")
        self.modif_tiro_per_colpire = IntVar(value=0)
        self.entry_modif_tpc = Entry(self.finestra, textvariable=self.modif_tiro_per_colpire)

        self.val_mod_attacco = StringVar(value="normale")
        self.radio_normale = Radiobutton(self.finestra, text='normale    ', value='normale', variable=self.val_mod_attacco)
        self.radio_vantaggio = Radiobutton(self.finestra, text='vantaggio ', value='vantaggio', variable=self.val_mod_attacco)
        self.radio_svantaggio = Radiobutton(self.finestra, text='svantaggio', value='svantaggio', variable=self.val_mod_attacco)

        self.attacco_label = Label(self.finestra, text="dadi attacco")
        self.val_attacco = StringVar(value="")
        self.entry_attacco = Entry(self.finestra, textvariable=self.val_attacco)
        self.attacca = Button(self.finestra, text="attacco!", command=self.attacco)

        self.spazio_vuoto3 = Label(self.finestra, text="")

        self.label_result_attacco = Label(self.finestra, text=self.attack_result)

        self.label_nome.grid(row=0, column=0)
        self.entry_nome_mostro.grid(row=0, column=1)

        self.label_pf.grid(row=2, column=0)
        self.entry_pf_mostro.grid(row=2, column=1)

        self.spazio_vuoto.grid(row=3, column=0)

        self.label_subisci_danno.grid(row=4, column=0)
        self.entry_danno.grid(row=4, column=1)
        self.subisci_danno.grid(row=4, column=2)
        self.undo_danno_butt.grid(row=4, column=3)

        self.spazio_vuoto2.grid(row=5, column=0)

        self.label_tpc.grid(row=6, column=0)
        self.entry_modif_tpc.grid(row=6, column=1)

        self.radio_normale.grid(row=7, column=0)
        self.radio_vantaggio.grid(row=8, column=0)
        self.radio_svantaggio.grid(row=9, column=0)

        self.attacco_label.grid(row=10, column=0)
        self.entry_attacco.grid(row=10, column=1)
        self.attacca.grid(row=10, column=2)

        self.spazio_vuoto3.grid(row=11, column=0)

        self.label_result_attacco.grid(row=12, column=1)

    def tiro_per_colpire(self):
        # -rolla d20
        # -add modificatore tiro
        # -printa risultato tiro per colpire

        self.attack_result += "tiro per colpire: "
        print(self.modif_tiro_per_colpire.get())
        if self.val_mod_attacco.get() == 'vantaggio' or self.val_mod_attacco.get() == 'svantaggio':
            tiro1 = rolla(20)
            print('roll1 = ' + str(tiro1))
            tiro2 = rolla(20)
            print('roll2 = ' + str(tiro2))
            if tiro1 > tiro2:
                if self.val_mod_attacco.get() == 'vantaggio':
                    # return tiro1 + modif_per_colpire
                    self.attack_result += str(tiro1 + self.modif_tiro_per_colpire.get())
                    if tiro1 == 20:
                        self.attack_result += "\tCritico!"
                    elif tiro1 == 1:
                        self.attack_result += "\tAnticritico!"
                    print('vant - 1 ' + str(tiro1))
                else:
                    # return tiro2 + modif_per_colpire
                    self.attack_result += str(tiro2 + self.modif_tiro_per_colpire.get())
                    if tiro2 == 20:
                        self.attack_result += "\tCritico!"
                    elif tiro2 == 1:
                        self.attack_result += "\tAnticritico!"
                    print('svant - 2 ' + str(tiro2))
            else:
                if self.val_mod_attacco.get() == 'vantaggio':
                    # return tiro2 + modif_per_colpire
                    self.attack_result += str(tiro2 + self.modif_tiro_per_colpire.get())
                    if tiro2 == 20:
                        self.attack_result += "\tCritico!"
                    elif tiro2 == 1:
                        self.attack_result += "\tAnticritico!"
                    print('vant - 2 ' + str(tiro2))
                else:
                    # return tiro1 + modif_per_colpire
                    self.attack_result += str(tiro1 + self.modif_tiro_per_colpire.get())
                    if tiro1 == 20:
                        self.attack_result += "\tCritico!"
                    elif tiro1 == 1:
                        self.attack_result += "\tAnticritico!"
                    print('svant - 1 ' + str(tiro1))
        else:
            # return rolla(20) + self.modif_tiro_per_colpire
            tiro = rolla(20)
            self.attack_result += str(tiro + self.modif_tiro_per_colpire.get())
            if tiro == 20:
                self.attack_result += "\tCritico!"
            elif tiro == 1:
                self.attack_result += "\tAntiritico!"
            print("tiro normale = " + self.attack_result)
        self.attack_result += "\n\n"

    def attacco(self):
        # -roll dado_attacco
        # -add costante attacco
        # -printa risultato attacco diviso per tipo e con totale

        self.attack_result = ""
        self.label_result_attacco.config(text=self.attack_result)

        self.tiro_per_colpire()

        totale_danno = 0

        print(self.attack_result)

        if "Critico!" in self.attack_result:
            totale_danno += self.sequenza_attacchi()
            self.attack_result += "\n"
            totale_danno += self.sequenza_attacchi()
        else:
            totale_danno += self.sequenza_attacchi()

        self.attack_result += "\nTotale: " + str(totale_danno)
        self.label_result_attacco.config(text=self.attack_result)

    def sequenza_attacchi(self):
        lista_colpi = self.entry_attacco.get().split(',')
        tot = 0
        for tipo_attacco in range(0, len(lista_colpi)):  # numero di attacchi di tipo diverso
            attacco = 0
            for roll in range(0, int(lista_colpi[tipo_attacco].split('d')[0])):  # numero dadi attacco
                attacco += rolla(int(lista_colpi[tipo_attacco].split('d')[1].split('+')[0]))  # tipo dado attacco

            try:
                attacco += int(lista_colpi[tipo_attacco].split('d')[1].split('+')[1])  # costante additiva attacco
            except:
                pass
            self.attack_result += "attacco: " + str(attacco) + "\n"
            tot += attacco

        self.label_result_attacco.config(text=self.attack_result)
        return tot

    def undo_danno(self):
        self.punti_ferita = self.punti_ferita_momentanei
        self.entry_pf_mostro.delete(0, "end")
        self.entry_pf_mostro.insert(0, self.punti_ferita)
        print(self.punti_ferita)
        print(self.punti_ferita_momentanei)

    def subisci_attacco(self):
        # fa backup dei pf per l'undo
        # -sottrae alla vita i punti ferita
        # -mostra i punti ferita aggiornati

        self.punti_ferita = self.pf_mostro.get()
        self.punti_ferita_momentanei = self.punti_ferita
        self.punti_ferita -= self.val_danno_subito.get()
        self.entry_pf_mostro.delete(0, "end")
        self.entry_pf_mostro.insert(0, self.punti_ferita)
        print(self.punti_ferita)
        print(self.punti_ferita_momentanei)

