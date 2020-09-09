
from PyQt5 import QtCore, QtGui, QtWidgets

senderMailAddresses = list()
senderPasswords = list()
receiverNames = list()
receiverMailAddresses = list()
senderIndex = 0
receiverIndex = 0
smtpp = ["@yandex","@gmail","@outlook;@hotmail;@msn;.edu"]# 
smtps = ["smtp.yandex.com","smtp.gmail.com","smtp.office365.com"]
#----------------------------------------------------------------------------------------------------------------------#
# Save mail addresses to File
def writeToFile(type,txt1,txt2):
    if type == 's':
        file = open("senderMailAddress.txt","a")
        file.write(txt1+";"+txt2+";\n")
        file.close()
    if type == 'r':
        file = open("receiverMailAddress.txt", "a")
        file.write(txt1 + ";" + txt2+";\n")
        file.close()
#----------------------------------------------------------------------------------------------------------------------#
# Read From File to mail adress list and password list or name list
def readFromFile():
    try:
        senderMailAddresses.clear()
        receiverMailAddresses.clear()
        file = open("senderMailAddress.txt", "r")

        temp = file.readlines()
        file.close()
        for i in temp:
            senderMailAddresses.append(i.split(";")[0])
            senderPasswords.append(i.split(";")[1])

        file = open("receiverMailAddress.txt", "r")
        temp = file.readlines()
        file.close()
        for i in temp:
            receiverMailAddresses.append(i.split(";")[0])
            receiverNames.append(i.split(";")[1])
    except Exception as a:
        print(a)
#----------------------------------------------------------------------------------------------------------------------#
class Ui_MainWindow_addmailadress(object):
    def setupUi(self, MainWindow_addmailadress):
        MainWindow_addmailadress.setObjectName("MainWindow_addmailadress")
        MainWindow_addmailadress.resize(800, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow_addmailadress)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.radioButton_sender = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_sender.setFont(font)
        self.radioButton_sender.setChecked(True)
        self.radioButton_sender.setObjectName("radioButton_sender")
        self.verticalLayout.addWidget(self.radioButton_sender)
        self.radioButton_Receiver = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_Receiver.setFont(font)
        self.radioButton_Receiver.setObjectName("radioButton_Receiver")
        self.verticalLayout.addWidget(self.radioButton_Receiver)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout.addWidget(self.lineEdit_1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow_addmailadress.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_addmailadress)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_addmailadress.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_addmailadress)
        self.statusbar.setObjectName("statusbar")
        MainWindow_addmailadress.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow_addmailadress)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_addmailadress)

        # -------------------------------------------------------------------------------------------------------------#
        self.radioButton_sender.toggled.connect(self.toggled)
        self.radioButton_Receiver.toggled.connect(self.toggled2)
        self.pushButton.clicked.connect(self.save)

    def retranslateUi(self, MainWindow_addmailadress):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_addmailadress.setWindowTitle(_translate("MainWindow_addmailadress", "Add Mail Address"))
        self.radioButton_sender.setText(_translate("MainWindow_addmailadress", "SENDER"))
        self.radioButton_Receiver.setText(_translate("MainWindow_addmailadress", "RECEIVER"))
        self.label_1.setText(_translate("MainWindow_addmailadress", "Enter the Sender Mail Address"))
        self.label_2.setText(_translate("MainWindow_addmailadress", "Enter the Password"))
        self.pushButton.setText(_translate("MainWindow_addmailadress", "SAVE"))
#----------------------------------------------------------------------------------------------------------------------#
    # Saving the mail addresses and passwords or names to file
    def save(self):
        try:
            address = self.lineEdit_1.text()

            if not '@' in address:
                self.pushButton.setText("MAIL ADDRESS IS INCORRECT")
                return
            if len(address) < 5:
                self.pushButton.setText()("MAIL ADDRESS IS INCORRECT")
                return



            if self.radioButton_sender.isChecked():

                password = self.lineEdit_2.text()
                writeToFile('s',address,password)

            else:

                name = self.lineEdit_2.text()
                writeToFile('r',address,name)
            self.pushButton.setText("SAVED SUCCESSFULLY")

        except Exception as aaa:
            pass
#----------------------------------------------------------------------------------------------------------------------#
    # When Selected the radiobuttons
    def toggled(self):
        self.label_1.setText("Enter the Sender Mail Address")
        self.label_2.setText("Enter the Password")

    def toggled2(self):
        self.label_1.setText("Enter the Receiver Mail Address")
        self.label_2.setText("Enter the Name of Receiver")
#----------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_addmailadress = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_addmailadress()
    ui.setupUi(MainWindow_addmailadress)
    MainWindow_addmailadress.show()
    sys.exit(app.exec_())