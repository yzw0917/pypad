import PyQt4.QtGui
import PyQt4.QtCore
import sys

super(DigiClock, self).__init__(parent)

class DigiClock(QLCDNumber):
    def __init__(self, parent=None):

        self.dragPosition = None

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.5)

        self.setNumDigits(19)
        self.showTime()
        self.resize(500, 60)

        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.showTime)
        timer.start(1000)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.red)
        self.setPalette(p)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
        if event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def showTime(self):
        time = QTime.currentTime()
        date = QDate.currentDate()
        text = date.toString("yyyy-MM-dd") + " " + time.toString("hh:mm:ss")
        self.display(text)


app = QApplication(sys.argv)
form = DigiClock()
form.show()
app.exec_()