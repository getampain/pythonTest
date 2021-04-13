import sys
from PyQt5.QtWidgets import *
#어떤 용도인거지???
#from PyQt5.QtCore import *


"""
    move 함수는 해당 위젯의 0,0 좌표로 부터 이동거리를 지정하는함수
    resize는 크기를 지정하는 파트

    setGeometry(300,300,300,300) 처럼 아에 처음부터 지정하는 방법도있다.


    connect 함수를 사용해서 이벤트를 바인드 해준다
"""

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        
        # 해당 파트에서 버튼을 추가한다
        btn1 = QPushButton("click this!!", self)
        btn1.move(30, 30)
        btn1.clicked.connect(self.alertMessage)

        # 표출부
        self.show()

    def alertMessage(self):
        QMessageBox.about(self, "message this !!", "clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())