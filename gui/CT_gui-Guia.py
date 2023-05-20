# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CT_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView


class Ui_CT_gui(object):
    def setupUi(self, CT_gui):
        CT_gui.setObjectName("CT_gui")
        CT_gui.resize(581, 521)
        self.centralwidget = QtWidgets.QWidget(CT_gui)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 581, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.CharDataTable = QtWidgets.QTableWidget(self.tab)
        self.CharDataTable.setGeometry(QtCore.QRect(260, 20, 300, 400))
        self.CharDataTable.setAlternatingRowColors(True)
        self.CharDataTable.setObjectName("CharDataTable")
        self.CharDataTable.setColumnCount(5)
        self.CharDataTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.CharDataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CharDataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CharDataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CharDataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.CharDataTable.setHorizontalHeaderItem(4, item)
        self.CharDataTable.horizontalHeader().setCascadingSectionResizes(True)
        self.CharDataTable.horizontalHeader().setDefaultSectionSize(10)
        self.CharDataTable.horizontalHeader().setMaximumSectionSize(91)
        self.CharDataTable.horizontalHeader().setMinimumSectionSize(49)
        self.CharDataTable.verticalHeader().setDefaultSectionSize(20)
        self.CharDataTable.verticalHeader().setMinimumSectionSize(20)
        self.CharEdit = QtWidgets.QLineEdit(self.tab)
        self.CharEdit.setGeometry(QtCore.QRect(100, 30, 121, 20))
        self.CharEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CharEdit.setObjectName("CharEdit")
        self.HPEdit = QtWidgets.QLineEdit(self.tab)
        self.HPEdit.setGeometry(QtCore.QRect(100, 50, 121, 20))
        self.HPEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.HPEdit.setObjectName("HPEdit")
        self.ACEdit = QtWidgets.QLineEdit(self.tab)
        self.ACEdit.setGeometry(QtCore.QRect(100, 70, 121, 20))
        self.ACEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ACEdit.setObjectName("ACEdit")
        self.InitiativeEdit = QtWidgets.QLineEdit(self.tab)
        self.InitiativeEdit.setGeometry(QtCore.QRect(100, 90, 121, 20))
        self.InitiativeEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.InitiativeEdit.setObjectName("InitiativeEdit")
        self.AddCharButton = QtWidgets.QPushButton(self.tab)
        self.AddCharButton.setGeometry(QtCore.QRect(20, 140, 201, 23))
        self.AddCharButton.setObjectName("AddCharButton")
        self.UndoCharButton = QtWidgets.QPushButton(self.tab)
        self.UndoCharButton.setGeometry(QtCore.QRect(20, 170, 201, 23))
        self.UndoCharButton.setObjectName("UndoCharButton")
        self.StartCombButton = QtWidgets.QPushButton(self.tab)
        self.StartCombButton.setGeometry(QtCore.QRect(20, 200, 171, 23))
        self.StartCombButton.setObjectName("StartCombButton")
        self.CombatCheckBox = QtWidgets.QCheckBox(self.tab)
        self.CombatCheckBox.setGeometry(QtCore.QRect(200, 200, 41, 21))
        self.CombatCheckBox.setText("")
        self.CombatCheckBox.setCheckable(False)
        self.CombatCheckBox.setObjectName("CombatCheckBox")
        self.Char = QtWidgets.QLabel(self.tab)
        self.Char.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.Char.setObjectName("Char")
        self.HP = QtWidgets.QLabel(self.tab)
        self.HP.setGeometry(QtCore.QRect(20, 50, 81, 20))
        self.HP.setObjectName("HP")
        self.AC = QtWidgets.QLabel(self.tab)
        self.AC.setGeometry(QtCore.QRect(20, 70, 81, 20))
        self.AC.setObjectName("AC")
        self.Initiative = QtWidgets.QLabel(self.tab)
        self.Initiative.setGeometry(QtCore.QRect(20, 90, 81, 20))
        self.Initiative.setObjectName("Initiative")
        self.Cond = QtWidgets.QLabel(self.tab)
        self.Cond.setGeometry(QtCore.QRect(20, 110, 81, 20))
        self.Cond.setObjectName("Cond")
        self.CondComboBox = QtWidgets.QComboBox(self.tab)
        self.CondComboBox.setEnabled(True)
        self.CondComboBox.setGeometry(QtCore.QRect(100, 110, 121, 20))
        self.CondComboBox.setEditable(False)
        self.CondComboBox.setCurrentText("")
        self.CondComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.CondComboBox.setObjectName("CondComboBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.CharOrderTable = QtWidgets.QTableWidget(self.tab_2)
        self.CharOrderTable.setGeometry(QtCore.QRect(10, 20, 300, 400))
        self.CharOrderTable.setAlternatingRowColors(True)
        self.CharOrderTable.setObjectName("CharOrderTable")
        self.CharOrderTable.setColumnCount(5)
        self.CharOrderTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.CharOrderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CharOrderTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CharOrderTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CharOrderTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.CharOrderTable.setHorizontalHeaderItem(4, item)
        self.CharOrderTable.horizontalHeader().setCascadingSectionResizes(True)
        self.CharOrderTable.horizontalHeader().setDefaultSectionSize(10)
        self.CharOrderTable.horizontalHeader().setMaximumSectionSize(91)
        self.CharOrderTable.horizontalHeader().setMinimumSectionSize(49)
        self.CharOrderTable.verticalHeader().setDefaultSectionSize(20)
        self.CharOrderTable.verticalHeader().setMinimumSectionSize(20)
        self.DmgDealtEdit = QtWidgets.QLineEdit(self.tab_2)
        self.DmgDealtEdit.setGeometry(QtCore.QRect(440, 60, 121, 20))
        self.DmgDealtEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DmgDealtEdit.setObjectName("DmgDealtEdit")
        self.Damage = QtWidgets.QLabel(self.tab_2)
        self.Damage.setGeometry(QtCore.QRect(320, 30, 211, 20))
        self.Damage.setAlignment(QtCore.Qt.AlignCenter)
        self.Damage.setObjectName("Damage")
        self.DmgDealt = QtWidgets.QLabel(self.tab_2)
        self.DmgDealt.setGeometry(QtCore.QRect(320, 60, 121, 20))
        self.DmgDealt.setObjectName("DmgDealt")
        self.DmgTargetComboBox = QtWidgets.QComboBox(self.tab_2)
        self.DmgTargetComboBox.setGeometry(QtCore.QRect(440, 80, 121, 22))
        self.DmgTargetComboBox.setObjectName("DmgTargetComboBox")
        self.DmgTarget = QtWidgets.QLabel(self.tab_2)
        self.DmgTarget.setGeometry(QtCore.QRect(320, 80, 121, 20))
        self.DmgTarget.setObjectName("DmgTarget")
        self.CondDealt = QtWidgets.QLabel(self.tab_2)
        self.CondDealt.setGeometry(QtCore.QRect(320, 160, 121, 20))
        self.CondDealt.setObjectName("CondDealt")
        self.CondTarget = QtWidgets.QLabel(self.tab_2)
        self.CondTarget.setGeometry(QtCore.QRect(320, 180, 121, 20))
        self.CondTarget.setObjectName("CondTarget")
        self.Condition = QtWidgets.QLabel(self.tab_2)
        self.Condition.setGeometry(QtCore.QRect(320, 130, 211, 20))
        self.Condition.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Condition.setAlignment(QtCore.Qt.AlignCenter)
        self.Condition.setObjectName("Condition")
        self.CondTargetComboBox = QtWidgets.QComboBox(self.tab_2)
        self.CondTargetComboBox.setGeometry(QtCore.QRect(440, 180, 121, 22))
        self.CondTargetComboBox.setObjectName("CondTargetComboBox")
        self.DmgHealed = QtWidgets.QLabel(self.tab_2)
        self.DmgHealed.setGeometry(QtCore.QRect(320, 260, 121, 20))
        self.DmgHealed.setObjectName("DmgHealed")
        self.DmgHealedEdit = QtWidgets.QLineEdit(self.tab_2)
        self.DmgHealedEdit.setGeometry(QtCore.QRect(440, 260, 121, 20))
        self.DmgHealedEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DmgHealedEdit.setObjectName("DmgHealedEdit")
        self.HealTarget = QtWidgets.QLabel(self.tab_2)
        self.HealTarget.setGeometry(QtCore.QRect(320, 280, 121, 20))
        self.HealTarget.setObjectName("HealTarget")
        self.Heal = QtWidgets.QLabel(self.tab_2)
        self.Heal.setGeometry(QtCore.QRect(320, 230, 211, 20))
        self.Heal.setAlignment(QtCore.Qt.AlignCenter)
        self.Heal.setObjectName("Heal")
        self.DmgHealedComboBox = QtWidgets.QComboBox(self.tab_2)
        self.DmgHealedComboBox.setGeometry(QtCore.QRect(440, 280, 121, 22))
        self.DmgHealedComboBox.setObjectName("DmgHealedComboBox")
        self.Round = QtWidgets.QLabel(self.tab_2)
        self.Round.setGeometry(QtCore.QRect(480, 390, 61, 20))
        self.Round.setObjectName("Round")
        self.NextTurnButton = QtWidgets.QPushButton(self.tab_2)
        self.NextTurnButton.setGeometry(QtCore.QRect(320, 360, 241, 23))
        self.NextTurnButton.setObjectName("NextTurnButton")
        self.DealActionButton = QtWidgets.QPushButton(self.tab_2)
        self.DealActionButton.setGeometry(QtCore.QRect(320, 330, 241, 23))
        self.DealActionButton.setObjectName("DealActionButton")
        self.CondDealtComboBox = QtWidgets.QComboBox(self.tab_2)
        self.CondDealtComboBox.setGeometry(QtCore.QRect(440, 160, 121, 22))
        self.CondDealtComboBox.setObjectName("CondDealtComboBox")
        self.RoundNumber = QtWidgets.QLabel(self.tab_2)
        self.RoundNumber.setGeometry(QtCore.QRect(540, 390, 21, 20))
        self.RoundNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RoundNumber.setObjectName("RoundNumber")
        self.tabWidget.addTab(self.tab_2, "")
        CT_gui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CT_gui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 22))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        CT_gui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CT_gui)
        self.statusbar.setObjectName("statusbar")
        CT_gui.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(CT_gui)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(CT_gui)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(CT_gui)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen = QtWidgets.QAction(CT_gui)
        self.actionOpen.setObjectName("actionOpen")
        self.menuHome.addAction(self.actionNew)
        self.menuHome.addAction(self.actionSave)
        self.menuHome.addAction(self.actionSave_as)
        self.menuHome.addAction(self.actionOpen)
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(CT_gui)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CT_gui)

    def retranslateUi(self, CT_gui):
        _translate = QtCore.QCoreApplication.translate
        CT_gui.setWindowIcon(QtGui.QIcon('D:\RPG\DnD\CombatTracker\Python\gui\CT_icon.ico'))
        CT_gui.setWindowTitle(_translate("CT_gui", "CombAlva Tracked"))
        item = self.CharDataTable.horizontalHeaderItem(0)
        item.setText(_translate("CT_gui", "Character"))
        item = self.CharDataTable.horizontalHeaderItem(1)
        item.setText(_translate("CT_gui", "HP"))
        item = self.CharDataTable.horizontalHeaderItem(2)
        item.setText(_translate("CT_gui", "AC"))
        item = self.CharDataTable.horizontalHeaderItem(3)
        item.setText(_translate("CT_gui", "Init."))
        item = self.CharDataTable.horizontalHeaderItem(4)
        item.setText(_translate("CT_gui", "Condition"))
        header = self.CharDataTable.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.AddCharButton.setText(_translate("CT_gui", "Add Character"))
        self.UndoCharButton.setText(_translate("CT_gui", "Undo Character"))
        self.StartCombButton.setText(_translate("CT_gui", "Start Combat"))
        self.Char.setText(_translate("CT_gui", "Character"))
        self.HP.setText(_translate("CT_gui", "HP"))
        self.AC.setText(_translate("CT_gui", "AC"))
        self.Initiative.setText(_translate("CT_gui", "Initiative"))
        self.Cond.setText(_translate("CT_gui", "Condition"))
        self.CondComboBox.insertItems(0, ["Normal", "Prone", "Hiden", "Grappled", "Charmed", "Frightened", "Poisoned", "Blind", "Incapacited", "Paralised", "Petrified", "Restrained", "Stunned", "Unconscious", "Invisible", "Deafened"])
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CT_gui", "Character Info"))
        item = self.CharOrderTable.horizontalHeaderItem(0)
        item.setText(_translate("CT_gui", "Character"))
        item = self.CharOrderTable.horizontalHeaderItem(1)
        item.setText(_translate("CT_gui", "HP"))
        item = self.CharOrderTable.horizontalHeaderItem(2)
        item.setText(_translate("CT_gui", "AC"))
        item = self.CharOrderTable.horizontalHeaderItem(3)
        item.setText(_translate("CT_gui", "Init."))
        item = self.CharOrderTable.horizontalHeaderItem(4)
        item.setText(_translate("CT_gui", "Condition"))
        header = self.CharOrderTable.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.Damage.setText(_translate("CT_gui", "Damage"))
        self.DmgDealt.setText(_translate("CT_gui", "Damage dealt"))
        self.DmgTarget.setText(_translate("CT_gui", "Damage target"))
        self.CondDealt.setText(_translate("CT_gui", "Condition dealt"))
        self.CondTarget.setText(_translate("CT_gui", "Condition target"))
        self.Condition.setText(_translate("CT_gui", "Condition"))
        self.DmgHealed.setText(_translate("CT_gui", "Damage healed"))
        self.HealTarget.setText(_translate("CT_gui", "Healing target"))
        self.Heal.setText(_translate("CT_gui", "Heal"))
        self.Round.setText(_translate("CT_gui", "Round"))
        self.NextTurnButton.setText(_translate("CT_gui", "Next Turn"))
        self.DealActionButton.setText(_translate("CT_gui", "Deal Action"))
        self.RoundNumber.setText(_translate("CT_gui", "0"))
        self.CondDealtComboBox.insertItems(0, ["Normal", "Prone", "Hiden", "Grappled", "Charmed", "Frightened", "Poisoned", "Blind", "Incapacited", "Paralised", "Petrified", "Restrained", "Stunned", "Unconscious", "Invisible", "Deafened", "Dead", "Stable", "Revived"])
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CT_gui", "Rounds"))
        self.menuHome.setTitle(_translate("CT_gui", "Home"))
        self.actionNew.setText(_translate("CT_gui", "New"))
        self.actionNew.setShortcut(_translate("CT_gui", "Ctrl+N"))
        self.actionSave.setText(_translate("CT_gui", "Save"))
        self.actionSave.setShortcut(_translate("CT_gui", "Ctrl+S"))
        self.actionSave_as.setText(_translate("CT_gui", "Save as..."))
        self.actionSave_as.setShortcut(_translate("CT_gui", "Ctrl+Shift+S"))
        self.actionOpen.setText(_translate("CT_gui", "Open"))
        self.actionOpen.setShortcut(_translate("CT_gui", "Ctrl+O"))
