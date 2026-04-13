from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal, Slot, QThread
from ui_workerui import Ui_MyWidget
import sys
import time

class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_MyWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        
        self.button_1.clicked.connect(self.hardWork1)
        self.button_2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread

        # mover o worker para a thread
        worker.moveToThread(thread)

        # conectando no método run
        thread.started.connect(worker.run)
        
        # desconectando do run
        worker.finished.connect(thread.quit)

        # eliminando rresquicios da memória 
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)
        thread.start()

    def worker1Started(self, value):
        self.button_1.setDisabled(True)
        self.label_1.setText(value)
        print('worker iniciado')

    def worker1Progressed(self,value):
        self.label_1.setText(value)
        print('worker em progresso')

    def worker1Finished(self,value):
        self.button_1.setDisabled(False)
        self.label_1.setText(value)
        print('worker finalizado')
        

    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        # mover o worker para a thread
        worker.moveToThread(thread)

        # conectando no método run
        thread.started.connect(worker.run)
        
        # desconectando do run
        worker.finished.connect(thread.quit)

        # eliminando rresquicios da memória 
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)
        thread.start()

    def worker2Started(self, value):
        self.button_2.setDisabled(True)
        self.label_2.setText(value)
        print('worker 2 iniciado')

    def worker2Progressed(self,value):
        self.label_2.setText(value)
        print('worker 2 em progresso')

    def worker2Finished(self,value):
        self.button_2.setDisabled(False)
        self.label_2.setText(value)
        print('worker 2 finalizado')
        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
