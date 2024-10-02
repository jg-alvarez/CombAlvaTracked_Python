# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CT_DiceRoll_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiceRollWind(object):
    def setupUi(self, DiceRollWind):
        DiceRollWind.setObjectName("DiceRollWind")
        DiceRollWind.setWindowModality(QtCore.Qt.NonModal)
        DiceRollWind.resize(224, 203)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DiceRollWind.sizePolicy().hasHeightForWidth())
        DiceRollWind.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/CT_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DiceRollWind.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(DiceRollWind)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.DiceTypeBox = QtWidgets.QComboBox(DiceRollWind)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiceTypeBox.sizePolicy().hasHeightForWidth())
        self.DiceTypeBox.setSizePolicy(sizePolicy)
        self.DiceTypeBox.setObjectName("DiceTypeBox")
        self.DiceTypeBox.addItem("")
        self.DiceTypeBox.addItem("")
        self.DiceTypeBox.addItem("")
        self.DiceTypeBox.addItem("")
        self.DiceTypeBox.addItem("")
        self.DiceTypeBox.addItem("")
        self.DiceTypeBox.addItem("")
        self.DiceTypeBox.addItem("")
        self.gridLayout_2.addWidget(self.DiceTypeBox, 0, 0, 1, 1)
        self.XLabel = QtWidgets.QLabel(DiceRollWind)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XLabel.sizePolicy().hasHeightForWidth())
        self.XLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.XLabel.setFont(font)
        self.XLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.XLabel.setObjectName("XLabel")
        self.gridLayout_2.addWidget(self.XLabel, 0, 1, 1, 1)
        self.NumDiceEdit = QtWidgets.QLineEdit(DiceRollWind)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumDiceEdit.sizePolicy().hasHeightForWidth())
        self.NumDiceEdit.setSizePolicy(sizePolicy)
        self.NumDiceEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NumDiceEdit.setObjectName("NumDiceEdit")
        self.gridLayout_2.addWidget(self.NumDiceEdit, 0, 2, 1, 1)
        self.PluxLabel = QtWidgets.QLabel(DiceRollWind)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PluxLabel.sizePolicy().hasHeightForWidth())
        self.PluxLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PluxLabel.setFont(font)
        self.PluxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PluxLabel.setObjectName("PluxLabel")
        self.gridLayout_2.addWidget(self.PluxLabel, 0, 3, 1, 1)
        self.ModifierEdit = QtWidgets.QLineEdit(DiceRollWind)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModifierEdit.sizePolicy().hasHeightForWidth())
        self.ModifierEdit.setSizePolicy(sizePolicy)
        self.ModifierEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ModifierEdit.setObjectName("ModifierEdit")
        self.gridLayout_2.addWidget(self.ModifierEdit, 0, 4, 1, 1)
        self.frame = QtWidgets.QFrame(DiceRollWind)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.RollLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RollLabel.sizePolicy().hasHeightForWidth())
        self.RollLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(68)
        font.setBold(True)
        font.setWeight(75)
        self.RollLabel.setFont(font)
        self.RollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RollLabel.setObjectName("RollLabel")
        self.gridLayout.addWidget(self.RollLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 5)
        self.buttonBox = QtWidgets.QDialogButtonBox(DiceRollWind)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 5)

        self.retranslateUi(DiceRollWind)
        self.buttonBox.accepted.connect(DiceRollWind.accept) # type: ignore
        self.buttonBox.rejected.connect(DiceRollWind.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DiceRollWind)

    def retranslateUi(self, DiceRollWind):
        _translate = QtCore.QCoreApplication.translate
        DiceRollWind.setWindowTitle(_translate("DiceRollWind", "Dice Roll"))
        self.DiceTypeBox.setItemText(0, _translate("DiceRollWind", "d2"))
        self.DiceTypeBox.setItemText(1, _translate("DiceRollWind", "d4"))
        self.DiceTypeBox.setItemText(2, _translate("DiceRollWind", "d6"))
        self.DiceTypeBox.setItemText(3, _translate("DiceRollWind", "d8"))
        self.DiceTypeBox.setItemText(4, _translate("DiceRollWind", "d10"))
        self.DiceTypeBox.setItemText(5, _translate("DiceRollWind", "d12"))
        self.DiceTypeBox.setItemText(6, _translate("DiceRollWind", "d20"))
        self.DiceTypeBox.setItemText(7, _translate("DiceRollWind", "d100"))
        self.XLabel.setText(_translate("DiceRollWind", "X"))
        self.NumDiceEdit.setText(_translate("DiceRollWind", "1"))
        self.PluxLabel.setText(_translate("DiceRollWind", "+"))
        self.ModifierEdit.setText(_translate("DiceRollWind", "0"))
        self.RollLabel.setText(_translate("DiceRollWind", "0"))
import Icon_rc
import dSet_rc
