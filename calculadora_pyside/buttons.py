from PySide6.QtWidgets import QGridLayout, QPushButton
# ... outras importações necessárias (Display, Info, etc)

class ButtonsGrid(QGridLayout):
    def __init__(self, display, info, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.display = display
        self.info = info
        self.window = window
        
        # Sua lógica de botões aqui...
        self._makeGrid()

    def _makeGrid(self):
        # Exemplo simplificado de criação para teste
        # Se sua lógica de máscara estiver falhando, o app não abre
        buttons = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', 'C', '0', '=', '/']
        
        row, col = 0, 0
        for text in buttons:
            btn = QPushButton(text)
            self.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1