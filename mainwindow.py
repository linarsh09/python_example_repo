import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = QWidget
        self.setWindowTitle("Меню")
        self.setGeometry(200, 200, 200, 200)
        self.newgame_button = QPushButton("Новая игра")
        self.settings_button = QPushButton("Настройки")
        self.records_button = QPushButton("Рекорд")
        self.exit_button = QPushButton("Выход")
        
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.layout.addWidget(self.newgame_button)
        self.layout.addWidget(self.settings_button)
        self.layout.addWidget(self.records_button)
        self.layout.addWidget(self.exit_button)

