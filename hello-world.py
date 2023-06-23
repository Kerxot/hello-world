from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 300)         # Set the window size
        self.setWindowTitle('hello-world')  # Set the window title

        self.title_label = QLabel('hello-world')        # Set a label with a text
        self.title_label.setFont(QFont('Arial', 12))    # Set the font and size to the label

        self.vertical_layout = QVBoxLayout()    # Create a layout
        self.vertical_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)  # Set the content to the layout aligned to center

        self.central_widget = QWidget() # Create a widget
        self.central_widget.setLayout(self.vertical_layout) # Set the layout with the content into the widget
        
        self.setCentralWidget(self.central_widget)  # Set the central widget


if __name__ == '__main__':
    app = QApplication([])  # Create a QApplication instance
    window = Window1()      # Initialize a Window1 object
    window.show()           # Display the window
    app.exec_()             # Start the application event loop
