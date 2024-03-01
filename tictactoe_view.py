from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic
import os

class TictactoeView(QMainWindow):
    def __init__(self):
        super(TictactoeView, self).__init__()
        uic.loadUi(os.path.join(os.path.split(__file__)[0], "tictactoe.ui"), self)

        self.dict_of_pixmaps = {f"player_{index_player}": QIcon(QPixmap(f"./player_{index_player}.png")) for index_player in range(1, 5)}

    def check_cell(self, index_line, index_column, turn):
        self.findChild(QPushButton, f'push_button_{index_line}_{index_column}').setIcon(self.dict_of_pixmaps[f"player_{turn}"])
        self.findChild(QPushButton, f'push_button_{index_line}_{index_column}').setEnabled(False)

    def game_finished(self, winner):
        for index_line in range(0, 4):
            for index_column in range(0, 4):
                self.findChild(QPushButton, f'push_button_{index_line}_{index_column}').setEnabled(False)

        if winner == 0:
            self.game_status.setText(f"Match nul")
        else:
            self.game_status.setText(f"Le gagnant est le joueur {winner}")
