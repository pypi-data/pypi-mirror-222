# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailed_progress_report.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGroupBox,
    QLabel, QProgressBar, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_DetailedProgressReport(object):
    def setupUi(self, DetailedProgressReport):
        if not DetailedProgressReport.objectName():
            DetailedProgressReport.setObjectName(u"DetailedProgressReport")
        DetailedProgressReport.resize(628, 338)
        self.verticalLayout = QVBoxLayout(DetailedProgressReport)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblMessage = QLabel(DetailedProgressReport)
        self.lblMessage.setObjectName(u"lblMessage")

        self.verticalLayout.addWidget(self.lblMessage)

        self.progressBar = QProgressBar(DetailedProgressReport)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.groupDetails = QGroupBox(DetailedProgressReport)
        self.groupDetails.setObjectName(u"groupDetails")
        self.verticalLayout_2 = QVBoxLayout(self.groupDetails)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txtDetails = QTextBrowser(self.groupDetails)
        self.txtDetails.setObjectName(u"txtDetails")

        self.verticalLayout_2.addWidget(self.txtDetails)


        self.verticalLayout.addWidget(self.groupDetails)

        self.buttonBox = QDialogButtonBox(DetailedProgressReport)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DetailedProgressReport)

        QMetaObject.connectSlotsByName(DetailedProgressReport)
    # setupUi

    def retranslateUi(self, DetailedProgressReport):
        DetailedProgressReport.setWindowTitle(QCoreApplication.translate("DetailedProgressReport", u"Form", None))
        self.lblMessage.setText(QCoreApplication.translate("DetailedProgressReport", u"Processing", None))
        self.groupDetails.setTitle(QCoreApplication.translate("DetailedProgressReport", u"Details", None))
    # retranslateUi

