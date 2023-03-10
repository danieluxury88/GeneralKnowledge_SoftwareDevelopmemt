import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLineEdit, QPushButton
from pprint import pprint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input_box = QLineEdit()
        self.button = QPushButton("Click me!")
        self.text_area = QTextEdit()

        # Connect button clicked signal to handler
        self.button.clicked.connect(self.handle_click)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.input_box)
        layout.addWidget(self.button)
        layout.addWidget(self.text_area)

        # Set the central widget of the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def handle_click(self):
        pprint("Hello World!")
        self.text_area.insertPlainText("Hello World!\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
