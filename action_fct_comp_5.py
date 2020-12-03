
import sqlite3
from utils import display
from gui.fct_comp_5 import  Ui_fct_comp_5
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

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

        #display.refreshLabel(self.ui.label_fct_comp_representation, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT noSpec,nomSpec,dateRep,count(*) FROM LesSpectacles natural join LesRepresentations_base natural join LesTickets GROUP BY noSpec, nomSpec,dateRep,noRang,noPlace")
        except Exception as e:
            self.ui.tableresultat.setRowCount(0)
            display.refreshLabel(self.ui.label_res, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.tableresultat, result)
