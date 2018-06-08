import sys

from PyQt5 import QtCore, QtGui
from test1gui import Ui_Form


class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.helloworld)

    def helloworld(self):
        self.ui.textEdit.setText(“Hello world”)

if __name__ == “__main__”:
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())        print (‘Hello world again’)