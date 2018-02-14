import random
import sys
from PyQt5.QtCore import *
from PyQt5 import QtTest
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
detecting=0
p1=0
p2=0
ww=0
nom = []
lis = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J']
random.shuffle(lis)
print(lis)

app = QApplication(sys.argv)
window = QWidget()
window.move(90, 90)
window.setFixedSize(1100, 800)
window.styleSheet()
window.setWindowTitle('Memory Game')



window.setWindowIcon(QtGui.QIcon('logos11.png'))

l15=QtWidgets.QLabel(window)
l15.resize(1400,1500)
l15.move(-80,-170)

l15.setPixmap(QPixmap("logos1.png"))
# -----------------------------





b = QPushButton(window)
b.resize(120, 120)
b.setStyleSheet("background:")
b.move(200,100)

b2 = QPushButton(window)
b2.resize(120, 120)
b2.move(340 ,100)


b3 = QPushButton(window)
b3.resize(120, 120)
b3.move(480,100)

b4 = QPushButton(window)
b4.resize(120, 120)
b4.move(620, 100)

#===========================


b5 = QPushButton(window)
b5.resize(120, 120)
b5.move(760, 100)







#------------------------







b6 = QPushButton(window)
b6.resize(120, 120)
b6.move(200,240)

b7 = QPushButton(window)
b7.resize(120, 120)
b7.move(340, 240)

b8 = QPushButton(window)
b8.resize(120, 120)
b8.move(480, 240)

b9 = QPushButton(window)
b9.resize(120, 120)
b9.move(620, 240)

b10 = QPushButton(window)
b10.resize(120, 120)
b10.move(760, 240)


#------------------------




b11 = QPushButton(window)
b11.resize(120, 120)
b11.move(200,380)

b12 = QPushButton(window)
b12.resize(120, 120)
b12.move(340, 380)

b13 = QPushButton(window)
b13.resize(120, 120)
b13.move(480, 380)

b14 = QPushButton(window)
b14.resize(120, 120)
b14.move(620, 380)

b15 = QPushButton(window)
b15.resize(120, 120)
b15.move(760, 380)

#=====================


b16 = QPushButton(window)
b16.resize(120, 120)
b16.move(200,520)

b17 = QPushButton(window)
b17.resize(120, 120)
b17.move(340, 520)

b18 = QPushButton(window)
b18.resize(120, 120)
b18.move(480, 520)

b19 = QPushButton(window)
b19.resize(120, 120)
b19.move(620, 520)

b20 = QPushButton(window)
b20.resize(120, 120)
b20.move(760, 520)
#========================




l3 = QtWidgets.QLabel(window)
l3.move(455,60)
l3.setStyleSheet('font-size: 12pt; font-family: Bookman;color: #312e47')
l3.setText('Eng.Abdelrahman Reda')




l5 = QtWidgets.QLabel(window)
l5.move(483,80)
l5.setStyleSheet('font-size: 7pt; font-family: Bookman;color: #312e47')
l5.setText('FCI-CAIRO UNIVERSITY')










l1s = QtWidgets.QLabel(window)
l1s.setText("Player two score")
l1s.move(212,675)


l2s= QtWidgets.QLabel(window)
l2s.setText("Player one score")
l2s.move(773,675)






l2 = QtWidgets.QLabel(window)
l2.move(250,700)
l2.setText('0')





l = QtWidgets.QLabel(window)

l.move(810,700)
l.setText('0')



# -----------------------------

def press1():
    b.setText('1')
    QtTest.QTest.qWait(400)
    b.setText(lis[0])
    QtTest.QTest.qWait(400)
    b.setText('1')

    nom.append(lis[0])

    nom.append('1')

    checkking()


def press2():

    b2.setText('2')
    QtTest.QTest.qWait(400)
    b2.setText(lis[1])

    QtTest.QTest.qWait(400)
    b2.setText('2')
    nom.append(lis[1])
    nom.append('2')

    checkking()


