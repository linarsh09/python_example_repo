from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.label_player1 = QtWidgets.QLabel("Игрок 1")
        self.label_player2 = QtWidgets.QLabel("Игрок 2")
        self.layout.addWidget(self.label_player1)
        self.layout.addWidget(self.label_player2)

        self.board = QtWidgets.QGridLayout()
        self.board.setSpacing(0)
        for row in range(8):
            for col in range(8):
                cell = QtWidgets.QLabel()
                cell.setFixedSize(60, 60)
                cell.setAlignment(Qt.AlignCenter)
                if (row + col) % 2 == 0:
                    cell.setStyleSheet("background-color: #EEEED2")
                else:
                    cell.setStyleSheet("background-color: #769656")
                self.board.addWidget(cell, row, col)
        self.layout.addLayout(self.board)





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
 
