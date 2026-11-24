import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMainWindow, QCheckBox

from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 700)
        self.checkbox = QCheckBox("Do You Like food?", self)
        self.initUI()


    def initUI(self):
        self.checkbox.setGeometry(0, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family:  Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)




    def checkbox_changed(self, state):
        # print(state) # this gives value when value is checked [in this case it would be 2]
        if state == 2:    
            print("You Like Food")
        else:
            print("You do not like food")






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys,exit(app.exec_())


if __name__ == "__main__":
    main()

