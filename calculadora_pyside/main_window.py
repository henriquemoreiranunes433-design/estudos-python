from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o widget central e layout
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # adjustSize calcula o tamanho ideal baseado nos widgets filhos
        self.adjustSize()
        # Fixa o tamanho para o usuário não conseguir redimensionar
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)