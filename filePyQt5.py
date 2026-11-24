import sys
# sys --- System-specfic parameters and functions

# sys module provides access to some variables used or  maintained by the interpreter and to functions
# That interact strongly with the interpreter.It is always available

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(500, 100, 500, 500)
                        #(x, y, width, height)
        self.setWindowIcon(QIcon("tlok.jpg")) 

def main():
    app = QApplication(sys.argv)
    # sys.argv The list of command line arguments passed to a python script.argv[0] is the
    # script name(it is operating system dependent whether this is a full pathname or not).

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()