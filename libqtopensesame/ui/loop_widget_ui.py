# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/loop_widget.ui'
#
# Created: Mon Mar  5 11:58:10 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_loop_widget(object):
    def setupUi(self, loop_widget):
        loop_widget.setObjectName(_fromUtf8("loop_widget"))
        loop_widget.resize(760, 159)
        self.gridLayout = QtGui.QGridLayout(loop_widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget_options = QtGui.QWidget(loop_widget)
        self.widget_options.setObjectName(_fromUtf8("widget_options"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_options)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_item = QtGui.QLabel(self.widget_options)
        self.label_item.setObjectName(_fromUtf8("label_item"))
        self.gridLayout_2.addWidget(self.label_item, 0, 0, 1, 1)
        self.combobox_item = QtGui.QComboBox(self.widget_options)
        self.combobox_item.setObjectName(_fromUtf8("combobox_item"))
        self.gridLayout_2.addWidget(self.combobox_item, 0, 1, 1, 1)
        self.label_cycles = QtGui.QLabel(self.widget_options)
        self.label_cycles.setObjectName(_fromUtf8("label_cycles"))
        self.gridLayout_2.addWidget(self.label_cycles, 3, 0, 1, 1)
        self.combobox_order = QtGui.QComboBox(self.widget_options)
        self.combobox_order.setObjectName(_fromUtf8("combobox_order"))
        self.combobox_order.addItem(_fromUtf8(""))
        self.combobox_order.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.combobox_order, 0, 3, 1, 1)
        self.label_order = QtGui.QLabel(self.widget_options)
        self.label_order.setObjectName(_fromUtf8("label_order"))
        self.gridLayout_2.addWidget(self.label_order, 0, 2, 1, 1)
        self.spin_cycles = QtGui.QSpinBox(self.widget_options)
        self.spin_cycles.setObjectName(_fromUtf8("spin_cycles"))
        self.gridLayout_2.addWidget(self.spin_cycles, 3, 1, 1, 1)
        self.label_repeat = QtGui.QLabel(self.widget_options)
        self.label_repeat.setObjectName(_fromUtf8("label_repeat"))
        self.gridLayout_2.addWidget(self.label_repeat, 4, 0, 1, 1)
        self.spin_repeat = QtGui.QDoubleSpinBox(self.widget_options)
        self.spin_repeat.setObjectName(_fromUtf8("spin_repeat"))
        self.gridLayout_2.addWidget(self.spin_repeat, 4, 1, 1, 1)
        self.label_skip = QtGui.QLabel(self.widget_options)
        self.label_skip.setObjectName(_fromUtf8("label_skip"))
        self.gridLayout_2.addWidget(self.label_skip, 3, 2, 1, 1)
        self.spin_skip = QtGui.QSpinBox(self.widget_options)
        self.spin_skip.setMaximum(10000)
        self.spin_skip.setObjectName(_fromUtf8("spin_skip"))
        self.gridLayout_2.addWidget(self.spin_skip, 3, 3, 1, 1)
        self.checkbox_offset = QtGui.QCheckBox(self.widget_options)
        self.checkbox_offset.setObjectName(_fromUtf8("checkbox_offset"))
        self.gridLayout_2.addWidget(self.checkbox_offset, 4, 2, 1, 2)
        self.gridLayout.addWidget(self.widget_options, 0, 0, 1, 1)
        self.widget_buttons = QtGui.QWidget(loop_widget)
        self.widget_buttons.setObjectName(_fromUtf8("widget_buttons"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_buttons)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button_add_cyclevar = QtGui.QPushButton(self.widget_buttons)
        self.button_add_cyclevar.setObjectName(_fromUtf8("button_add_cyclevar"))
        self.horizontalLayout.addWidget(self.button_add_cyclevar)
        self.button_rename_cyclevar = QtGui.QPushButton(self.widget_buttons)
        self.button_rename_cyclevar.setObjectName(_fromUtf8("button_rename_cyclevar"))
        self.horizontalLayout.addWidget(self.button_rename_cyclevar)
        self.button_remove_cyclevar = QtGui.QPushButton(self.widget_buttons)
        self.button_remove_cyclevar.setObjectName(_fromUtf8("button_remove_cyclevar"))
        self.horizontalLayout.addWidget(self.button_remove_cyclevar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_wizard = QtGui.QPushButton(self.widget_buttons)
        self.button_wizard.setObjectName(_fromUtf8("button_wizard"))
        self.horizontalLayout.addWidget(self.button_wizard)
        self.gridLayout.addWidget(self.widget_buttons, 3, 0, 1, 1)
        self.frame_summary = QtGui.QFrame(loop_widget)
        self.frame_summary.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_summary.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_summary.setObjectName(_fromUtf8("frame_summary"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_summary)
        self.horizontalLayout_2.setMargin(4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_info = QtGui.QLabel(self.frame_summary)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setObjectName(_fromUtf8("label_info"))
        self.horizontalLayout_2.addWidget(self.label_info)
        self.label_summary = QtGui.QLabel(self.frame_summary)
        self.label_summary.setObjectName(_fromUtf8("label_summary"))
        self.horizontalLayout_2.addWidget(self.label_summary)
        self.gridLayout.addWidget(self.frame_summary, 1, 0, 1, 1)

        self.retranslateUi(loop_widget)
        QtCore.QMetaObject.connectSlotsByName(loop_widget)

    def retranslateUi(self, loop_widget):
        loop_widget.setWindowTitle(QtGui.QApplication.translate("loop_widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_item.setText(QtGui.QApplication.translate("loop_widget", "Item to run", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cycles.setText(QtGui.QApplication.translate("loop_widget", "Cycles", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_order.setItemText(0, QtGui.QApplication.translate("loop_widget", "random", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_order.setItemText(1, QtGui.QApplication.translate("loop_widget", "sequential", None, QtGui.QApplication.UnicodeUTF8))
        self.label_order.setText(QtGui.QApplication.translate("loop_widget", "Order", None, QtGui.QApplication.UnicodeUTF8))
        self.label_repeat.setText(QtGui.QApplication.translate("loop_widget", "Repeat", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_repeat.setPrefix(QtGui.QApplication.translate("loop_widget", "each cycle ", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_repeat.setSuffix(QtGui.QApplication.translate("loop_widget", " time(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_skip.setText(QtGui.QApplication.translate("loop_widget", "At loop start, skip the", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_skip.setSuffix(QtGui.QApplication.translate("loop_widget", " cycle(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_skip.setPrefix(QtGui.QApplication.translate("loop_widget", "first ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_offset.setText(QtGui.QApplication.translate("loop_widget", "Run skipped cycles at end of loop (offset mode)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add_cyclevar.setText(QtGui.QApplication.translate("loop_widget", "Add variable", None, QtGui.QApplication.UnicodeUTF8))
        self.button_rename_cyclevar.setText(QtGui.QApplication.translate("loop_widget", "Rename variable", None, QtGui.QApplication.UnicodeUTF8))
        self.button_remove_cyclevar.setText(QtGui.QApplication.translate("loop_widget", "Remove variable", None, QtGui.QApplication.UnicodeUTF8))
        self.button_wizard.setText(QtGui.QApplication.translate("loop_widget", "Variable wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_info.setText(QtGui.QApplication.translate("loop_widget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_summary.setText(QtGui.QApplication.translate("loop_widget", "Automatic summary", None, QtGui.QApplication.UnicodeUTF8))

