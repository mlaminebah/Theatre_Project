# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_comp_4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_comp_4(object):
    def setupUi(self, fct_comp_4):
        fct_comp_4.setObjectName("fct_comp_4")
        fct_comp_4.resize(911, 325)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_comp_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(fct_comp_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(fct_comp_4)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_4_num = QtWidgets.QComboBox(fct_comp_4)
        self.comboBox_4_num.setObjectName("comboBox_4_num")
        self.horizontalLayout.addWidget(self.comboBox_4_num)
        self.label_2 = QtWidgets.QLabel(fct_comp_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_4_categorie = QtWidgets.QComboBox(fct_comp_4)
        self.comboBox_4_categorie.setObjectName("comboBox_4_categorie")
        self.horizontalLayout.addWidget(self.comboBox_4_categorie)
        self.pushButton_fct_4 = QtWidgets.QPushButton(fct_comp_4)
        self.pushButton_fct_4.setObjectName("pushButton_fct_4")
        self.horizontalLayout.addWidget(self.pushButton_fct_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table_fct_comp_4 = QtWidgets.QTableWidget(fct_comp_4)
        self.table_fct_comp_4.setObjectName("table_fct_comp_4")
        self.table_fct_comp_4.setColumnCount(6)
        self.table_fct_comp_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_4.setHorizontalHeaderItem(5, item)
        self.table_fct_comp_4.horizontalHeader().setDefaultSectionSize(70)
        self.table_fct_comp_4.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_comp_4.horizontalHeader().setStretchLastSection(True)
        self.table_fct_comp_4.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_comp_4)
        self.label_fct_comp_4 = QtWidgets.QLabel(fct_comp_4)
        self.label_fct_comp_4.setText("")
        self.label_fct_comp_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_comp_4.setObjectName("label_fct_comp_4")
        self.verticalLayout.addWidget(self.label_fct_comp_4)

        self.retranslateUi(fct_comp_4)
        self.pushButton_fct_4.clicked.connect(fct_comp_4.refreshResult)
        self.comboBox_4_num.currentTextChanged['QString'].connect(fct_comp_4.refreshCatList)
        QtCore.QMetaObject.connectSlotsByName(fct_comp_4)

    def retranslateUi(self, fct_comp_4):
        _translate = QtCore.QCoreApplication.translate
        fct_comp_4.setWindowTitle(_translate("fct_comp_4", "Tickets d\'un dossier et d\'une catégorie"))
        self.label_3.setText(_translate("fct_comp_4", "Travail à réaliser : améliorez l\'interface de sorte que le numéro de dossier ne puisse être choisi que parmi ceux présents dans la base. La catégorie ne doit proposer que des valeurs possibles pour le numéro de dossier actuellement choisi."))
        self.label.setText(_translate("fct_comp_4", "Num dossier"))
        self.label_2.setText(_translate("fct_comp_4", "Catégorie"))
        self.pushButton_fct_4.setText(_translate("fct_comp_4", "Valider"))
        item = self.table_fct_comp_4.horizontalHeaderItem(0)
        item.setText(_translate("fct_comp_4", "noSpec"))
        item = self.table_fct_comp_4.horizontalHeaderItem(1)
        item.setText(_translate("fct_comp_4", "dateRep"))
        item = self.table_fct_comp_4.horizontalHeaderItem(2)
        item.setText(_translate("fct_comp_4", "noPlace"))
        item = self.table_fct_comp_4.horizontalHeaderItem(3)
        item.setText(_translate("fct_comp_4", "noRang"))
        item = self.table_fct_comp_4.horizontalHeaderItem(4)
        item.setText(_translate("fct_comp_4", "dateEmTick"))
        item = self.table_fct_comp_4.horizontalHeaderItem(5)
        item.setText(_translate("fct_comp_4", "noDos"))

