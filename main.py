import sys
from datetime import date

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QWidget

from view.main_window import UiForm
# from model import Footballer
#
# footballers = [
#     Footballer(full_name='name 1', date_of_birth=date(year=2000, month=1, day=1), team_id=1, city_id=1, position_id=1),
#     Footballer(full_name='name 2', date_of_birth=date(year=2000, month=1, day=1), team_id=1, city_id=2, position_id=1),
# ]
# for footballer in footballers:
#     footballer.save()

app = QApplication(sys.argv)

Form = QWidget()
ui = UiForm()
# ui.setupUi(Form)
ui.show()
sys.exit(app.exec())
