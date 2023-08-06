import typing
from typing import Optional

import PySide6.QtCore
import PySide6.QtWidgets
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from maphis.filter_widget import FilterWidget
from maphis.image_list_delegate import ImageListView
from maphis.image_list_model import ImageListModel, ImageListSortFilterProxyModel
from maphis.project.project import Project


class PhotoListWidget(QWidget):
    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None,
                 f: PySide6.QtCore.Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent, f)
        self.layout = QVBoxLayout()

        self.filter_widget: FilterWidget = FilterWidget()
        self._lblImageCount: QLabel = QLabel()

        self._image_list_view: ImageListView = ImageListView()

        self.layout.addWidget(self.filter_widget)
        self.layout.addWidget(self._lblImageCount)
        self.layout.addWidget(self._image_list_view)

        self._image_list_model: ImageListModel = ImageListModel()
        self._image_list_proxy: ImageListSortFilterProxyModel = ImageListSortFilterProxyModel()
        self._image_list_proxy.layoutChanged.connect(self._update_lblImageCount)

        self._project: typing.Optional[Project] = None
        self.setLayout(self.layout)

    def set_project(self, project: typing.Optional[Project]):
        self._project = project
        if self._project is not None:
            self._image_list_model.initialize(self._project.storage, self._project._thumbnail_storage)
            self._image_list_proxy.setSourceModel(self._image_list_model)
            self._image_list_view.setModel(self._image_list_proxy)
        else:
            self._image_list_view.setModel(None)
            self._image_list_model.initialize(None, None)

    def _update_lblImageCount(self, a, b):
        total_count = self._image_list_model.rowCount()
        shown_count = self._image_list_proxy.rowCount()
        hidden_count = total_count - shown_count
        self._lblImageCount.setText(f'Showing {shown_count} photo{"s" if shown_count != 1 else ""}{"" if hidden_count == 0 else f" ({hidden_count} hidden)"}.')