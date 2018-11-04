from weixinwork import Ui_Dialog
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
if __name__=='__main__':
	app=QtWidgets.QApplication(sys.argv)
	Form=QtWidgets.QWidget()
	ui=Ui_Dialog()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())