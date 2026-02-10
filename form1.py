from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter, QPen,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QWidget)
from ui_form1 import Ui_Dialog

class Form1(QDialog):

    def __init__(self):
        super(Form1,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.repaint()

    def paintEvent(self, event):
        super().paintEvent(event)
        width = self.width()
        height = self.height()
        g = QPainter(self)
        g.setPen(QPen(QColor("Red"), 5))
        g.setBrush(QColor("Yellow"))
        g.drawEllipse(0, 0, width, height)
        g.end()