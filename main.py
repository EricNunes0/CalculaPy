import tkinter

class MyWindow:
    def __init__(self, win):
        self.win = win
        self.theme = 0

        self.conta = tkinter.Label(self.win, font = "Arial 14", fg = "#808080", justify = tkinter.RIGHT)
        self.conta.place(x = 10, y = 10, width = 300, height = 20)

        self.resultado = tkinter.Entry(self.win, font = "Arial 28", bg = "#f0f0f0", justify = tkinter.RIGHT, border = "0px solid")
        self.resultado.place(x = 10, y = 30, width = 300, height = 40)
        self.resultado.insert(0, 0)

        self.btnTheme = tkinter.Button(self.win, cursor = "hand2", text = "☀", font = "Arial 12", bg = "#d0d0d0", border = "1px solid", command = lambda:self.changeTheme())
        self.btnTheme.place(x = 10, y = 10, width = 25, height = 25)

        btnWidth = 71
        btnHeight = 71
        btnPosX = 12
        btnPosY = 82
        btnProX = 75
        btnProY = 75
        btnBorder = "0px raised"

        fontFamily = "Arial 14"
        btnBg = "#fff"
        btnBgGray = "#fafafa"
        btnBgD = "#3a3a3a"
        btnBgGrayD = "#404040"

        self.btnPercent = tkinter.Button(self.win, cursor = "hand2", text = "%", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.addOperator("÷ 100 ×"))
        self.btnPercent.place(x = btnPosX + (btnProX * 0), y = btnPosY + (btnProY * 0), width = btnWidth, height = btnHeight)
        self.btnCE = tkinter.Button(self.win, cursor = "hand2", text = "CE", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.clearResult())
        self.btnCE.place(x = btnPosX + (btnProX * 1), y = btnPosY + (btnProY * 0), width = btnWidth, height = btnHeight)
        self.btnC = tkinter.Button(self.win, cursor = "hand2", text = "C", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.clearAll())
        self.btnC.place(x = btnPosX + (btnProX * 2), y = btnPosY + (btnProY * 0), width = btnWidth, height = btnHeight)
        self.btnBackspace = tkinter.Button(self.win, cursor = "hand2", text = "X", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.backspace())
        self.btnBackspace.place(x = btnPosX + (btnProX * 3), y = btnPosY + (btnProY * 0), width = btnWidth, height = btnHeight)

        self.btnFraction = tkinter.Button(self.win, cursor = "hand2", text = "⅟", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.fractionNumerator())
        self.btnFraction.place(x = btnPosX + (btnProX * 0), y = btnPosY + (btnProY * 1), width = btnWidth, height = btnHeight)
        self.btnExp = tkinter.Button(self.win, cursor = "hand2", text = "xʸ", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.addOperator("^"))
        self.btnExp.place(x = btnPosX + (btnProX * 1), y = btnPosY + (btnProY * 1), width = btnWidth, height = btnHeight)
        self.btnRaiz = tkinter.Button(self.win, cursor = "hand2", text = "²√x", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.raiz())
        self.btnRaiz.place(x = btnPosX + (btnProX * 2), y = btnPosY + (btnProY * 1), width = btnWidth, height = btnHeight)
        self.btnDiv = tkinter.Button(self.win, cursor = "hand2", text = "÷", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.addOperator("÷"))
        self.btnDiv.place(x = btnPosX + (btnProX * 3), y = btnPosY + (btnProY * 1), width = btnWidth, height = btnHeight)

        self.btn7 = tkinter.Button(self.win, cursor = "hand2", text = "7", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(7))
        self.btn7.place(x = btnPosX + (btnProX * 0), y = btnPosY + (btnProY * 2), width = btnWidth, height = btnHeight)
        self.btn8 = tkinter.Button(self.win, cursor = "hand2", text = "8", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(8))
        self.btn8.place(x = btnPosX + (btnProX * 1), y = btnPosY + (btnProY * 2), width = btnWidth, height = btnHeight)
        self.btn9 = tkinter.Button(self.win, cursor = "hand2", text = "9", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(9))
        self.btn9.place(x = btnPosX + (btnProX * 2), y = btnPosY + (btnProY * 2), width = btnWidth, height = btnHeight)
        self.btnMult = tkinter.Button(self.win, cursor = "hand2", text = "×", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.addOperator("×"))
        self.btnMult.place(x = btnPosX + (btnProX * 3), y = btnPosY + (btnProY * 2), width = btnWidth, height = btnHeight)

        self.btn4 = tkinter.Button(self.win, cursor = "hand2", text = "4", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(4))
        self.btn4.place(x = btnPosX + (btnProX * 0), y = btnPosY + (btnProY * 3), width = btnWidth, height = btnHeight)
        self.btn5 = tkinter.Button(self.win, cursor = "hand2", text = "5", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(5))
        self.btn5.place(x = btnPosX + (btnProX * 1), y = btnPosY + (btnProY * 3), width = btnWidth, height = btnHeight)
        self.btn6 = tkinter.Button(self.win, cursor = "hand2", text = "6", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(6))
        self.btn6.place(x = btnPosX + (btnProX * 2), y = btnPosY + (btnProY * 3), width = btnWidth, height = btnHeight)
        self.btnSub = tkinter.Button(self.win, cursor = "hand2", text = "-", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.addOperator("-"))
        self.btnSub.place(x = btnPosX + (btnProX * 3), y = btnPosY + (btnProY * 3), width = btnWidth, height = btnHeight)

        self.btn1 = tkinter.Button(self.win, cursor = "hand2", text = "1", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(1))
        self.btn1.place(x = btnPosX + (btnProX * 0), y = btnPosY + (btnProY * 4), width = btnWidth, height = btnHeight)
        self.btn2 = tkinter.Button(self.win, cursor = "hand2", text = "2", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(2))
        self.btn2.place(x = btnPosX + (btnProX * 1), y = btnPosY + (btnProY * 4), width = btnWidth, height = btnHeight)
        self.btn3 = tkinter.Button(self.win, cursor = "hand2", text = "3", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(3))
        self.btn3.place(x = btnPosX + (btnProX * 2), y = btnPosY + (btnProY * 4), width = btnWidth, height = btnHeight)
        self.btnSum = tkinter.Button(self.win, cursor = "hand2", text = "+", font = fontFamily, bg = btnBgGray, border = btnBorder, command = lambda:self.addOperator("+"))
        self.btnSum.place(x = btnPosX + (btnProX * 3), y = btnPosY + (btnProY * 4), width = btnWidth, height = btnHeight)

        self.btnInvert = tkinter.Button(self.win, cursor = "hand2", text = "+/-", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.invert())
        self.btnInvert.place(x = btnPosX + (btnProX * 0), y = btnPosY + (btnProY * 5), width = btnWidth, height = btnHeight)
        self.btn0 = tkinter.Button(self.win, cursor = "hand2", text = "0", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit(0))
        self.btn0.place(x = btnPosX + (btnProX * 1), y = btnPosY + (btnProY * 5), width = btnWidth, height = btnHeight)
        self.btnComma = tkinter.Button(self.win, cursor = "hand2", text = ",", font = fontFamily, bg = btnBg, border = btnBorder, command = lambda:self.addNumberDigit("."))
        self.btnComma.place(x = btnPosX + (btnProX * 2), y = btnPosY + (btnProY * 5), width = btnWidth, height = btnHeight)
        self.btnEqual = tkinter.Button(self.win, cursor = "hand2", text = "=", font = fontFamily, bg = "#205aca", fg = "#fff", border = btnBorder, command = lambda:self.calculate())
        self.btnEqual.place(x = btnPosX + (btnProX * 3), y = btnPosY + (btnProY * 5), width = btnWidth, height = btnHeight)

        def on_enter(btn):
            if self.theme == 0:
                btn.widget["background"] = "#f5f5f5"
            elif self.theme == 1:
                btn.widget["background"] = "#353535"
        def on_leave(btn):
            if self.theme == 0:
                btn.widget["background"] = btnBg
            elif self.theme == 1:
                btn.widget["background"] = btnBgD
        def on_leaveGray(btn):
            if self.theme == 0:
                btn.widget["background"] = btnBgGray
            if self.theme == 1:
                btn.widget["background"] = btnBgGrayD

        self.btnPercent.bind("<Enter>", on_enter)
        self.btnPercent.bind("<Leave>", on_leaveGray)
        self.btnCE.bind("<Enter>", on_enter)
        self.btnCE.bind("<Leave>", on_leaveGray)
        self.btnC.bind("<Enter>", on_enter)
        self.btnC.bind("<Leave>", on_leaveGray)
        self.btnBackspace.bind("<Enter>", on_enter)
        self.btnBackspace.bind("<Leave>", on_leaveGray)
        self.btnFraction.bind("<Enter>", on_enter)
        self.btnFraction.bind("<Leave>", on_leaveGray)
        self.btnExp.bind("<Enter>", on_enter)
        self.btnExp.bind("<Leave>", on_leaveGray)
        self.btnRaiz.bind("<Enter>", on_enter)
        self.btnRaiz.bind("<Leave>", on_leaveGray)
        self.btnDiv.bind("<Enter>", on_enter)
        self.btnDiv.bind("<Leave>", on_leaveGray)
        self.btn7.bind("<Enter>", on_enter)
        self.btn7.bind("<Leave>", on_leave)
        self.btn8.bind("<Enter>", on_enter)
        self.btn8.bind("<Leave>", on_leave)
        self.btn9.bind("<Enter>", on_enter)
        self.btn9.bind("<Leave>", on_leave)
        self.btnMult.bind("<Enter>", on_enter)
        self.btnMult.bind("<Leave>", on_leaveGray)
        self.btn4.bind("<Enter>", on_enter)
        self.btn4.bind("<Leave>", on_leave)
        self.btn5.bind("<Enter>", on_enter)
        self.btn5.bind("<Leave>", on_leave)
        self.btn6.bind("<Enter>", on_enter)
        self.btn6.bind("<Leave>", on_leave)
        self.btnSub.bind("<Enter>", on_enter)
        self.btnSub.bind("<Leave>", on_leaveGray)
        self.btn1.bind("<Enter>", on_enter)
        self.btn1.bind("<Leave>", on_leave)
        self.btn2.bind("<Enter>", on_enter)
        self.btn2.bind("<Leave>", on_leave)
        self.btn3.bind("<Enter>", on_enter)
        self.btn3.bind("<Leave>", on_leave)
        self.btnSum.bind("<Enter>", on_enter)
        self.btnSum.bind("<Leave>", on_leaveGray)
        self.btnInvert.bind("<Enter>", on_enter)
        self.btnInvert.bind("<Leave>", on_leave)
        self.btn0.bind("<Enter>", on_enter)
        self.btn0.bind("<Leave>", on_leave)
        self.btnComma.bind("<Enter>", on_enter)
        self.btnComma.bind("<Leave>", on_leave)

        self.win.title("CalculaPy")
        self.win.geometry("320x540")
        self.win.mainloop()

    def addNumberDigit(self, num):
        self.num = num
        resultado = str(self.resultado.get())
        if len(resultado) >= 14:
            return
        if self.num == 0:
            if resultado.startswith("0"):
                return
        else:
            if resultado.startswith("0"):
                self.resultado.delete(0, "end")
        self.resultado.insert("end", self.num)
    
    def addOperator(self, operator: str):
        conta = self.conta.cget("text")
        resultado = str(self.resultado.get())
        if len(conta) == 0:
            self.conta.config(text = f"{resultado} {operator}")
            self.resultado.delete(0, "end")
            self.resultado.insert(0, 0)
        else:
            self.calculate()
            resultado = str(self.resultado.get())
            self.conta.config(text = f"{resultado} {operator}")
            self.resultado.delete(0, "end")
            self.resultado.insert(0, 0)

    def clearResult(self):
        self.resultado.delete(0, "end")
        self.resultado.insert(0, 0)
    
    def clearAll(self):
        self.conta.config(text = "")
        self.resultado.delete(0, "end")
        self.resultado.insert(0, 0)

    def backspace(self):
        resultado = self.resultado.get()[:-1]
        self.resultado.delete(0, tkinter.END)
        if len(resultado) == 0:
            self.resultado.insert(0, 0)
        else:
            self.resultado.insert(0, resultado)

    def fractionNumerator(self):
        resultado = str(self.resultado.get())
        self.resultado.delete(0, "end")
        r = eval(f"1/{resultado}")
        self.resultado.insert(0, r)

    def raiz(self):
        resultado = str(self.resultado.get())
        self.resultado.delete(0, "end")
        r = eval(f"{resultado} ** 0.5")
        self.resultado.insert(0, r)

    def invert(self):
        try:
            resultado = int(self.resultado.get())
        except Exception as e:
            resultado = 0
        self.resultado.delete(0, tkinter.END)
        self.resultado.insert(0, -resultado)

    def calculate(self):
        conta = str(self.conta.cget("text"))
        resultado = str(self.resultado.get())
        contaSplitted = conta.split(" ")
        contaTxt = ""
        for s in contaSplitted:
            for i in range(len(s)):
                if s.startswith("0"):
                    s = s[1:]
            contaTxt += s
        for i in range(len(resultado)):
            if resultado.startswith("0"):
                resultado = resultado[1:]
        try:
            r = eval(contaTxt.replace("×", "*").replace("÷", "/").replace("^", "**") + resultado)
        except Exception as e:
            r = 0
        self.conta.config(text = "")
        self.resultado.delete(0, "end")
        self.resultado.insert(0, r)
    
    def changeTheme(self):
        if self.theme == 0:
            self.theme = 1
            self.win.configure(background = "#303030")
            self.btnTheme.configure(text = "🌙")
            self.conta.configure(background = "#303030", fg = "#b0b0b0")
            self.resultado.configure(background = "#303030", fg = "#fff")
            ic = self.win.winfo_children()
            for b in range(0, len(ic)):
                btnCheck = str(ic[b])
                if btnCheck.count("button") > 0:
                    bg = ic[b].cget("bg")
                    if bg == "#fff":
                        ic[b].configure(background = "#3a3a3a", fg = "#fff")
                    elif bg == "#fafafa":
                        ic[b].configure(background = "#404040", fg = "#fff")
        elif self.theme == 1:
            self.theme = 0
            self.win.configure(background = "#f0f0f0")
            self.btnTheme.configure(text = "☀")
            self.conta.configure(background = "#f0f0f0", fg = "#808080")
            self.resultado.configure(background = "#f0f0f0", fg = "#000")
            ic = self.win.winfo_children()
            for b in range(0, len(ic)):
                btnCheck = str(ic[b])
                if btnCheck.count("button") > 0:
                    bg = ic[b].cget("bg")
                    if bg == "#3a3a3a":
                        ic[b].configure(background = "#fff", fg = "#000")
                    elif bg == "#404040":
                        ic[b].configure(background = "#fafafa", fg = "#000")

calcTk = tkinter.Tk()
MyWindow(calcTk)