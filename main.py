import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QWidget

from view.main_window import UiForm

app = QApplication(sys.argv)

Form = QWidget()
ui = UiForm()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec())
