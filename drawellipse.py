import sys
from PySide6.QtWidgets import QApplication
from form1 import Form1

if(__name__ == "__main__"):
    app = QApplication()
    dialog = Form1()
    dialog.show()
    sys.exit(app.exec())