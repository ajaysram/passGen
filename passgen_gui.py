from PyQt5 import QtCore, QtWidgets
import random
import string

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 233)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 90, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        self.passwordPlaceholder = QtWidgets.QLabel(self.centralwidget)
        self.passwordPlaceholder.setGeometry(QtCore.QRect(150, 40, 251, 51))
        self.passwordPlaceholder.setStyleSheet("font-size:20px;")
        self.passwordPlaceholder.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordPlaceholder.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.passwordPlaceholder.setObjectName("passwordPlaceholder")
        self.helpText = QtWidgets.QLabel(self.centralwidget)
        self.helpText.setGeometry(QtCore.QRect(160, 170, 251, 17))
        self.helpText.setStyleSheet("color:rgb(46, 52, 54);")
        self.helpText.setObjectName("helpText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "passGen"))
        self.pushButton.setText(_translate("MainWindow", "Get a new password"))
        self.passwordPlaceholder.setText(_translate("MainWindow", "CLICK TO GET PASSWORD"))
        self.helpText.setText(_translate("MainWindow", "Passwords are copied to clipboard"))

    def on_click(self):
        password = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$*_&") for _ in range(16))
        self.passwordPlaceholder.setText(password)
        QtWidgets.QApplication.clipboard().setText(password)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