def press3():
    b3.setText('3')
    QtTest.QTest.qWait(400)
    b3.setText(lis[2])
    QtTest.QTest.qWait(400)

    nom.append(lis[2])
    nom.append('3')
    b3.setText('3')
    checkking()


def press4():
    b4.setText('4')
    QtTest.QTest.qWait(400)
    b4.setText(lis[3])
    QtTest.QTest.qWait(400)
    nom.append(lis[3])
    nom.append('4')
    b4.setText('4')
    checkking()




def press5():
    b5.setText('5')
    QtTest.QTest.qWait(400)
    b5.setText(lis[4])
    QtTest.QTest.qWait(400)
    nom.append(lis[4])
    nom.append('5')
    b5.setText('5')
    checkking()

def press6():
    b6.setText('6')
    QtTest.QTest.qWait(400)
    b6.setText(lis[5])
    QtTest.QTest.qWait(400)
    nom.append(lis[5])
    nom.append('6')
    b6.setText('6')
    checkking()

def press7():
    b7.setText('7')
    QtTest.QTest.qWait(400)
    b7.setText(lis[6])
    QtTest.QTest.qWait(400)
    nom.append(lis[6])
    nom.append('7')
    b7.setText('7')
    checkking()

def press8():
    b8.setText('8')
    QtTest.QTest.qWait(400)
    b8.setText(lis[7])
    QtTest.QTest.qWait(400)
    nom.append(lis[6])
    nom.append('8')
    b8.setText('8')
    checkking()

def press9():
    b9.setText('9')
    QtTest.QTest.qWait(400)
    b9.setText(lis[8])
    QtTest.QTest.qWait(400)
    nom.append(lis[8])
    nom.append('9')
    b9.setText('9')
    checkking()

def press10():
    b10.setText('10')
    QtTest.QTest.qWait(400)
    b10.setText(lis[9])
    QtTest.QTest.qWait(400)
    nom.append(lis[9])
    nom.append('10')
    b10.setText('10')
    checkking()

def press11():
    b11.setText('11')
    QtTest.QTest.qWait(400)
    b11.setText(lis[10])
    QtTest.QTest.qWait(400)
    nom.append(lis[10])
    nom.append('11')
    b11.setText('11')
    checkking()
def press12():
    b12.setText('12')
    QtTest.QTest.qWait(400)
    b12.setText(lis[11])
    QtTest.QTest.qWait(400)
    nom.append(lis[11])
    nom.append('12')
    b12.setText('12')
    checkking()

def press13():
    b13.setText('13')
    QtTest.QTest.qWait(400)
    b13.setText(lis[12])
    QtTest.QTest.qWait(400)
    nom.append(lis[12])
    nom.append('13')
    b13.setText('13')
    checkking()

def press14():
    b14.setText('14')
    QtTest.QTest.qWait(400)
    b14.setText(lis[13])
    QtTest.QTest.qWait(400)
    nom.append(lis[13])
    nom.append('14')
    b14.setText('14')
    checkking()

def press15():
    b15.setText('15')
    QtTest.QTest.qWait(400)
    b15.setText(lis[14])
    QtTest.QTest.qWait(400)
    nom.append(lis[14])
    nom.append('15')
    b15.setText('15')
    checkking()

def press16():
    b16.setText('16')
    QtTest.QTest.qWait(400)
    b16.setText(lis[15])
    QtTest.QTest.qWait(400)
    nom.append(lis[15])
    nom.append('16')
    b16.setText('16')
    checkking()

def press17():
    b17.setText('17')
    QtTest.QTest.qWait(400)
    b17.setText(lis[16])
    QtTest.QTest.qWait(400)
    nom.append(lis[16])
    nom.append('17')
    b17.setText('17')
    checkking()

