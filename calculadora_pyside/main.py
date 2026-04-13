import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                             QWidget, QPushButton, QGridLayout, QLineEdit)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QKeyEvent

# ESTILO
ESTILO_DARK = """
    QMainWindow {
        background-color: #1e1e1e;
    }
    QLineEdit {
        background-color: #252526;
        color: #ffffff;
        border: none;
        padding: 20px;
        font-size: 32px;
        font-weight: bold;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    QPushButton {
        background-color: #333333;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 25px;
        min-width: 50px;
        min-height: 50px;
    }
    QPushButton:hover {
        background-color: #444444;
    }
    QPushButton#operacao {
        background-color: #ff9500;
        color: white;
    }
    QPushButton#operacao:hover {
        background-color: #ffaa33;
    }
    QPushButton#igual {
        background-color: #2d9d58;
    }
    QPushButton#limpar {
        background-color: #d32f2f;
    }
"""

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Pro")
        self.setMinimumSize(320, 450)
        
        # Widget Central
        self.cw = QWidget()
        self.setCentralWidget(self.cw)
        self.layout = QVBoxLayout(self.cw)
        self.layout.setContentsMargins(15, 15, 15, 15)

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        # Grid de Botões
        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)
        self.make_buttons()

    def make_buttons(self):
        botoes = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', 'back', '=']
        ]

        for row, line in enumerate(botoes):
            for col, text in enumerate(line):
                btn = QPushButton(text)
                
                # Definindo Estilos Específicos por ID
                if text in '/+*-': btn.setObjectName("operacao")
                elif text == '=': btn.setObjectName("igual")
                elif text == 'C': btn.setObjectName("limpar")
                
                btn.clicked.connect(lambda checked=False, t=text: self.process_click(t))
                self.grid.addWidget(btn, row, col)

    def process_click(self, text):
        atual = self.display.text()

        if text == 'C':
            self.display.clear()
        elif text == 'back':
            self.display.setText(atual[:-1])
        elif text == '=':
            try:
                # Substitui 'x' e '÷' se necessário para o eval funcionar
                expressao = atual.replace(' ', '')
                resultado = str(eval(expressao))
                self.display.setText(resultado)
            except Exception:
                self.display.setText("Erro")
        else:
            self.display.setText(atual + text)

    #  SUPORTE AO TECLADO 
    def keyPressEvent(self, event: QKeyEvent):
        key = event.text()
        code = event.key()

       # mapeamento das teclas
        if key in "0123456789.+-*/()":
            self.process_click(key)
        elif code in (Qt.Key_Return, Qt.Key_Enter):
            self.process_click('=')
        elif code == Qt.Key_Backspace:
            self.process_click('back')
        elif code == Qt.Key_Escape:
            self.process_click('C')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(ESTILO_DARK) 
    
    janela = Calculadora()
    janela.show()
    
   
    sys.exit(app.exec())