from PySide2 import QtCore, QtWidgets


class FileWindowClass(object):
    def __init__(self, file_window):
        self.file_window = file_window
        self.gridLayout = QtWidgets.QGridLayout(self.file_window)
        self.add_button = QtWidgets.QPushButton(self.file_window)
        self.remove_button = QtWidgets.QPushButton(self.file_window)
        # self.close_button = QtWidgets.QPushButton(self.file_window)
        self.file_list = QtWidgets.QListWidget(self.file_window)
        self.last_file = None

    def window_setup(self):
        self.file_window.setObjectName("file_window")
        self.file_window.setWindowModality(QtCore.Qt.NonModal)
        self.file_window.resize(320, 240)
        #
        # self.file_window.setMinimumSize(QtCore.QSize(320, 240))
        # self.file_window.setMaximumSize(QtCore.QSize(320, 240))

        # set that you could drag, drop and select images in the file list
        self.file_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.file_list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        self.gridLayout.addWidget(self.add_button, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.remove_button, 0, 1, 1, 1)
        # self.gridLayout.addWidget(self.close_button, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.file_list, 1, 0, 1, 2)

        self.text_setup()
        QtCore.QObject.connect(self.add_button, QtCore.SIGNAL("clicked()"), self.add_file)
        # QtCore.QObject.connect(self.close_button, QtCore.SIGNAL("clicked()"), self.file_window.close)
        QtCore.QObject.connect(self.remove_button, QtCore.SIGNAL("clicked()"), self.remove_item)
        QtCore.QMetaObject.connectSlotsByName(self.file_window)

    # function that sets up all the titles and texts in the window
    def text_setup(self):
        self.file_window.setWindowTitle("OpenPIV file")
        self.add_button.setText("Add")
        self.remove_button.setText("Remove")
        # self.close_button.setText(QtWidgets.QApplication.translate("file_window", "Close", None, -1))

    # the function that add the files when the add button is clicked
    def add_file(self):
        self.last_file = QtWidgets.QFileDialog.getOpenFileNames(self.file_list, path=QtCore.QDir,
                                                               filter=('images(*.png *.jpg *.jpeg *.bmp *.tif *.tiff)'))
        if self.last_file != '':
            self.file_list.addItem(QtCore.QFileInfo(str(self.last_file)).fileName())

    # the function that remove selected files when the remove button is clicked
    def remove_item(self):
        for selected_item in self.file_list.selectedItems():
            self.file_list.takeItem(self.file_list.row(selected_item))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    file_window = QtWidgets.QWidget()
    file_window_class = FileWindowClass(file_window)
    file_window_class.window_setup()
    file_window.show()
    sys.exit(app.exec_())
