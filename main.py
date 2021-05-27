# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from functools import partial
from PySide6.QtUiTools import QUiLoader


class Main:
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.game = [[None for i in range(3)] for j in range(3)]
        self.game[0][0] = self.ui.btn_00
        self.game[0][1] = self.ui.btn_01
        self.game[0][2] = self.ui.btn_02
        self.game[1][0] = self.ui.btn_10
        self.game[1][1] = self.ui.btn_11
        self.game[1][2] = self.ui.btn_12
        self.game[2][0] = self.ui.btn_20
        self.game[2][1] = self.ui.btn_21
        self.game[2][2] = self.ui.btn_22

        self.player = 1
        self.player1_wins = 0
        self.player2_wins = 0
        self.draw = 0

        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play, i, j))

    def play(self, i, j):
        if self.game[i][j].text() == "":
            if self.player == 1:
                self.game[i][j].setText("X")
                self.game[i][j].setStyleSheet("color : Blue; background-color : #7ce4e6; font: 75 12pt MS Shell Dlg 2;")
                self.player = 2
            elif self.player == 2:
                if self.ui.rb_pl1_vs_pl2.isChecked():
                    self.game[i][j].setText("O")
                    self.game[i][j].setStyleSheet(
                        "color : red; background-color : #ffb5ba; font: 75 16pt MS Shell Dlg 2;")
                    self.player = 1
                elif self.ui.rb_pl1_vs_co.isChecked():
                    message = QMessageBox()
                    message.setText("Coming soon")
                    message.exec_()
        self.check()

    def check(self):
        if all(self.game[0][i].text() == "X" for i in range(3)):
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            message = QMessageBox()
            message.setText("VeryGood,You Win")
            message.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    sys.exit(app.exec_())
