import typing
from typing import List, Tuple, Optional

from PySide6.QtCore import QPoint, QRect, QObject
from PySide6.QtGui import QImage, QPainter
from PySide6.QtWidgets import QWidget, QComboBox, QHBoxLayout, QLabel

from maphis.common.label_change import CommandEntry
from maphis.common.photo import Photo
from maphis.common.state import State
from maphis.common.tool import Tool, PaintCommand, EditContext
from maphis.common.user_param import ParamBuilder


class SetScale(Tool):

    def __init__(self, state: State, parent: QObject = None):
        super().__init__(state, parent)
        # self.units = UnitStore()

    @property
    def active(self) -> bool:
        return super().active

    @property
    def viz_active(self) -> bool:
        return super().viz_active

    def activate(self):
        super().activate()

    def deactivate(self):
        super().deactivate()

    def switch_to_photo(self, photo: Photo):
        super().switch_to_photo(photo)

    def left_press(self, painter: QPainter, pos: QPoint, context: EditContext) -> Tuple[Optional[CommandEntry], QRect]:
        return super().left_press(painter, pos, context)

    def left_release(self, painter: QPainter, pos: QPoint, context: EditContext) -> Tuple[
        Optional[CommandEntry], QRect]:
        return super().left_release(painter, pos, context)

    def right_release(self, painter: QPainter, pos: QPoint, context: EditContext) -> Tuple[
        Optional[CommandEntry], QRect]:
        return super().right_release(painter, pos, context)

    def mouse_move(self, painter: QPainter, new_pos: QPoint, old_pos: QPoint, context: EditContext) -> Tuple[
        Optional[CommandEntry], QRect]:
        return super().mouse_move(painter, new_pos, old_pos, context)

    def viz_left_press(self, pos: QPoint, canvas: QImage) -> List[PaintCommand]:
        return super().viz_left_press(pos, canvas)

    def viz_left_release(self, pos: QPoint, canvas: QImage) -> List[PaintCommand]:
        return super().viz_left_release(pos, canvas)

    def viz_right_release(self, pos: QPoint, canvas: QImage) -> List[PaintCommand]:
        return super().viz_right_release(pos, canvas)

    def viz_mouse_move(self, new_pos: QPoint, old_pos: QPoint, canvas: QImage) -> List[PaintCommand]:
        return super().viz_mouse_move(new_pos, old_pos, canvas)

    def reset_tool(self):
        super().reset_tool()

    @property
    def viz_commands(self) -> List[PaintCommand]:
        return super().viz_commands

    @property
    def setting_widget(self) -> typing.Optional[QWidget]:
        return super().setting_widget

    @property
    def auto_register(self) -> bool:
        return False

    @property
    def group(self) -> str:
        return 'scale_extraction'

    # def _setup_tool_widget(self):
    #
    #     self._layout_hbox = QHBoxLayout()
    #
    #     self._reference_length = ParamBuilder().name('Reference length').key('reference_length').int_param()\
    #         .default_value(1).min_value(0).build()
    #     self._referenceLength_spinBox = self._reference_length.get_value_spinbox()
    #
    #     self._layout_hbox.addWidget(QLabel('Reference length:'))
    #     self._layout_hbox.addWidget(self._referenceLength_spinBox)
    #
    #     # self._units_comboBox = QComboBox()
    #     # default_idx = 0
    #     # for i, prefix in enumerate(list(SIPrefix)):
    #     #     unit = Unit(BaseUnit.m, prefix=prefix, dim=1)
    #     #     self._units_comboBox.addItem(str(unit), unit)
    #     #     if prefix == SIPrefix.m:
    #     #         default_idx = i
    #     # self._units_comboBox.setCurrentIndex(default_idx)
    #     self._units_comboBox = self._reference_length.get_unit_combo_box(UnitType.Physical)
    #     self._units_comboBox.currentIndexChanged.connect(self._handle_reference_unit_changed)
    #
    #     self._layout_hbox.addWidget(self._units_comboBox)
    #
    #     self._line_length = ParamBuilder().name('Line length').key('line_length').int_param()\
    #         .default_value(0).min_value(0).build()
    #
    #     self._layout_hbox.addSpacing(2)
    #     self._layout_hbox.addWidget(QLabel('Line length:'))
    #     self._layout_hbox.addWidget(self._line_length.get_label())



