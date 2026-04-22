from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self): 
        super().__init__()
        self.widget = QtWidgets.QWidget()
        self.button = QtWidgets.QPushButton("Добавить")
        self.button.clicked.connect(self.add_student)
        self.button.setStyleSheet("""
            background-color : pink;
            font-family: 'Verdana'; font-size: 14pt;
        """)
        self.dropdown_list = QtWidgets.QComboBox()
        self.dropdown_list.addItems(
            ["ИС-25-3", "ИС-24-1"]
        )
        self.layout = QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.dropdown_list)
        self.text_edit = QtWidgets.QLineEdit()
        self.text_edit.setPlaceholderText("Введите текст...")
        self.layout.addWidget(self.text_edit)

        self.plain_text_edit = QtWidgets.QPlainTextEdit()
        self.plain_text_edit.setStyleSheet("""
            background-color: #8f728a;
            color: blue;
        """)
        self.layout.addWidget(self.plain_text_edit)
    
    def add_student(self):
        selected_group = self.dropdown_list.currentText()
        student_name = self.text_edit.text()
        self.plain_text_edit.setPlainText(self.plain_text_edit.toPlainText() + "\n" + student_name+'|'+ selected_group)
        print('Нажато')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = MainWindow() # создал объект
    main_window.show() # вызвал метод шоу
    app.exec_()
