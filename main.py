import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Основное окно')
        self.resize(300, 200)

#app = QApplication(sys.argv)
app = QtWidgets.QApplication()


#window = QWidget()
window = MainWindow()
#window.setWindowTitle('Простейшее окно')
window.show()
app.exec()
#sys.exit(app.exec())