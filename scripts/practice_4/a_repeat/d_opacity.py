import os

from PySide6 import QtWidgets, QtCore, QtGui

from conf import ROOT_FOLDER


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)  # Удаление titleBar
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)  # Установка прозрачного фона

        # добавление эффекта тени
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(10)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

        #
        label = QtWidgets.QLabel()
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        label.setPixmap(QtGui.QPixmap(os.path.join(ROOT_FOLDER, 'static', 'ico', "64.png")))
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(QtWidgets.QPushButton("123156"))

        self.setLayout(layout)

        # self.setStyleSheet('border: 5px solid black; background-image: "64.png"')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
