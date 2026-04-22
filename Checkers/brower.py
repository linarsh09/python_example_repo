from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QUrl
from  PyQt5.QtWebEngineWidgets import QWebEngineView
 




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl("https://google.kz"))
        self.layout.addWidget(self.webview)





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
 
