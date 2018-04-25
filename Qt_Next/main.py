from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal,pyqtSlot
import sys

class Person(QObject):
    def __init__(self):
        QObject.__init__(self)

    saidName = pyqtSignal(str, arguments=['say'])
    #здесь добавляем свои функции слоты
    @pyqtSlot(str)
    def say(self,name):
        word = "Hi" + name
        self.saidName.emit(word)

sys_argv = sys.argv
sys_argv += ['--style', 'material'] #установка дизайна
app = QGuiApplication(sys.argv)
person = Person()
engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty('personal',person)
engine.load('new.qml')
sys.exit(app.exec_())