def press18():
    b18.setText('18')
    QtTest.QTest.qWait(400)
    b18.setText(lis[17])
    QtTest.QTest.qWait(400)
    nom.append(lis[17])
    nom.append('18')
    b18.setText('18')
    checkking()

def press19():
    b19.setText('19')
    QtTest.QTest.qWait(400)
    b19.setText(lis[18])
    QtTest.QTest.qWait(400)
    nom.append(lis[18])
    nom.append('19')
    b19.setText('19')
    checkking()

def press20():
    b20.setText('20')
    QtTest.QTest.qWait(400)
    b20.setText(lis[19])
    QtTest.QTest.qWait(400)
    nom.append(lis[19])
    nom.append('20')
    b20.setText('20')
    checkking()





l4 = QtWidgets.QLabel(window)
l4.move(387,35)
l4.setStyleSheet('font-size: 15pt; font-family: Bookman;color:#312e47')
l4.setText('HELLO 12345678901234567890!')







# ================================






b.clicked.connect(press1)
b2.clicked.connect(press2)
b3.clicked.connect(press3)
b4.clicked.connect(press4)
b5.clicked.connect(press5)
b6.clicked.connect(press6)
b7.clicked.connect(press7)
b8.clicked.connect(press8)
b9.clicked.connect(press9)
b10.clicked.connect(press10)
b11.clicked.connect(press11)
b12.clicked.connect(press12)
b13.clicked.connect(press13)
b14.clicked.connect(press14)
b15.clicked.connect(press15)
b16.clicked.connect(press16)
b17.clicked.connect(press17)
b18.clicked.connect(press18)
b19.clicked.connect(press19)
b20.clicked.connect(press20)



def checkking ():
    if len(nom) >= 4 :
        print(nom)
        if nom[0] == nom[2] and nom[1] != nom[3] :
            print('shit')
            if "1" in nom :
                b.setEnabled(False)
            if "2" in nom :
                b2.setEnabled(False)
            if "3" in nom :
                b3.setEnabled(False)
            if "4" in nom :
                b4.setEnabled(False)
            if "5" in nom :
                b5.setEnabled(False)
            if "6" in nom :
                b6.setEnabled(False)
            if "7" in nom :
                b7.setEnabled(False)
            if "8" in nom :
                b8.setEnabled(False)
            if "9" in nom:
                b9.setEnabled(False)
            if "10" in nom :
                b10.setEnabled(False)
            if "11" in nom :
                b11.setEnabled(False)
            if "12" in nom :
                b12.setEnabled(False)
            if "13" in nom:
                b13.setEnabled(False)
            if "14" in nom:
                b14.setEnabled(False)
            if "15" in nom:
                b15.setEnabled(False)
            if "16" in nom:
                b16.setEnabled(False)
            if "17" in nom:
                b17.setEnabled(False)
            if "18" in nom:
                b18.setEnabled(False)
            if "19" in nom:
                b19.setEnabled(False)
            if "20" in nom:
                b20.setEnabled(False)








            global detecting
            global p1
            global p2
            if detecting % 2 ==0 :
                p1=p1+1
                l.setText(str(p1))
                detecting=detecting+1



            else:
                p2=p2+1
                print(p2)
                l2.setText(str(p2))
                detecting = detecting + 1



            nom.remove(nom[0])
            nom.remove(nom[0])
            nom.remove(nom[0])
            nom.remove(nom[0])
            print(nom)
        else:
            print('hey')


            nom.remove(nom[0])
            nom.remove(nom[0])
            nom.remove(nom[0])
            nom.remove(nom[0])

            print(nom)
            print('**************')
            detecting = detecting + 1
    if p1 > 5 :
        QMessageBox.about(window,'player one won!','have a nice day !')
        window.close()
    if p2 > 5 :

        QMessageBox.about(window, 'player two won!', 'have a nice day !')

        window.close()
    if p1+p2==10 :
        QMessageBox.about(window, ' draw !', 'have a nice day !')
        window.close()




window.show()
app.exec_()


