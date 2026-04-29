import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.current_player = "X"
        self.button = [[None for _ in range(3)] for _ in range(3)]

        grid = QGridLayout()
        
        for row in range (3):
            for col in range (3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                self.button [row][col] = button
                
                button.clicked.connect(lambda _, r=row, c=col: self.handle_click(r, c))
                grid.addWidget(button, row, col)

                grid.addWidget(button, row, col)
        self.setLayout(grid)

    def handle_click(self, row, col):
        button = self.button[row][col]

        if button.text() == "":
            button.setText(self.current_player)

            if self.check_winner():
                QMessageBox.information(self, "Игра окончена",
                                        f"Игрок {self.current_player} победил!")
                self.reset_game()
                return

            if self.is_draw():
                QMessageBox.information(self, "Игра окончена", "Ничья!")
                self.reset_game()
                return

            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if (self.button[i][0].text() ==
                self.button[i][1].text() ==
                self.button[i][2].text() != ""):
                return True

        for i in range(3):
            if (self.button[0][i].text() ==
                self.button[1][i].text() ==
                self.button[2][i].text() != ""):
                return True

        if (self.button[0][0].text() ==
            self.button[1][1].text() ==
            self.button[2][2].text() != ""):
            return True

        if (self.button[0][2].text() ==
            self.button[1][1].text() ==
            self.button[2][0].text() != ""):
            return True

        return False
        
    def is_draw(self):
        for row in self.button:
            for button in row:
                if button.text() == "":
                    return False
        return True
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
