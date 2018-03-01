import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = '$$$ The Price is Right $$$'
        self.left = 1100
        self.top = 350
        self.width = 500
        self.height = 600
        self.numPlayer = 0;
        self.guesses = 0;
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(254,189,105))
        self.setPalette(p)

        self.label = QLabel('',self)
        self.label.setGeometry(10,10,400,50)

        self.actualPrice = QLabel('',self)
        self.actualPrice.setGeometry(10,10,400,50)

        p1 = QLabel('', self)
        p1.setGeometry(10,10,400,50)
        p2 = QLabel('', self)
        p2.setGeometry(10,10,400,50)
        p3 = QLabel('', self)
        p3.setGeometry(10,10,400,50)
        p4 = QLabel('', self)
        p4.setGeometry(10,10,400,50)

        self.usertexts = {"p1text":p1, "p2text":p2, "p3text":p3, "p4text":p4}

        p1UserName = QLineEdit(self)
        p1UserName.resize(0,0)
        p2UserName = QLineEdit(self)
        p2UserName.resize(0,0)
        p3UserName = QLineEdit(self)
        p3UserName.resize(0,0)
        p4UserName = QLineEdit(self)
        p4UserName.resize(0,0)
        self.users = {"p1UserName":p1UserName, "p2UserName":p2UserName,
                    "p3UserName":p3UserName, "p4UserName":p4UserName}

        self.productName = QLabel('',self)
        self.productName.setGeometry(10,10,400,50)

        self.enterGuess = QLabel('', self)
        self.enterGuess.setGeometry(10,10,400,50)

        self.buttonOne = QPushButton('Start A Game', self)
        self.buttonOne.setToolTip('startGame')
        self.buttonOne.move(150,200) 
        self.buttonOne.resize(200, 50)
        self.buttonOne.clicked.connect(self.start_game)

        self.submitButton = QPushButton('Submit', self)
        self.submitButton.setToolTip('joinGame')
        self.submitButton.move(150,410) 
        self.submitButton.resize(0,0)
        self.submitButton.clicked.connect(self.submit_button)

        self.replayButton = QPushButton('Replay?', self)
        self.replayButton.setToolTip('joinGame')
        self.replayButton.move(150,410) 
        self.replayButton.resize(0,0)
        self.replayButton.clicked.connect(self.submit_button)

        self.quitButton = QPushButton('Quit', self)
        self.quitButton.setToolTip('joinGame')
        self.quitButton.move(150,410) 
        self.quitButton.resize(0,0)
        self.quitButton.clicked.connect(self.submit_button)

        self.image = QLabel(self)
        self.pixmap = QPixmap('./fart_ring.jpg')
        self.pixmap = self.pixmap.scaled(200,200)

        self.textbox = QLineEdit(self)
        self.textbox.move(150, 200)
        self.textbox.resize(0,0) 

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 200)
        self.textbox2.resize(0,0) 

        self.show()

    @pyqtSlot()
    def start_game(self):
        self.label.setText('Enter number of players:')
        self.label.move(160,150)
        self.textbox.resize(50,25)
        self.textbox.move(220, 200)
        self.buttonOne.setText('Enter')
        self.buttonOne.move(150,250)
        self.buttonOne.clicked.connect(self.enter_num_players)

    def enter_num_players(self):
        self.numPlayers = int(self.textbox.text())
        self.label.resize(0,0)
        self.textbox.resize(0,0)
        x = 100
        x2 = 65
        for i in range(0, self.numPlayers):
            uText = "p" + (str(i + 1)) + 'text'
            uName = 'p' + (str(i + 1)) + 'UserName'
            user = self.users[uName]
            user.resize(200,25)
            usertext = self.usertexts[uText]
            usertext.setText('p' + str(i+1) + ' username:')
            x+=50
            x2+=50
            user.move(150, x)
            usertext.move(150, x2)
        self.buttonOne.move(150,300)
        self.buttonOne.clicked.connect(self.entered_usernames)

    @pyqtSlot()
    def entered_usernames(self):
        self.image.setPixmap(self.pixmap)
        self.image.resize(200,200)
        self.image.move(150,100)
        self.productName.setText('The Moon Ring')
        self.productName.move(200,300)
        self.enterGuess.setText('Enter Your Guess: ')
        self.enterGuess.move(120,350)
        self.textbox2.setText('')
        self.textbox2.resize(100,25)
        self.textbox2.move(280, 365)
        self.buttonOne.resize(200,50)
        self.buttonOne.move(150, 400)
        self.buttonOne.clicked.connect(self.guessed)

    @pyqtSlot()
    def join_game(self):
        self.startGameButton.resize(0,0)
        self.joinGameButton.clicked.connect(self.join_game_code)
        self.textbox.resize(200,25)

    @pyqtSlot()
    def enter_guess(self, usertext):
        self.image.setPixmap(self.pixmap)
        self.image.resize(200,200)
        self.image.move(150,100)
        self.productName.setText('The Moon Ring')
        self.productName.move(200,300)
        self.enterGuess.setText('Enter Your Guess: ')
        self.enterGuess.move(120,350)
        self.textbox2.setText('')
        self.textbox2.resize(100,25)
        self.textbox2.move(280, 365)
        self.buttonOne.resize(200,50)
        self.buttonOne.move(150, 400)
        self.buttonOne.clicked.connect(self.guessed)
        return

    @pyqtSlot()
    def guessed(self):
        if self.guesses < self.numPlayers:
            self.guesses+=1
            uText = "p" + str(self.guesses) + "text"
            self.usertexts[uText].setText("p" + str(self.guesses) + " guessed " + str(self.textbox2.text()))
            print(self.usertexts[uText].text())
            return

    @pyqtSlot()
    def submit_button(self):
        self.image.resize(0,0)
        self.textbox.resize(0,0)
        self.productName.resize(0,0)
        self.enterGuess.resize(0,0)
        self.submitButton.resize(0,0)

        self.actualPrice.setText('Cost: $100.00')
        self.actualPrice.move(200,100)
        self.p1Output.setText('P1 Result')
        self.p1Output.move(150,175)
        self.p2Output.setText('P2 Result')
        self.p2Output.move(150,225)
        self.p3Output.setText('P3 Result')
        self.p3Output.move(150,275)
        self.p4Output.setText('P4 Result')
        self.p4Output.move(150,325)

        self.replayButton.resize(200,50)
        self.replayButton.move(150,400)
        self.quitButton.resize(200,50)
        self.quitButton.move(150,475)
        
    @pyqtSlot()
    def replay_button(self):
        self.initUI()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())