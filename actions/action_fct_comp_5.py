
import sqlite3
from utils import display
from gui.fct_comp_5 import  Ui_fct_comp_5
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTableWidget

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


# Classe permettant d'afficher la fonction à compléter 1
class AppFctComp6(QDialog):

    ui = Ui_fct_comp_5()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        # display.refreshLabel(self.ui.label_fct_comp_representation, "")
        try:
            cursor1 = self.data.cursor()
            result1 = cursor1.execute(
                "SELECT noSpec,dateRep FROM LesRepresentations_base"
            )
            for row in result1:

                cursor2 = self.data.cursor()
                result2 = cursor2.execute(
                    "SELECT noSpec, dateRep FROM LesTickets  WHERE noSpec = ? AND dateRep = ?",
                   [row[0], row[1]])
                for row1 in result2:
                    cursor3 = self.data.cursor()
                    result3 = cursor3.execute(
                        "SELECT noSpec,dateRep, count(*) FROM LesTickets where noSpec = ? AND  dateRep = ?",
                        [row1[0], row1[1]])
                display.refreshGenericData1(self.ui.tableresultat, result3)

        except Exception as e:
            self.ui.tableresultat.setRowCount(0)
            display.refreshLabel(self.ui.label_res, "Impossible d'afficher les résultats : " + repr(e))

