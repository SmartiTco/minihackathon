import sys
from PyQt5 import QtCore, QtGui , QtWidgets
from vue.mainwindow import Ui_MainWindow


class Main(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

        # Connect "add" button with a custom function (addInputTextToListbox)
        self.addButton.clicked.connect(self.addInputTextToListbox)

#    def addInputTextToListbox(self):
#        txt = self.myTextInput.text()
#        self.listWidget.addItem(txt)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = Main(dialog)

    dialog.show()
    sys.exit(app.exec_())