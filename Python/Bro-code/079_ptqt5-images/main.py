import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 720, 480)

        label = QLabel(self)
        label.setGeometry(0, 0, 100, 100)

        pixmap = QPixmap('../077_pyqt5_gui_app/ishiubafavicon.png')
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2, (self.height() - label.height()) // 2, label.width(), label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
