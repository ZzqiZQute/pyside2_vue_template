# This Python file uses the following encoding: utf-8
import sys
import os
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QCoreApplication,Qt,QUrl,QDir,QObject,Signal,Slot
from PySide2.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings

from PySide2.QtWebChannel import QWebChannel


class Comm(QObject):
    logAck = Signal(str)

    def __init__(self,parent):
        QObject.__init__(self,parent)

    @Slot(str)
    def log(self,message):
       print(message)
       self.logAck.emit('Ok Vue !')




class MainWindow(QMainWindow):
    view = None
    chan = None
    comm = None
    def __init__(self,debug=False,parent=None):
        QMainWindow.__init__(self,parent)
        QWebEngineSettings.defaultSettings().setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard,True)
        QWebEngineSettings.defaultSettings().setAttribute(QWebEngineSettings.JavascriptCanPaste,True)
        self.view=QWebEngineView(self)
        self.setCentralWidget(self.view)
        self.chan=QWebChannel(self)
        self.comm = Comm(self)
        self.chan.registerObject('channelInterface',self.comm)
        self.view.page().setWebChannel(self.chan)
        self.view.setContextMenuPolicy(Qt.NoContextMenu)
        if debug:
            self.view.load('http://localhost:8080')
            self.devView=QWebEngineView()
            self.view.page().setDevToolsPage(self.devView.page())
            self.devView.show()
        else:
            url = 'file:///'+QDir.fromNativeSeparators(os.path.abspath(os.path.join(os.path.dirname(__file__),'./frontend/dist/index.html')))
            self.view.load(QUrl(url))


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    app = QApplication([])
    window = MainWindow(True)
    window.resize(1000,800)
    window.show()
    sys.exit(app.exec_())
