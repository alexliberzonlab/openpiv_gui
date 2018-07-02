from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    # set up function for the gui
    def setupUi(self, MainWindow):
        # MainWindow = widget of the gui
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 484)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)

        # icon = the icon top left (i will fix it later)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/openpiv_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Israel))
        MainWindow.setIconSize(QtCore.QSize(174, 79))

        # centeral_widget = everything under the menu bar
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setAutoFillBackground(False)
        self.central_widget.setObjectName("central_widget")
        MainWindow.setCentralWidget(self.central_widget)

        # menu_bar = the menu bars in the top
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1068, 21))
        self.menu_bar.setMouseTracking(False)
        self.menu_bar.setObjectName("menu_bar")

        # menu_file = the file menu bar in the top
        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.menu_bar)

        # status_bar = the vertical layout for the menu bars
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)

        # action_test = one of the options in the file menu
        self.action_test = QtWidgets.QAction(MainWindow)
        self.action_test.setObjectName("action_test")
        self.menu_file.addAction(self.action_test)
        self.menu_bar.addAction(self.menu_file.menuAction())

        # writing all the titles/texts
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "OpenPIV", None, -1))
        self.menu_file.setTitle(QtWidgets.QApplication.translate("MainWindow", "file", None, -1))
        self.action_test.setText(QtWidgets.QApplication.translate("MainWindow", "test", None, -1))

        # connecting everything to the widget
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    import sys
    # creating the widget
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
