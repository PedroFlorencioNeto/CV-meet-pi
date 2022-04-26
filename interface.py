# Projeto Conheça o Pi - Interface gráfica
# Autor: Pedro Florencio de Almeida Neto - pedroflorencio@alu.ufc.br


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1024, 768)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(0, 0, 1024, 768))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/1.png"))
            self.label.setObjectName("label")
            self.iniciarButton = QtWidgets.QPushButton(self.centralwidget)
            self.iniciarButton.setGeometry(QtCore.QRect(440, 640, 161, 61))
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.iniciarButton.setFont(font)
            self.iniciarButton.setStyleSheet("background-color: rgb(52, 101, 164);")
            self.iniciarButton.setObjectName("iniciarButton")
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

            self.iniciarButton.clicked.connect(self.teladois)

    def inicio(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/1.png"))
        self.label.setObjectName("label")
        self.iniciarButton = QtWidgets.QPushButton(self.centralwidget)
        self.iniciarButton.setGeometry(QtCore.QRect(440, 640, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.iniciarButton.setFont(font)
        self.iniciarButton.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.iniciarButton.setObjectName("iniciarButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.iniciarButton.clicked.connect(self.teladois)


    def teladois(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelFundo = QtWidgets.QLabel(self.centralwidget)
        self.labelFundo.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.labelFundo.setText("")
        self.labelFundo.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/2.png"))
        self.labelFundo.setObjectName("labelFundo")
        self.queroButton = QtWidgets.QPushButton(self.centralwidget)
        self.queroButton.setGeometry(QtCore.QRect(210, 650, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.queroButton.setFont(font)
        self.queroButton.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.queroButton.setObjectName("queroButton")
        self.sairButton = QtWidgets.QPushButton(self.centralwidget)
        self.sairButton.setGeometry(QtCore.QRect(560, 650, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sairButton.setFont(font)
        self.sairButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.sairButton.setObjectName("sairButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_2(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.queroButton.clicked.connect(self.telatres)
        self.sairButton.clicked.connect(self.inicio)

    def telatres(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.proximoButton = QtWidgets.QPushButton(self.centralwidget)
        self.proximoButton.setGeometry(QtCore.QRect(290, 710, 89, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.proximoButton.setFont(font)
        self.proximoButton.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.proximoButton.setObjectName("proximoButton")
        self.explicacaoButton = QtWidgets.QPushButton(self.centralwidget)
        self.explicacaoButton.setGeometry(QtCore.QRect(460, 710, 89, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.explicacaoButton.setFont(font)
        self.explicacaoButton.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.explicacaoButton.setObjectName("explicacaoButton")
        self.sairButton = QtWidgets.QPushButton(self.centralwidget)
        self.sairButton.setGeometry(QtCore.QRect(620, 710, 89, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sairButton.setFont(font)
        self.sairButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.sairButton.setObjectName("sairButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 0, 1024, 671))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_3(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.movie = QMovie("pi-seara-da-ciencia/images2/pi2.gif") 
        self.label.setMovie(self.movie) 
        self.startAnimation() 
        self.explicacaoButton.clicked.connect(self.explicar)
        self.sairButton.clicked.connect(self.inicio)
        self.proximoButton.clicked.connect(self.telacinco)

    def telacinco(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fundolabel2 = QtWidgets.QLabel(self.centralwidget)
        self.fundolabel2.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.fundolabel2.setText("")
        self.fundolabel2.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/5.png"))
        self.fundolabel2.setObjectName("fundolabel2")
        self.iniciarButton = QtWidgets.QPushButton(self.centralwidget)
        self.iniciarButton.setGeometry(QtCore.QRect(400, 690, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.iniciarButton.setFont(font)
        self.iniciarButton.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.iniciarButton.setObjectName("iniciarButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_4(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.iniciarButton.clicked.connect(self.telaseis)
    
    def telaseis(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelFundo3 = QtWidgets.QLabel(self.centralwidget)
        self.labelFundo3.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.labelFundo3.setText("")
        self.labelFundo3.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/6.png"))
        self.labelFundo3.setObjectName("labelFundo3")
        self.repetirButton = QtWidgets.QPushButton(self.centralwidget)
        self.repetirButton.setGeometry(QtCore.QRect(360, 720, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.repetirButton.setFont(font)
        self.repetirButton.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.repetirButton.setObjectName("repetirButton")
        self.sairButton = QtWidgets.QPushButton(self.centralwidget)
        self.sairButton.setGeometry(QtCore.QRect(550, 720, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sairButton.setFont(font)
        self.sairButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.sairButton.setObjectName("sairButton")
        self.piLabel = QtWidgets.QLabel(self.centralwidget)
        self.piLabel.setGeometry(QtCore.QRect(120, 620, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.piLabel.setFont(font)
        self.piLabel.setObjectName("piLabel")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(280, 450, 471, 71))
        self.horizontalSlider.setMaximum(9)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.poligonoLabel = QtWidgets.QLabel(self.centralwidget)
        self.poligonoLabel.setGeometry(QtCore.QRect(380, 120, 281, 271))
        self.poligonoLabel.setText("")
        self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencial/images2/six.png"))
        self.poligonoLabel.setObjectName("poligonoLabel")
        self.nomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.nomeLabel.setGeometry(QtCore.QRect(400, 430, 310, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nomeLabel.setFont(font)
        self.nomeLabel.setObjectName("nomeLabel")
        self.piLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.piLabel_2.setGeometry(QtCore.QRect(630, 620, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.piLabel_2.setFont(font)
        self.piLabel_2.setObjectName("piLabel_2")
        MainWindow.setCentralWidget(self.centralwidget)
        
        texto = '3,0000000000000'
        lados="Hexágono (6 lados)"

        self.retranslateUi_5(MainWindow,texto,lados)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.sairButton.clicked.connect(self.inicio)
        self.horizontalSlider.valueChanged.connect(self.selecao)
        self.repetirButton.clicked.connect(self.telasete)
    
    def telasete(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/7.png"))
        self.label.setObjectName("label")
        self.iniciarButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.iniciarButton_2.setGeometry(QtCore.QRect(180, 650, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.iniciarButton_2.setFont(font)
        self.iniciarButton_2.setStyleSheet("\n"
"background-color: rgb(117, 80, 123);")
        self.iniciarButton_2.setObjectName("iniciarButton_2")
        self.iniciarButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.iniciarButton_3.setGeometry(QtCore.QRect(440, 650, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.iniciarButton_3.setFont(font)
        self.iniciarButton_3.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.iniciarButton_3.setObjectName("iniciarButton_3")
        self.iniciarButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.iniciarButton_4.setGeometry(QtCore.QRect(770, 650, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.iniciarButton_4.setFont(font)
        self.iniciarButton_4.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.iniciarButton_4.setObjectName("iniciarButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.iniciarButton_2.clicked.connect(self.telacinco)
        self.iniciarButton_3.clicked.connect(self.telaoito)
        self.iniciarButton_4.clicked.connect(self.inicio)

        self.retranslateUi_6(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def telaoito(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/8.png"))
        self.label.setObjectName("label")
        self.procurarButton = QtWidgets.QPushButton(self.centralwidget)
        self.procurarButton.setGeometry(QtCore.QRect(390, 650, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.procurarButton.setFont(font)
        self.procurarButton.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.procurarButton.setObjectName("procurarButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 350, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(77)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_7(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.procurarButton.clicked.connect(self.telanove)

    def telanove(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/9.png"))
        self.label.setObjectName("label")
        self.sairButton = QtWidgets.QPushButton(self.centralwidget)
        self.sairButton.setGeometry(QtCore.QRect(200, 660, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sairButton.setFont(font)
        self.sairButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.sairButton.setObjectName("sairButton")
        self.inserirButoon = QtWidgets.QPushButton(self.centralwidget)
        self.inserirButoon.setGeometry(QtCore.QRect(410, 660, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.inserirButoon.setFont(font)
        self.inserirButoon.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.inserirButoon.setObjectName("inserirButoon")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 330, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(52, 101, 164);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_8(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.sairButton.clicked.connect(self.inicio)
        self.inserirButoon.clicked.connect(self.telaoito)

    def selecao(self):
        
        position = int(self.horizontalSlider.value())

        # 6 lados
        if position == 0:
            texto = '3,0000000000000'
            lados="Hexágono (6 lados)"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/six.png"))
    

        # 7 lados
        elif position == 1:
            texto = '3,0371861738229'
            lados="Heptágono (7 lados)"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/seven.png"))

        # 8 lados
        elif position == 2:
            texto = '3,0614674589207'
            lados="Octógono (8 lados)"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/eight.png"))

        # 9 lados
        elif position == 3:
            texto = '3,078181289931'
            lados="Eneágono (9 lados)"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/nine.png"))

        # 10 lados
        elif position == 4:
            texto = '3,0901699437495'
            lados="Decágono (10 lados)"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/ten.png"))

        # 11 lados
        elif position == 5:
            texto = '3,0990581252557'
            lados="Hendecágono (11 lados)"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/eleven.png"))

        # 12 lados
        elif position == 6:
            texto = '3,1058285412302'
            lados="Dodecágono (12 lados)"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/twelve.png"))

        # 24 lados    
        elif position == 7: 
            texto = '3,1326286132812'
            lados="Tetracoságono (24 lados)"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/twentyfour.png"))

        # 48 lados    
        elif position == 8:
            texto = '3,1393502030469'
            lados="Polígono de 48 lados"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/fortyeight.png"))

        # 96 lados    
        elif position == 9:
            texto = '3,1410319508905'
            lados="Polígono de 96 lados"
            self.retranslateUi_5(MainWindow,texto,lados)
            self.poligonoLabel.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/ninetysix.png")) 

    def explicar(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.proximoButton = QtWidgets.QPushButton(self.centralwidget)
        self.proximoButton.setGeometry(QtCore.QRect(290, 710, 89, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.proximoButton.setFont(font)
        self.proximoButton.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.proximoButton.setObjectName("proximoButton")
        self.explicacaoButton = QtWidgets.QPushButton(self.centralwidget)
        self.explicacaoButton.setGeometry(QtCore.QRect(460, 710, 89, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.explicacaoButton.setFont(font)
        self.explicacaoButton.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.explicacaoButton.setObjectName("explicacaoButton")
        self.sairButton = QtWidgets.QPushButton(self.centralwidget)
        self.sairButton.setGeometry(QtCore.QRect(620, 710, 89, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sairButton.setFont(font)
        self.sairButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.sairButton.setObjectName("sairButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 0, 1024, 671))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_3(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.movie = QMovie("images2/pi2.gif") 
        self.label.setMovie(self.movie) 
        self.startAnimation() 
        self.explicacaoButton.clicked.connect(self.explicar)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 470, 700, 240))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pi-seara-da-ciencia/images2/label.png"))
        self.label_2.setObjectName("label_2")
        self.sairButton.clicked.connect(self.inicio)
        self.proximoButton.clicked.connect(self.telacinco)

    def startAnimation(self): 
        self.movie.start() 
  
    
    def stopAnimation(self): 
        self.movie.stop() 

   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.iniciarButton.setText(_translate("MainWindow", "Iniciar"))

    def retranslateUi_2(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.queroButton.setText(_translate("MainWindow", "Quero visualizar!"))
        self.sairButton.setText(_translate("MainWindow", "Sair"))
        
    def retranslateUi_3(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.proximoButton.setText(_translate("MainWindow", "Próximo"))
        self.explicacaoButton.setText(_translate("MainWindow", "Explicação"))
        self.sairButton.setText(_translate("MainWindow", "Sair"))

    def retranslateUi_4(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.iniciarButton.setText(_translate("MainWindow", "Iniciar"))

    def retranslateUi_5(self, MainWindow,texto,lados):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.repetirButton.setText(_translate("MainWindow", "Próximo"))
        self.sairButton.setText(_translate("MainWindow", "Sair"))
        self.piLabel.setText(_translate("MainWindow", texto))
        self.nomeLabel.setText(_translate("MainWindow", lados))
        self.piLabel_2.setText(_translate("MainWindow", "3,14159265358979"))

    def retranslateUi_6(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.iniciarButton_2.setText(_translate("MainWindow", "Voltar"))
        self.iniciarButton_3.setText(_translate("MainWindow", "Iniciar"))
        self.iniciarButton_4.setText(_translate("MainWindow", "Sair")) 

    def retranslateUi_7(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.procurarButton.setText(_translate("MainWindow", "Procurar"))

    def retranslateUi_8(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sairButton.setText(_translate("MainWindow", "Sair"))
        self.inserirButoon.setText(_translate("MainWindow", "Inserir outra data"))
        self.label_2.setText(_translate("MainWindow", "Procurando"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
