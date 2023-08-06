# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AboutMAPHIS(object):
    def setupUi(self, AboutMAPHIS):
        if not AboutMAPHIS.objectName():
            AboutMAPHIS.setObjectName(u"AboutMAPHIS")
        AboutMAPHIS.resize(432, 292)
        self.horizontalLayout = QHBoxLayout(AboutMAPHIS)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lblMAPHIS = QLabel(AboutMAPHIS)
        self.lblMAPHIS.setObjectName(u"lblMAPHIS")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMAPHIS.sizePolicy().hasHeightForWidth())
        self.lblMAPHIS.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.lblMAPHIS, 0, Qt.AlignHCenter)

        self.lblVersion = QLabel(AboutMAPHIS)
        self.lblVersion.setObjectName(u"lblVersion")
        sizePolicy.setHeightForWidth(self.lblVersion.sizePolicy().hasHeightForWidth())
        self.lblVersion.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.lblVersion, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lblLicense = QLabel(AboutMAPHIS)
        self.lblLicense.setObjectName(u"lblLicense")
        self.lblLicense.setTextFormat(Qt.RichText)

        self.verticalLayout.addWidget(self.lblLicense, 0, Qt.AlignHCenter)

        self.lblGitlab = QLabel(AboutMAPHIS)
        self.lblGitlab.setObjectName(u"lblGitlab")
        self.lblGitlab.setTextFormat(Qt.MarkdownText)
        self.lblGitlab.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.lblGitlab, 0, Qt.AlignHCenter)

        self.lblProjectRepoURL = QLabel(AboutMAPHIS)
        self.lblProjectRepoURL.setObjectName(u"lblProjectRepoURL")
        self.lblProjectRepoURL.setTextFormat(Qt.MarkdownText)

        self.verticalLayout.addWidget(self.lblProjectRepoURL, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(AboutMAPHIS)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setTextFormat(Qt.MarkdownText)

        self.verticalLayout.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.gridAuthors = QGroupBox(AboutMAPHIS)
        self.gridAuthors.setObjectName(u"gridAuthors")
        self.gridLayout_2 = QGridLayout(self.gridAuthors)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.gridAuthors)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gridAuthors)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.MarkdownText)

        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_7 = QLabel(self.gridAuthors)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.label = QLabel(self.gridAuthors)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridAuthors)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_10 = QLabel(self.gridAuthors)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setTextFormat(Qt.MarkdownText)

        self.gridLayout_2.addWidget(self.label_10, 4, 1, 1, 1)

        self.label_2 = QLabel(self.gridAuthors)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.MarkdownText)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridAuthors)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_4 = QLabel(self.gridAuthors)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.MarkdownText)

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridAuthors)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextFormat(Qt.MarkdownText)

        self.gridLayout_2.addWidget(self.label_8, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.gridAuthors)

        self.lblCBIA = QLabel(AboutMAPHIS)
        self.lblCBIA.setObjectName(u"lblCBIA")
        self.lblCBIA.setTextFormat(Qt.MarkdownText)

        self.verticalLayout.addWidget(self.lblCBIA, 0, Qt.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(AboutMAPHIS)

        QMetaObject.connectSlotsByName(AboutMAPHIS)
    # setupUi

    def retranslateUi(self, AboutMAPHIS):
        AboutMAPHIS.setWindowTitle(QCoreApplication.translate("AboutMAPHIS", u"About MAPHIS", None))
        self.lblMAPHIS.setText(QCoreApplication.translate("AboutMAPHIS", u"MAPHIS", None))
        self.lblVersion.setText(QCoreApplication.translate("AboutMAPHIS", u"<version>", None))
        self.lblLicense.setText(QCoreApplication.translate("AboutMAPHIS", u"license", None))
        self.lblGitlab.setText(QCoreApplication.translate("AboutMAPHIS", u"Website: https://cbia.fi.muni.cz/software/maphis.html", None))
        self.lblProjectRepoURL.setText(QCoreApplication.translate("AboutMAPHIS", u"Project repository: https://gitlab.fi.muni.cz/xmraz3/maphis", None))
        self.label_11.setText(QCoreApplication.translate("AboutMAPHIS", u"FAQ: https://gitlab.fi.muni.cz/xmraz3/maphis/-/wikis/FAQ", None))
        self.gridAuthors.setTitle(QCoreApplication.translate("AboutMAPHIS", u"Authors", None))
        self.label_5.setText(QCoreApplication.translate("AboutMAPHIS", u"Mat\u011bj Pek\u00e1r", None))
        self.label_6.setText(QCoreApplication.translate("AboutMAPHIS", u"matej.pekar120@gmail.com", None))
        self.label_7.setText(QCoreApplication.translate("AboutMAPHIS", u"Stano Pek\u00e1r", None))
        self.label.setText(QCoreApplication.translate("AboutMAPHIS", u"Petr Matula", None))
        self.label_3.setText(QCoreApplication.translate("AboutMAPHIS", u"Radoslav Mr\u00e1z", None))
        self.label_10.setText(QCoreApplication.translate("AboutMAPHIS", u"172454@mail.muni.cz", None))
        self.label_2.setText(QCoreApplication.translate("AboutMAPHIS", u"pem@fi.muni.cz", None))
        self.label_9.setText(QCoreApplication.translate("AboutMAPHIS", u"Karel \u0160t\u011bpka", None))
        self.label_4.setText(QCoreApplication.translate("AboutMAPHIS", u"radoslav.mraz95@gmail.com", None))
        self.label_8.setText(QCoreApplication.translate("AboutMAPHIS", u"56765@muni.cz", None))
        self.lblCBIA.setText(QCoreApplication.translate("AboutMAPHIS", u"Developed at CBIA https://cbia.fi.muni.cz/", None))
    # retranslateUi

