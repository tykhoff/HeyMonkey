from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtGui import *
from bs4 import BeautifulSoup


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        wv = QWebView()
        box_layout_1 = QVBoxLayout()
        box_layout_1.addWidget(wv)

        box_layout_2 = QVBoxLayout()
        textfield = QTextEdit()
        box_layout_2.addWidget(textfield)

        console = QWebView()
        box_layout_0 = QVBoxLayout()
        box_layout_0.addWidget(console)

        main_layout = QGridLayout()
        main_layout.addLayout(box_layout_0, 0, 0)
        main_layout.addLayout(box_layout_1, 1, 1)
        main_layout.addLayout(box_layout_2, 0, 1)

        def get_html():
            self.html_tmp = wv.page().mainFrame().toHtml()
            textfield.insertPlainText(self.html_tmp)
            console.setHtml(self.html_tmp)

        self.setLayout(main_layout)
        self.setWindowTitle("Hey Monkey")

        wv.load(QUrl('http://www.huxiu.com/'))
        wv.loadFinished.connect(get_html)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())
