import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

def on_button_click():
    QMessageBox.information(window, "Info", "Button clicked!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Demo App')
window.setGeometry(100, 100, 300, 200)

button = QPushButton('Click Me', window)
button.clicked.connect(on_button_click)
button.move(100, 80)

window.show()
sys.exit(app.exec_())
