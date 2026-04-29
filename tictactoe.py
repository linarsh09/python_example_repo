import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class TTT(QWidget):
    def __init__(self):
        super().__init__()

        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        grid = QGridLayout()

        for row in range(3):
            for col in range(3):
                buttons = QPushButton("")
                buttons.setFixedSize(100,100)
                self.buttons [row][col] = buttons
                buttons.clicked.connect(lambda _, r=row, c=col: self.handle_click(r,c))              
                grid.addWidget(buttons, row, col)
        self.setLayout(grid)
    
    def handle_click(self,row,col):
        button = self.buttons[row][col]

        if button.text() == "":
            button.setText(self.current_player)

            self.current_player = "0" if self.current_player == "X" else "X"

if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = TTT()
    window.show()
    sys.exit(app.exec_())