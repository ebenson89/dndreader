# Form implementation generated from reading ui file 'c:\Users\Emily\Documents\GitHub\dndreader\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.all_files_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.all_files_label.setFont(font)
        self.all_files_label.setObjectName("all_files_label")
        self.gridLayout.addWidget(self.all_files_label, 5, 2, 1, 1)
        self.kind_box = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kind_box.sizePolicy().hasHeightForWidth())
        self.kind_box.setSizePolicy(sizePolicy)
        self.kind_box.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.kind_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.kind_box.setObjectName("kind_box")
        self.gridLayout.addWidget(self.kind_box, 1, 3, 1, 1)
        self.Random_Item_lable = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(28)
        self.Random_Item_lable.setFont(font)
        self.Random_Item_lable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Random_Item_lable.setObjectName("Random_Item_lable")
        self.gridLayout.addWidget(self.Random_Item_lable, 7, 2, 1, 1)
        self.files_list_output = QtWidgets.QListWidget(self.centralwidget)
        self.files_list_output.setObjectName("files_list_output")
        self.gridLayout.addWidget(self.files_list_output, 6, 2, 1, 1)
        self.random_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.random_item_button.setObjectName("random_item_button")
        self.gridLayout.addWidget(self.random_item_button, 8, 2, 1, 1)
        self.roll_dice_button = QtWidgets.QPushButton(self.centralwidget)
        self.roll_dice_button.setObjectName("roll_dice_button")
        self.gridLayout.addWidget(self.roll_dice_button, 3, 1, 1, 3)
        self.random_item_output = QtWidgets.QLabel(self.centralwidget)
        self.random_item_output.setText("")
        self.random_item_output.setObjectName("random_item_output")
        self.gridLayout.addWidget(self.random_item_output, 9, 2, 1, 1)
        self.roll_the_dice_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.roll_the_dice_label.setFont(font)
        self.roll_the_dice_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.roll_the_dice_label.setObjectName("roll_the_dice_label")
        self.gridLayout.addWidget(self.roll_the_dice_label, 0, 0, 1, 4)
        self.how_many_box = QtWidgets.QLineEdit(self.centralwidget)
        self.how_many_box.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.how_many_box.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.how_many_box.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.how_many_box.setObjectName("how_many_box")
        self.gridLayout.addWidget(self.how_many_box, 1, 1, 1, 1)
        self.dice = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dice.setFont(font)
        self.dice.setObjectName("dice")
        self.gridLayout.addWidget(self.dice, 1, 2, 1, 1)
        self.results_output = QtWidgets.QLabel(self.centralwidget)
        self.results_output.setText("")
        self.results_output.setObjectName("results_output")
        self.gridLayout.addWidget(self.results_output, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 21))
        self.menubar.setObjectName("menubar")
        self.menuDice_Rolling = QtWidgets.QMenu(self.menubar)
        self.menuDice_Rolling.setObjectName("menuDice_Rolling")
        self.menuCharacter_Creation = QtWidgets.QMenu(self.menubar)
        self.menuCharacter_Creation.setObjectName("menuCharacter_Creation")
        self.menuRandom_Select = QtWidgets.QMenu(self.menubar)
        self.menuRandom_Select.setObjectName("menuRandom_Select")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEvil_Method = QtGui.QAction(MainWindow)
        self.actionEvil_Method.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionEvil_Method.setObjectName("actionEvil_Method")
        self.actionDefault_Dice_Setup = QtGui.QAction(MainWindow)
        self.actionDefault_Dice_Setup.setObjectName("actionDefault_Dice_Setup")
        self.menuDice_Rolling.addAction(self.actionDefault_Dice_Setup)
        self.menuCharacter_Creation.addAction(self.actionEvil_Method)
        self.menubar.addAction(self.menuDice_Rolling.menuAction())
        self.menubar.addAction(self.menuCharacter_Creation.menuAction())
        self.menubar.addAction(self.menuRandom_Select.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TTRPG Reader"))
        self.all_files_label.setText(_translate("MainWindow", "Choose File"))
        self.kind_box.setText(_translate("MainWindow", "20"))
        self.Random_Item_lable.setText(_translate("MainWindow", "Random Entry"))
        self.random_item_button.setText(_translate("MainWindow", "Choose a random entry"))
        self.roll_dice_button.setText(_translate("MainWindow", "Roll The Dice!"))
        self.roll_the_dice_label.setText(_translate("MainWindow", "Roll The Dice!"))
        self.how_many_box.setText(_translate("MainWindow", "1"))
        self.dice.setText(_translate("MainWindow", "d"))
        self.menuDice_Rolling.setTitle(_translate("MainWindow", "Dice Rolling"))
        self.menuCharacter_Creation.setTitle(_translate("MainWindow", "Character Creation"))
        self.menuRandom_Select.setTitle(_translate("MainWindow", "Random Select"))
        self.actionEvil_Method.setText(_translate("MainWindow", "Evil Method"))
        self.actionDefault_Dice_Setup.setText(_translate("MainWindow", "Default Dice Setup"))
