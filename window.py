from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.label_player1 = QtWidgets.QLabe("player 1")
        self.label_player2 = QtWidgets.QLabe("player 2")

        self.layout.addWidget(self.label_player1)
        self.layout.addWidget(self.label_player2)

        self.board = QtWidgets.QGridLayout()
        self.board.setSpacing(0)
        for row in range(8):
            for col in range(8):
                cell = QtWidgets.QLabel()
                cell.setFixedSeze(60,60)
                cell.setAligment(Qt.AlignCenter)
                if (row+col) % 2 == 0:
                    cell.setStyleSheet("""background-color: grey; """)
                else:
                    cell.setStyleSheet("""background-color: white; """)
                self.board.addWidget(cell, row, col)
        self.layout.addLayout(self.board)