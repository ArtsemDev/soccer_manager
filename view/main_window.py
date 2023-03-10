from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QPushButton, QVBoxLayout, QLineEdit, QWidget, QMainWindow, QInputDialog)

from model import City, Footballer, Team, Position
from view.search_window import SearchForm


class UiForm(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 480)
        self.vertical_layout = QVBoxLayout(Form)
        self.vertical_layout.setSpacing(5)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.vertical_layout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setAccessibleDescription(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.vertical_layout_2 = QVBoxLayout(self.frame)
        self.vertical_layout_2.setObjectName(u"vertical_layout_2")
        self.search_filter = ''
        self.delete_filter = ''

        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setText('SEARCH')
        self.searchButton.clicked.connect(self.open_search_window)
        self.vertical_layout_2.addWidget(self.searchButton)

        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setText('DELETE')
        self.deleteButton.clicked.connect(self.open_delete_window)
        self.vertical_layout_2.addWidget(self.deleteButton)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 28))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_4.setText('??????')

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_7.setText('???????? ????????????????')

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.horizontalLayout.addWidget(self.label)
        self.label.setText('??????????????')

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_2.setText('??????????')

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_5.setText('????????????')

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_6.setText('??????????????')

        self.vertical_layout_2.addWidget(self.frame_2, 0, Qt.AlignTop)
        self.vertical_layout.addWidget(self.frame)

        QMetaObject.connectSlotsByName(Form)
        self.frames = []
        self.load_from_db()

    def load_from_db(self):
        for frame in self.frames:
            frame.deleteLater()
        self.frames.clear()
        footballers = Footballer.select()

        for footballer in footballers:
            info = footballer.info.lower().split()
            for i in self.search_filter.lower().split():
                if i not in info:
                    break
            else:
                frame = QFrame(self.frame)
                frame.setObjectName(u"frame_3")
                frame.setFrameShape(QFrame.StyledPanel)
                frame.setFrameShadow(QFrame.Raised)
                horizontal_layout = QHBoxLayout(frame)
                horizontal_layout.setObjectName(u"horizontalLayout_2")

                label = QLabel(frame)
                label.setObjectName(f"label_name_{footballer.pk}")
                horizontal_layout.addWidget(label)
                label.setText(footballer.full_name)

                label = QLabel(frame)
                label.setObjectName(f"label_dob_{footballer.pk}")
                horizontal_layout.addWidget(label)
                label.setText(footballer.birthdate)

                team = Team.get(footballer.team_id)
                label = QLabel(frame)
                label.setObjectName(f"label_team_{footballer.pk}")
                horizontal_layout.addWidget(label)
                label.setText(team.name)

                city = City.get(footballer.city_id)
                label = QLabel(frame)
                label.setObjectName(f"label_city_{footballer.pk}")
                horizontal_layout.addWidget(label)
                label.setText(city.name)

                # city = City.get(footballer.city_id)
                label = QLabel(frame)
                label.setObjectName(f"label__{footballer.pk}")
                horizontal_layout.addWidget(label)
                label.setText('????????????')

                position = Position.get(footballer.position_id)
                label = QLabel(frame)
                label.setObjectName(f"label_position_{footballer.pk}")
                horizontal_layout.addWidget(label)
                label.setText(position.name)
                self.frames.append(frame)
                self.vertical_layout_2.addWidget(frame, 0, Qt.AlignTop)
        self.search_filter = ''

    def open_search_window(self):
        text, ok = QInputDialog.getText(
            self,
            'Input',
            'Input',
        )
        if ok:
            self.search_filter = text
            self.load_from_db()

    def _delete(self):
        footballers = Footballer.select()

        deleted_count = 0

        for footballer in footballers:
            info = footballer.info.lower().split()
            for i in self.delete_filter.lower().split():
                if i not in info:
                    break
            else:
                footballer.delete()
                deleted_count += 1
        self.delete_filter = ''
        print(deleted_count)

    def open_delete_window(self):
        text, ok = QInputDialog.getText(
            self,
            'DELETE',
            'FILTER DELETE'
        )
        if ok:
            self.delete_filter = text
            self._delete()
            self.load_from_db()
