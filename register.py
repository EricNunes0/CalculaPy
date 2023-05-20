import tkinter

cadastros = []

class MyWindow:
    def __init__(self, win):
        self.win = win
        self.win.title("Cadastro")
        self.win.geometry("320x560")
        self.bgColor = "#f0f0f0"
        self.win.configure(background=self.bgColor)

        self.labelN = tkinter.Label(self.win, text="Nome completo", font="Arial 14", bg=self.bgColor, fg="#000")
        self.labelN.place(x=10, y=10, width=300, height=20)

        self.entryN = tkinter.Entry(self.win, font="Arial 18", border="2px solid")
        self.entryN.place(x=10, y=30, width=300, height=40)

        self.labelD = tkinter.Label(self.win, text="Data de nascimento", font="Arial 14", bg=self.bgColor, fg="#000")
        self.labelD.place(x=10, y=80, width=300, height=20)

        self.days = []
        for i in range(1, 32):
            self.days.append(f"{i}")
        self.day = tkinter.StringVar(self.win)
        self.day.set(self.days[0])
        self.day.set("Dia")

        self.entryD1 = tkinter.OptionMenu(self.win, self.day, *self.days)
        self.entryD1['menu'].configure(font=('Arial', 12), activeborderwidth=10)
        self.entryD1.configure(font=('Arial', 12))
        self.entryD1.place(x=10, y=100, width=100, height=40)

        self.months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro",
                       "Outubro", "Novembro", "Dezembro"]
        self.month = tkinter.StringVar(self.win)
        self.month.set(self.months[0])
        self.month.set("Mês")

        self.entryD2 = tkinter.OptionMenu(self.win, self.month, *self.months)
        self.entryD2['menu'].configure(font=('Arial', 12), activeborderwidth=10)
        self.entryD2.configure(font=('Arial', 12))
        self.entryD2.place(x=110, y=100, width=100, height=40)

        self.years = []
        for i in range(2010, 1920, -1):
            self.years.append(f"{i}")
        self.year = tkinter.StringVar(self.win)
        self.year.set(self.years[0])
        self.year.set("Ano")

        self.entryD3 = tkinter.OptionMenu(self.win, self.year, *self.years)
        self.entryD3['menu'].configure(font=('Arial', 12), activeborderwidth=10)
        self.entryD3.configure(font=('Arial', 12))
        self.entryD3.place(x=210, y=100, width=100, height=40)

        self.labelE = tkinter.Label(self.win, text="E-mail", font="Arial 14", bg=self.bgColor, fg="#000")
        self.labelE.place(x=10, y=150, width=300, height=20)

        self.entryE = tkinter.Entry(self.win, font="Arial 18", border="2px solid")
        self.entryE.place(x=10, y=170, width=300, height=40)

        self.labelN1 = tkinter.Label(self.win, text="Nota 1", font="Arial 14", bg=self.bgColor, fg="#000")
        self.labelN1.place(x=10, y=220, width=150, height=20)

        self.entryN1 = tkinter.Entry(self.win, font="Arial 18", border="2px solid")
        self.entryN1.place(x=10, y=240, width=150, height=40)

        self.labelN2 = tkinter.Label(self.win, text="Nota 2", font="Arial 14", bg=self.bgColor, fg="#000")
        self.labelN2.place(x=160, y=220, width=150, height=20)

        self.entryN2 = tkinter.Entry(self.win, font="Arial 18", border="2px solid")
        self.entryN2.place(x=160, y=240, width=150, height=40)

        self.btnTheme = tkinter.Button(self.win, cursor="hand2", text="Cadastrar", font="Arial 14", border="2px solid", command=lambda: self.registerUser())
        self.btnTheme.place(x=10, y=290, width=300, height=40)

        self.labelPrint = tkinter.Label(self.win, text="", bg=self.bgColor, font="Arial 10")
        self.labelPrint.place(x=10, y=340, width=300, height=20)

        self.searchN = tkinter.Label(self.win, text="Pesquisar por nome", font="Arial 14", bg=self.bgColor, fg="#000")
        self.searchN.place(x=10, y=370, width=300, height=20)

        self.entrySearchN = tkinter.Entry(self.win, font="Arial 18", border="2px solid")
        self.entrySearchN.place(x=10, y=400, width=300, height=40)

        self.btnPrint = tkinter.Button(self.win, cursor="hand2", text="Exibir", font="Arial 14", border="2px solid", command=lambda: self.getUsers())
        self.btnPrint.place(x=10, y=450, width=300, height=40)

        self.labelMedia = tkinter.Label(self.win, text="", bg=self.bgColor, font="Arial 14")
        self.labelMedia.place(x=10, y=500, width=300, height=20)

        self.win.mainloop()

    def registerUser(self):
        if len(self.entryN.get()) == 0:
            self.entryN.config(highlightthickness=2, highlightbackground="#ff2020", highlightcolor="#ff2020")
            self.labelPrint.config(text="É necessário informar o seu nome completo", fg="#ff2020")
            return
        self.entryN.config(highlightthickness=0, highlightbackground="#000", highlightcolor="#000")

        if self.day.get() == "Dia":
            self.entryD1.config(highlightthickness=2, highlightbackground="#ff2020", highlightcolor="#ff2020")
            self.labelPrint.config(text="É necessário informar sua data de nascimento", fg="#ff2020")
            return
        self.entryD1.config(highlightthickness=0, highlightbackground="#000", highlightcolor="#000")

        if self.month.get() == "Mês":
            self.entryD2.config(highlightthickness=2, highlightbackground="#ff2020", highlightcolor="#ff2020")
            self.labelPrint.config(text="É necessário informar sua data de nascimento", fg="#ff2020")
            return
        self.entryD2.config(highlightthickness=0, highlightbackground="#000", highlightcolor="#000")

        if self.year.get() == "Ano":
            self.entryD3.config(highlightthickness=2, highlightbackground="#ff2020", highlightcolor="#ff2020")
            self.labelPrint.config(text="É necessário informar sua data de nascimento", fg="#ff2020")
            return
        self.entryD3.config(highlightthickness=0, highlightbackground="#000", highlightcolor="#000")

        if len(self.entryE.get()) == 0:
            self.entryE.config(highlightthickness=2, highlightbackground="#ff2020", highlightcolor="#ff2020")
            self.labelPrint.config(text="É necessário informar o seu e-mail", fg="#ff2020")
            return
        self.entryE.config(highlightthickness=0, highlightbackground="#000", highlightcolor="#000")

        try:
            n1 = float(self.entryN1.get())
        except Exception as e:
            self.entryN1.config(highlightthickness=2, highlightbackground="#ff2020", highlightcolor="#ff2020")
            self.labelPrint.config(text="É necessário informar a primeira nota", fg="#ff2020")
            return
        self.entryN1.config(highlightthickness=0, highlightbackground="#000", highlightcolor="#000")
        try:
            n2 = float(self.entryN2.get())
        except Exception as e:
            self.entryN2.config(highlightthickness=2, highlightbackground="#ff2020", highlightcolor="#ff2020")
            self.labelPrint.config(text="É necessário informar a segunda nota", fg="#ff2020")
            return
        self.entryN2.config(highlightthickness=0, highlightbackground="#000", highlightcolor="#000")
        media = (n1 + n2) / 2
        self.labelPrint.config(text="Aluno cadastrado!", fg="#20ff20")

        cadastros.append({
            "name": self.entryN.get(),
            "date": self.day.get() + "/" + self.month.get() + "/" + self.year.get(),
            "email": self.entryE.get(),
            "nota1": float(self.entryN1.get()),
            "nota2": float(self.entryN2.get()),
            "media": media
        })

    def getUsers(self):
        if len(self.entrySearchN.get()) == 0:
            self.labelPrint.config(text="Informe o nome do aluno", fg="#ff2020")
            return
        if len(cadastros) == 0:
            self.labelPrint.config(text="Não há usuários cadastrados", fg="#ff2020")
            return
        self.labelPrint.config(text="", fg="#ff2020")
        nameSearch = self.entrySearchN.get()
        for i in range(0, len(cadastros)):
            if cadastros[i]['name'].lower() == nameSearch.lower():
                self.labelMedia.config(text = f"Média do aluno: {cadastros[i]['media']}")
                return
        self.labelPrint.config(text="Aluno não encontrado", fg="#ff2020")
        return


myTk = tkinter.Tk()
MyWindow(myTk)
