# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from. resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 680)
        MainWindow.setMinimumSize(QSize(1080, 680))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"}\n"
"\n"
"#leftFrame_2, #rightFrame_2 {\n"
"	background-color: rgb(212, 224, 255);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"#leftFrame_Label, #leftFrame_Id, #leftFrame_Edits {\n"
"	border-radius: 20px;\n"
"	background-color: rgb(147, 147, 221);\n"
"}\n"
"\n"
"#leftFrame, #centerFrame, #table_upFrame, #table_bottomFrame {\n"
"	background-color: rgb(98, 98, 147);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"#groupBox {\n"
"    border: 1px solid gray;\n"
"    border-color: #FF17365D;\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"#groupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 58px;\n"
"    background-color: rgb(33, 37, 43);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#leftFrame_2, #rightFrame_2 {\n"
"	background-color: rgb"
                        "(98, 98, 147);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QFrame#frame_image {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
""
                        "\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/logo.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#frame_image {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(\":/weather/images/weather/01d@2x.png\");\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */ /* border-left do 15px LIGHT STYLE */\n"
"#topMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 12px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	co"
                        "lor: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
""
                        "\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons_new/images/icons_new/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb("
                        "40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 5px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radiu"
                        "s: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
""
                        "\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	pa"
                        "dding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
""
                        "}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizon"
                        "tal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
""
                        " }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"	background-image: url(:/icons_new/"
                        "images/icons_new/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top rig"
                        "ht;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons_new/images/icons_new/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
" "
                        "   width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {\n"
"	co"
                        "lor: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.backMainFrame = QFrame(self.styleSheet)
        self.backMainFrame.setObjectName(u"backMainFrame")
        self.backMainFrame.setStyleSheet(u"")
        self.backMainFrame.setFrameShape(QFrame.NoFrame)
        self.backMainFrame.setFrameShadow(QFrame.Raised)
        self.backMainFrame.setLineWidth(0)
        self.verticalLayout_21 = QVBoxLayout(self.backMainFrame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.backMainFrame)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setLayoutDirection(Qt.LeftToRight)
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.contentTopBg.setLineWidth(1)
        self.topLayout = QHBoxLayout(self.contentTopBg)
        self.topLayout.setSpacing(0)
        self.topLayout.setObjectName(u"topLayout")
        self.topLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.topLogo = QFrame(self.leftBox)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(50, 50))
        self.topLogo.setMaximumSize(QSize(50, 50))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.topLogo.setLineWidth(1)

        self.horizontalLayout_3.addWidget(self.topLogo)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy1)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setFrameShape(QFrame.NoFrame)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.topLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(32, 32))
        self.settingsTopBtn.setMaximumSize(QSize(32, 26))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(32, 32))
        self.minimizeAppBtn.setMaximumSize(QSize(32, 32))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons_new/images/icons_new/icons8-\u0441\u0432\u0435\u0440\u043d\u0443\u0442\u044c-\u043e\u043a\u043d\u043e-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(32, 32))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(32, 32))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons_new/images/icons_new/icons8-\u0440\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044c-\u043e\u043a\u043d\u043e-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(32, 32))
        self.closeAppBtn.setMaximumSize(QSize(32, 32))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons_new/images/icons_new/icons8-\u0437\u0430\u043a\u0440\u044b\u0442\u044c-\u043e\u043a\u043d\u043e-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.topLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.contentTopBg)

        self.bgApp = QFrame(self.backMainFrame)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy2)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")
        self.toggleButton.setIconSize(QSize(32, 32))
        self.toggleButton.setAutoRepeatDelay(300)

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons_new/images/icons_new/icons8-\u0433\u043b\u0430\u0432\u043d\u0430\u044f-32.png);")
        self.btn_home.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_export = QPushButton(self.topMenu)
        self.btn_export.setObjectName(u"btn_export")
        sizePolicy2.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy2)
        self.btn_export.setMinimumSize(QSize(0, 45))
        self.btn_export.setFont(font)
        self.btn_export.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export.setLayoutDirection(Qt.LeftToRight)
        self.btn_export.setStyleSheet(u"background-image: url(:/icons_new/images/icons_new/icons8-export-excel-32);")
        self.btn_export.setIconSize(QSize(16, 16))
        self.btn_export.setAutoRepeatDelay(300)

        self.verticalLayout_8.addWidget(self.btn_export)

        self.btn_import = QPushButton(self.topMenu)
        self.btn_import.setObjectName(u"btn_import")
        sizePolicy2.setHeightForWidth(self.btn_import.sizePolicy().hasHeightForWidth())
        self.btn_import.setSizePolicy(sizePolicy2)
        self.btn_import.setMinimumSize(QSize(0, 45))
        self.btn_import.setFont(font)
        self.btn_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import.setLayoutDirection(Qt.LeftToRight)
        self.btn_import.setStyleSheet(u"background-image: url(:/icons_new/images/icons_new/icons8-load-from-file-32);")

        self.verticalLayout_8.addWidget(self.btn_import)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy2.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy2)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons_new/images/icons_new/icons8-\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c-32);")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.frame_17 = QFrame(self.topMenu)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_17)

        self.btn_weather = QPushButton(self.topMenu)
        self.btn_weather.setObjectName(u"btn_weather")
        sizePolicy2.setHeightForWidth(self.btn_weather.sizePolicy().hasHeightForWidth())
        self.btn_weather.setSizePolicy(sizePolicy2)
        self.btn_weather.setMinimumSize(QSize(0, 45))
        self.btn_weather.setFont(font)
        self.btn_weather.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_weather.setLayoutDirection(Qt.LeftToRight)
        self.btn_weather.setStyleSheet(u"background-image: url(:/icons_new/images/icons_new/icons8-\u0447\u0430\u0441\u0442\u0438\u0447\u043d\u0430\u044f-\u043e\u0431\u043b\u0430\u0447\u043d\u043e\u0441\u0442\u044c-32);")

        self.verticalLayout_8.addWidget(self.btn_weather)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy2.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy2)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")
        self.toggleLeftBox.setIconSize(QSize(32, 32))

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 45))
        self.extraTopBg.setMaximumSize(QSize(16777215, 45))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setPointSize(10)
        self.extraLabel.setFont(font3)

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon4)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_info = QPushButton(self.extraTopMenu)
        self.btn_info.setObjectName(u"btn_info")
        sizePolicy2.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy2)
        self.btn_info.setMinimumSize(QSize(0, 45))
        self.btn_info.setFont(font)
        self.btn_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_info.setLayoutDirection(Qt.LeftToRight)
        self.btn_info.setStyleSheet(u"background-image: url(:/icons_new/images/icons_new/icons8-\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f-32.png);")

        self.verticalLayout_11.addWidget(self.btn_info)

        self.btn_db = QPushButton(self.extraTopMenu)
        self.btn_db.setObjectName(u"btn_db")
        sizePolicy2.setHeightForWidth(self.btn_db.sizePolicy().hasHeightForWidth())
        self.btn_db.setSizePolicy(sizePolicy2)
        self.btn_db.setMinimumSize(QSize(0, 45))
        self.btn_db.setFont(font)
        self.btn_db.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_db.setLayoutDirection(Qt.LeftToRight)
        self.btn_db.setStyleSheet(u"background-image: url(:/icons_new/images/icons_new/icons8-\u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c-\u0434\u0435\u0442\u0430\u043b\u0438-32.png);")

        self.verticalLayout_11.addWidget(self.btn_db)

        self.btn_author = QPushButton(self.extraTopMenu)
        self.btn_author.setObjectName(u"btn_author")
        self.btn_author.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_author.sizePolicy().hasHeightForWidth())
        self.btn_author.setSizePolicy(sizePolicy2)
        self.btn_author.setMinimumSize(QSize(0, 45))
        self.btn_author.setFont(font)
        self.btn_author.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_author.setLayoutDirection(Qt.LeftToRight)
        self.btn_author.setStyleSheet(u"background-image: url(:/icons_new/images/icons_new/icons8-\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440-32.png);")

        self.verticalLayout_11.addWidget(self.btn_author)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setMinimumSize(QSize(0, 400))
        self.extraCenter.setStyleSheet(u"")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget_2 = QStackedWidget(self.extraCenter)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"#stackedWidget_2 QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#stackedWidget_2 QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#stackedWidget_2 QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#stackedWidget_2 QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#stackedWidget_2 QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"#stackedWidget_2 QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"#stackedWidget_2 QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.verticalLayout_32 = QVBoxLayout(self.page_info)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page_info)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_8)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_info_1 = QFrame(self.frame_8)
        self.frame_info_1.setObjectName(u"frame_info_1")
        self.frame_info_1.setStyleSheet(u"#frame_info_1 {\n"
"	background-color: rgb(150, 150, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_info_1.setFrameShape(QFrame.StyledPanel)
        self.frame_info_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_info_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(7, 0, 1, 0)
        self.label_7 = QLabel(self.frame_info_1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 110))
        self.label_7.setFont(font3)

        self.verticalLayout_16.addWidget(self.label_7)


        self.verticalLayout.addWidget(self.frame_info_1)

        self.frame_info_2 = QFrame(self.frame_8)
        self.frame_info_2.setObjectName(u"frame_info_2")
        self.frame_info_2.setMinimumSize(QSize(0, 120))
        self.frame_info_2.setStyleSheet(u"#frame_info_2 {\n"
"	background-color: rgb(150, 150, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_info_2.setFrameShape(QFrame.StyledPanel)
        self.frame_info_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_info_2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(7, 0, 1, 0)
        self.label_8 = QLabel(self.frame_info_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.verticalLayout_17.addWidget(self.label_8)


        self.verticalLayout.addWidget(self.frame_info_2)

        self.frame_info_3 = QFrame(self.frame_8)
        self.frame_info_3.setObjectName(u"frame_info_3")
        self.frame_info_3.setMinimumSize(QSize(0, 90))
        self.frame_info_3.setStyleSheet(u"#frame_info_3 {\n"
"	background-color: rgb(150, 150, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_info_3.setFrameShape(QFrame.StyledPanel)
        self.frame_info_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_info_3)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(7, 0, 1, 0)
        self.label_9 = QLabel(self.frame_info_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.verticalLayout_18.addWidget(self.label_9)


        self.verticalLayout.addWidget(self.frame_info_3)

        self.frame_info_4 = QFrame(self.frame_8)
        self.frame_info_4.setObjectName(u"frame_info_4")
        self.frame_info_4.setMinimumSize(QSize(0, 50))
        self.frame_info_4.setStyleSheet(u"#frame_info_4 {\n"
"	background-color: rgb(150, 150, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_info_4.setFrameShape(QFrame.StyledPanel)
        self.frame_info_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_info_4)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(7, 0, 1, 0)
        self.label_13 = QLabel(self.frame_info_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.verticalLayout_31.addWidget(self.label_13)


        self.verticalLayout.addWidget(self.frame_info_4)


        self.verticalLayout_32.addWidget(self.frame_8)

        self.stackedWidget_2.addWidget(self.page_info)
        self.page_db = QWidget()
        self.page_db.setObjectName(u"page_db")
        self.verticalLayout_35 = QVBoxLayout(self.page_db)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page_db)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_9)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 180))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(70, 0))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_14)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_3 = QLabel(self.frame_14)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.verticalLayout_36.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_36.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_36.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.verticalLayout_36.addWidget(self.label_6)


        self.horizontalLayout_15.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_15)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 5, 0, 0)
        self.text_host = QLineEdit(self.frame_15)
        self.text_host.setObjectName(u"text_host")
        self.text_host.setMinimumSize(QSize(0, 30))
        self.text_host.setFont(font3)

        self.verticalLayout_37.addWidget(self.text_host)

        self.text_username = QLineEdit(self.frame_15)
        self.text_username.setObjectName(u"text_username")
        self.text_username.setMinimumSize(QSize(0, 30))
        self.text_username.setFont(font3)

        self.verticalLayout_37.addWidget(self.text_username)

        self.text_password = QLineEdit(self.frame_15)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setMinimumSize(QSize(0, 30))
        self.text_password.setFont(font3)

        self.verticalLayout_37.addWidget(self.text_password)

        self.text_db = QLineEdit(self.frame_15)
        self.text_db.setObjectName(u"text_db")
        self.text_db.setMinimumSize(QSize(0, 30))
        self.text_db.setFont(font3)

        self.verticalLayout_37.addWidget(self.text_db)


        self.horizontalLayout_15.addWidget(self.frame_15)


        self.verticalLayout_34.addWidget(self.frame_13)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 25))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_10)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        font4 = QFont()
        font4.setPointSize(12)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.frame_12)


        self.verticalLayout_34.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 130))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_11)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.btn_db_connector = QPushButton(self.frame_11)
        self.btn_db_connector.setObjectName(u"btn_db_connector")
        self.btn_db_connector.setMinimumSize(QSize(0, 30))
        self.btn_db_connector.setFont(font3)

        self.verticalLayout_38.addWidget(self.btn_db_connector)

        self.btn_db_loadconfig = QPushButton(self.frame_11)
        self.btn_db_loadconfig.setObjectName(u"btn_db_loadconfig")
        self.btn_db_loadconfig.setMinimumSize(QSize(0, 30))
        self.btn_db_loadconfig.setFont(font3)

        self.verticalLayout_38.addWidget(self.btn_db_loadconfig)

        self.btn_db_save = QPushButton(self.frame_11)
        self.btn_db_save.setObjectName(u"btn_db_save")
        self.btn_db_save.setMinimumSize(QSize(0, 30))
        self.btn_db_save.setFont(font3)

        self.verticalLayout_38.addWidget(self.btn_db_save)


        self.verticalLayout_34.addWidget(self.frame_11)


        self.verticalLayout_35.addWidget(self.frame_9)

        self.stackedWidget_2.addWidget(self.page_db)
        self.page_author = QWidget()
        self.page_author.setObjectName(u"page_author")
        self.verticalLayout_45 = QVBoxLayout(self.page_author)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.page_author)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_18)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_author_avatar = QFrame(self.frame_18)
        self.frame_author_avatar.setObjectName(u"frame_author_avatar")
        self.frame_author_avatar.setStyleSheet(u"")
        self.frame_author_avatar.setFrameShape(QFrame.StyledPanel)
        self.frame_author_avatar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_author_avatar)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_author_avatar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 200))
        self.label_2.setPixmap(QPixmap(u":/images/images/avatar.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.label_2)


        self.verticalLayout_46.addWidget(self.frame_author_avatar)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_20)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_author_1 = QLabel(self.frame_20)
        self.label_author_1.setObjectName(u"label_author_1")
        self.label_author_1.setFont(font3)
        self.label_author_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_48.addWidget(self.label_author_1)

        self.label_author_4 = QLabel(self.frame_20)
        self.label_author_4.setObjectName(u"label_author_4")
        self.label_author_4.setFont(font3)
        self.label_author_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_48.addWidget(self.label_author_4)

        self.label_author_2 = QLabel(self.frame_20)
        self.label_author_2.setObjectName(u"label_author_2")
        self.label_author_2.setFont(font3)
        self.label_author_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_48.addWidget(self.label_author_2)

        self.label_author_5 = QLabel(self.frame_20)
        self.label_author_5.setObjectName(u"label_author_5")
        self.label_author_5.setFont(font3)
        self.label_author_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_48.addWidget(self.label_author_5)

        self.label_author_3 = QLabel(self.frame_20)
        self.label_author_3.setObjectName(u"label_author_3")
        self.label_author_3.setFont(font3)
        self.label_author_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_48.addWidget(self.label_author_3)


        self.verticalLayout_46.addWidget(self.frame_20)


        self.verticalLayout_45.addWidget(self.frame_18)

        self.stackedWidget_2.addWidget(self.page_author)

        self.verticalLayout_10.addWidget(self.stackedWidget_2)


        self.verticalLayout_12.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_table = QWidget()
        self.page_table.setObjectName(u"page_table")
        self.horizontalLayout = QHBoxLayout(self.page_table)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, -1, -1)
        self.leftFrame = QFrame(self.page_table)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMinimumSize(QSize(210, 0))
        self.leftFrame.setMaximumSize(QSize(24, 16777215))
        self.leftFrame.setStyleSheet(u"")
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.leftFrame_Label = QFrame(self.leftFrame)
        self.leftFrame_Label.setObjectName(u"leftFrame_Label")
        self.leftFrame_Label.setMinimumSize(QSize(0, 40))
        self.leftFrame_Label.setMaximumSize(QSize(16777215, 40))
        self.leftFrame_Label.setStyleSheet(u"")
        self.leftFrame_Label.setFrameShape(QFrame.StyledPanel)
        self.leftFrame_Label.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.leftFrame_Label)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(5, 5, 5, 9)
        self.label_Title = QLabel(self.leftFrame_Label)
        self.label_Title.setObjectName(u"label_Title")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_Title.setFont(font5)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_Title)


        self.verticalLayout_23.addWidget(self.leftFrame_Label)

        self.leftFrame_Id = QFrame(self.leftFrame)
        self.leftFrame_Id.setObjectName(u"leftFrame_Id")
        self.leftFrame_Id.setMinimumSize(QSize(0, 100))
        self.leftFrame_Id.setMaximumSize(QSize(16777215, 100))
        self.leftFrame_Id.setStyleSheet(u"")
        self.leftFrame_Id.setFrameShape(QFrame.StyledPanel)
        self.leftFrame_Id.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.leftFrame_Id)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(5, 0, 5, 0)
        self.frame_2 = QFrame(self.leftFrame_Id)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_id = QLabel(self.frame_2)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setMinimumSize(QSize(30, 0))
        self.label_id.setMaximumSize(QSize(30, 16777215))
        self.label_id.setFont(font4)

        self.horizontalLayout_10.addWidget(self.label_id)

        self.text_id = QLineEdit(self.frame_2)
        self.text_id.setObjectName(u"text_id")
        self.text_id.setMinimumSize(QSize(70, 30))
        self.text_id.setMaximumSize(QSize(70, 16777215))
        self.text_id.setFont(font3)

        self.horizontalLayout_10.addWidget(self.text_id)


        self.verticalLayout_29.addWidget(self.frame_2)

        self.frame = QFrame(self.leftFrame_Id)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_Remove = QPushButton(self.frame)
        self.btn_Remove.setObjectName(u"btn_Remove")
        self.btn_Remove.setMinimumSize(QSize(0, 30))
        self.btn_Remove.setMaximumSize(QSize(16777215, 30))
        self.btn_Remove.setFont(font3)

        self.horizontalLayout_7.addWidget(self.btn_Remove)

        self.btn_Update = QPushButton(self.frame)
        self.btn_Update.setObjectName(u"btn_Update")
        self.btn_Update.setMinimumSize(QSize(0, 30))
        self.btn_Update.setMaximumSize(QSize(16777215, 30))
        self.btn_Update.setFont(font3)

        self.horizontalLayout_7.addWidget(self.btn_Update)


        self.verticalLayout_29.addWidget(self.frame)


        self.verticalLayout_23.addWidget(self.leftFrame_Id)

        self.leftFrame_Edits = QFrame(self.leftFrame)
        self.leftFrame_Edits.setObjectName(u"leftFrame_Edits")
        self.leftFrame_Edits.setMinimumSize(QSize(0, 350))
        self.leftFrame_Edits.setMaximumSize(QSize(16777215, 400))
        self.leftFrame_Edits.setStyleSheet(u"")
        self.leftFrame_Edits.setFrameShape(QFrame.StyledPanel)
        self.leftFrame_Edits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.leftFrame_Edits)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(5, 5, 5, 0)
        self.frame_7 = QFrame(self.leftFrame_Edits)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.leftFrame_Button_Labels = QFrame(self.frame_7)
        self.leftFrame_Button_Labels.setObjectName(u"leftFrame_Button_Labels")
        self.leftFrame_Button_Labels.setMaximumSize(QSize(60, 16777215))
        self.leftFrame_Button_Labels.setFrameShape(QFrame.StyledPanel)
        self.leftFrame_Button_Labels.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.leftFrame_Button_Labels)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 5, 0, 8)
        self.label_lastname = QLabel(self.leftFrame_Button_Labels)
        self.label_lastname.setObjectName(u"label_lastname")
        self.label_lastname.setFont(font3)

        self.verticalLayout_25.addWidget(self.label_lastname)

        self.label_firstname = QLabel(self.leftFrame_Button_Labels)
        self.label_firstname.setObjectName(u"label_firstname")
        self.label_firstname.setFont(font3)

        self.verticalLayout_25.addWidget(self.label_firstname)

        self.label_middlename = QLabel(self.leftFrame_Button_Labels)
        self.label_middlename.setObjectName(u"label_middlename")
        self.label_middlename.setFont(font3)

        self.verticalLayout_25.addWidget(self.label_middlename)

        self.label_gender = QLabel(self.leftFrame_Button_Labels)
        self.label_gender.setObjectName(u"label_gender")
        self.label_gender.setFont(font3)

        self.verticalLayout_25.addWidget(self.label_gender)

        self.label_age = QLabel(self.leftFrame_Button_Labels)
        self.label_age.setObjectName(u"label_age")
        self.label_age.setFont(font3)

        self.verticalLayout_25.addWidget(self.label_age)

        self.label_phone = QLabel(self.leftFrame_Button_Labels)
        self.label_phone.setObjectName(u"label_phone")
        self.label_phone.setFont(font3)

        self.verticalLayout_25.addWidget(self.label_phone)

        self.label_city = QLabel(self.leftFrame_Button_Labels)
        self.label_city.setObjectName(u"label_city")
        self.label_city.setFont(font3)

        self.verticalLayout_25.addWidget(self.label_city)


        self.horizontalLayout_14.addWidget(self.leftFrame_Button_Labels)

        self.leftFrame_Button_Main = QFrame(self.frame_7)
        self.leftFrame_Button_Main.setObjectName(u"leftFrame_Button_Main")
        self.leftFrame_Button_Main.setFrameShape(QFrame.StyledPanel)
        self.leftFrame_Button_Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.leftFrame_Button_Main)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.text_lastname = QLineEdit(self.leftFrame_Button_Main)
        self.text_lastname.setObjectName(u"text_lastname")
        self.text_lastname.setMinimumSize(QSize(0, 30))
        self.text_lastname.setFont(font3)

        self.verticalLayout_26.addWidget(self.text_lastname)

        self.text_firstname = QLineEdit(self.leftFrame_Button_Main)
        self.text_firstname.setObjectName(u"text_firstname")
        self.text_firstname.setMinimumSize(QSize(0, 30))
        self.text_firstname.setFont(font3)

        self.verticalLayout_26.addWidget(self.text_firstname)

        self.text_middlename = QLineEdit(self.leftFrame_Button_Main)
        self.text_middlename.setObjectName(u"text_middlename")
        self.text_middlename.setMinimumSize(QSize(0, 30))
        self.text_middlename.setFont(font3)

        self.verticalLayout_26.addWidget(self.text_middlename)

        self.box_gender = QComboBox(self.leftFrame_Button_Main)
        self.box_gender.addItem("")
        self.box_gender.addItem("")
        self.box_gender.setObjectName(u"box_gender")
        self.box_gender.setFont(font3)

        self.verticalLayout_26.addWidget(self.box_gender)

        self.text_age = QLineEdit(self.leftFrame_Button_Main)
        self.text_age.setObjectName(u"text_age")
        self.text_age.setMinimumSize(QSize(0, 30))
        self.text_age.setFont(font3)

        self.verticalLayout_26.addWidget(self.text_age)

        self.text_phone = QLineEdit(self.leftFrame_Button_Main)
        self.text_phone.setObjectName(u"text_phone")
        self.text_phone.setMinimumSize(QSize(0, 30))
        self.text_phone.setFont(font3)

        self.verticalLayout_26.addWidget(self.text_phone)

        self.text_city = QLineEdit(self.leftFrame_Button_Main)
        self.text_city.setObjectName(u"text_city")
        self.text_city.setMinimumSize(QSize(0, 30))
        self.text_city.setFont(font3)

        self.verticalLayout_26.addWidget(self.text_city)


        self.horizontalLayout_14.addWidget(self.leftFrame_Button_Main)


        self.verticalLayout_30.addWidget(self.frame_7)

        self.leftFrame_Buttons = QFrame(self.leftFrame_Edits)
        self.leftFrame_Buttons.setObjectName(u"leftFrame_Buttons")
        self.leftFrame_Buttons.setMinimumSize(QSize(0, 85))
        self.leftFrame_Buttons.setMaximumSize(QSize(16777215, 80))
        self.leftFrame_Buttons.setLayoutDirection(Qt.LeftToRight)
        self.leftFrame_Buttons.setStyleSheet(u"")
        self.leftFrame_Buttons.setFrameShape(QFrame.StyledPanel)
        self.leftFrame_Buttons.setFrameShadow(QFrame.Raised)
        self.leftFrame_Buttons.setLineWidth(1)
        self.verticalLayout_27 = QVBoxLayout(self.leftFrame_Buttons)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.btn_Append = QPushButton(self.leftFrame_Buttons)
        self.btn_Append.setObjectName(u"btn_Append")
        self.btn_Append.setMinimumSize(QSize(0, 30))
        self.btn_Append.setMaximumSize(QSize(16777215, 30))
        self.btn_Append.setFont(font3)

        self.verticalLayout_27.addWidget(self.btn_Append)

        self.btn_text_clean = QPushButton(self.leftFrame_Buttons)
        self.btn_text_clean.setObjectName(u"btn_text_clean")
        self.btn_text_clean.setMinimumSize(QSize(0, 30))
        self.btn_text_clean.setMaximumSize(QSize(16777215, 30))
        self.btn_text_clean.setFont(font3)

        self.verticalLayout_27.addWidget(self.btn_text_clean)


        self.verticalLayout_30.addWidget(self.leftFrame_Buttons)


        self.verticalLayout_23.addWidget(self.leftFrame_Edits)

        self.frame_5 = QFrame(self.leftFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.leftFrame)

        self.rightFrame = QFrame(self.page_table)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setStyleSheet(u"QFrame#frame, frame_2 {\n"
"	background-color: rgb(29, 29, 29);\n"
"	border-radius: 20px;\n"
"}")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.table_upFrame = QFrame(self.rightFrame)
        self.table_upFrame.setObjectName(u"table_upFrame")
        self.table_upFrame.setMinimumSize(QSize(0, 50))
        self.table_upFrame.setMaximumSize(QSize(16777215, 50))
        self.table_upFrame.setStyleSheet(u"")
        self.table_upFrame.setFrameShape(QFrame.StyledPanel)
        self.table_upFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.table_upFrame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.table_upFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(60, 16777215))
        self.label_11.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_11)

        self.box_find = QComboBox(self.table_upFrame)
        self.box_find.addItem("")
        self.box_find.addItem("")
        self.box_find.addItem("")
        self.box_find.addItem("")
        self.box_find.addItem("")
        self.box_find.addItem("")
        self.box_find.addItem("")
        self.box_find.addItem("")
        self.box_find.setObjectName(u"box_find")
        self.box_find.setMinimumSize(QSize(0, 30))
        self.box_find.setMaximumSize(QSize(140, 30))
        self.box_find.setFont(font3)

        self.horizontalLayout_13.addWidget(self.box_find)

        self.text_find = QLineEdit(self.table_upFrame)
        self.text_find.setObjectName(u"text_find")
        self.text_find.setMinimumSize(QSize(0, 30))
        self.text_find.setMaximumSize(QSize(120, 30))
        self.text_find.setFont(font3)

        self.horizontalLayout_13.addWidget(self.text_find)

        self.box_gender_select = QComboBox(self.table_upFrame)
        self.box_gender_select.addItem("")
        self.box_gender_select.addItem("")
        self.box_gender_select.setObjectName(u"box_gender_select")
        self.box_gender_select.setEnabled(True)
        self.box_gender_select.setMaximumSize(QSize(140, 30))

        self.horizontalLayout_13.addWidget(self.box_gender_select)

        self.btn_Find = QPushButton(self.table_upFrame)
        self.btn_Find.setObjectName(u"btn_Find")
        self.btn_Find.setMinimumSize(QSize(0, 30))
        self.btn_Find.setMaximumSize(QSize(80, 30))
        self.btn_Find.setFont(font3)

        self.horizontalLayout_13.addWidget(self.btn_Find)

        self.frame_6 = QFrame(self.table_upFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_6)

        self.btn_find_clean = QPushButton(self.table_upFrame)
        self.btn_find_clean.setObjectName(u"btn_find_clean")
        self.btn_find_clean.setMinimumSize(QSize(0, 30))
        self.btn_find_clean.setMaximumSize(QSize(75, 30))
        self.btn_find_clean.setFont(font3)

        self.horizontalLayout_13.addWidget(self.btn_find_clean)


        self.verticalLayout_22.addWidget(self.table_upFrame)

        self.table_bottomFrame = QFrame(self.rightFrame)
        self.table_bottomFrame.setObjectName(u"table_bottomFrame")
        self.table_bottomFrame.setStyleSheet(u"")
        self.table_bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.table_bottomFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.table_bottomFrame)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, -1, 9, -1)
        self.frame_3 = QFrame(self.table_bottomFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setMaximumSize(QSize(105, 16777215))
        self.label_10.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.box_sort = QComboBox(self.frame_3)
        self.box_sort.addItem("")
        self.box_sort.addItem("")
        self.box_sort.addItem("")
        self.box_sort.addItem("")
        self.box_sort.addItem("")
        self.box_sort.addItem("")
        self.box_sort.addItem("")
        self.box_sort.addItem("")
        self.box_sort.setObjectName(u"box_sort")
        self.box_sort.setMinimumSize(QSize(0, 30))
        self.box_sort.setMaximumSize(QSize(140, 30))
        self.box_sort.setFont(font3)

        self.horizontalLayout_8.addWidget(self.box_sort)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_4)

        self.label_name_import = QLabel(self.frame_3)
        self.label_name_import.setObjectName(u"label_name_import")
        self.label_name_import.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_name_import)

        self.btn_table_refresh = QPushButton(self.frame_3)
        self.btn_table_refresh.setObjectName(u"btn_table_refresh")
        self.btn_table_refresh.setMinimumSize(QSize(0, 30))
        self.btn_table_refresh.setMaximumSize(QSize(75, 30))
        self.btn_table_refresh.setFont(font3)

        self.horizontalLayout_8.addWidget(self.btn_table_refresh)


        self.verticalLayout_28.addWidget(self.frame_3)

        self.tableWidget_2 = QTableWidget(self.table_bottomFrame)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget_2.rowCount() < 5):
            self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_2.setFrameShadow(QFrame.Sunken)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setDragEnabled(False)
        self.tableWidget_2.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_2.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_28.addWidget(self.tableWidget_2)


        self.verticalLayout_22.addWidget(self.table_bottomFrame)


        self.horizontalLayout.addWidget(self.rightFrame)

        self.stackedWidget.addWidget(self.page_table)
        self.page_weather = QWidget()
        self.page_weather.setObjectName(u"page_weather")
        self.horizontalLayout_6 = QHBoxLayout(self.page_weather)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.leftFrame_2 = QFrame(self.page_weather)
        self.leftFrame_2.setObjectName(u"leftFrame_2")
        self.leftFrame_2.setMinimumSize(QSize(0, 0))
        self.leftFrame_2.setMaximumSize(QSize(250, 250))
        self.leftFrame_2.setFrameShape(QFrame.StyledPanel)
        self.leftFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.leftFrame_2)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.groupBox = QGroupBox(self.leftFrame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 120))
        font6 = QFont()
        self.groupBox.setFont(font6)
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.rb_ip = QRadioButton(self.groupBox)
        self.rb_ip.setObjectName(u"rb_ip")
        self.rb_ip.setFont(font3)
        self.rb_ip.setCheckable(True)
        self.rb_ip.setChecked(True)
        self.rb_ip.setAutoRepeat(False)

        self.verticalLayout_20.addWidget(self.rb_ip)

        self.rb_text = QRadioButton(self.groupBox)
        self.rb_text.setObjectName(u"rb_text")
        self.rb_text.setFont(font3)
        self.rb_text.setChecked(False)

        self.verticalLayout_20.addWidget(self.rb_text)


        self.verticalLayout_40.addWidget(self.groupBox)

        self.text_weather_city = QLineEdit(self.leftFrame_2)
        self.text_weather_city.setObjectName(u"text_weather_city")
        self.text_weather_city.setMinimumSize(QSize(0, 30))
        self.text_weather_city.setFont(font3)

        self.verticalLayout_40.addWidget(self.text_weather_city)

        self.btn_weather_enter = QPushButton(self.leftFrame_2)
        self.btn_weather_enter.setObjectName(u"btn_weather_enter")
        self.btn_weather_enter.setMinimumSize(QSize(0, 30))
        self.btn_weather_enter.setFont(font3)

        self.verticalLayout_40.addWidget(self.btn_weather_enter)


        self.horizontalLayout_6.addWidget(self.leftFrame_2)

        self.rightFrame_2 = QFrame(self.page_weather)
        self.rightFrame_2.setObjectName(u"rightFrame_2")
        self.rightFrame_2.setMinimumSize(QSize(0, 0))
        self.rightFrame_2.setMaximumSize(QSize(400, 545))
        self.rightFrame_2.setFrameShape(QFrame.StyledPanel)
        self.rightFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.rightFrame_2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_weather_title = QFrame(self.rightFrame_2)
        self.frame_weather_title.setObjectName(u"frame_weather_title")
        self.frame_weather_title.setMaximumSize(QSize(16777215, 70))
        self.frame_weather_title.setFrameShape(QFrame.StyledPanel)
        self.frame_weather_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_weather_title)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_weather_title = QLabel(self.frame_weather_title)
        self.label_weather_title.setObjectName(u"label_weather_title")
        font7 = QFont()
        font7.setPointSize(14)
        self.label_weather_title.setFont(font7)
        self.label_weather_title.setLineWidth(1)
        self.label_weather_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_weather_title)

        self.label_weather_last = QLabel(self.frame_weather_title)
        self.label_weather_last.setObjectName(u"label_weather_last")
        self.label_weather_last.setFont(font4)
        self.label_weather_last.setLineWidth(1)
        self.label_weather_last.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_weather_last)


        self.verticalLayout_41.addWidget(self.frame_weather_title)

        self.frame_weather_image = QFrame(self.rightFrame_2)
        self.frame_weather_image.setObjectName(u"frame_weather_image")
        self.frame_weather_image.setMaximumSize(QSize(16777215, 100))
        self.frame_weather_image.setLayoutDirection(Qt.LeftToRight)
        self.frame_weather_image.setFrameShape(QFrame.StyledPanel)
        self.frame_weather_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_weather_image)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 9, -1, -1)
        self.frame_image = QFrame(self.frame_weather_image)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setMinimumSize(QSize(100, 100))
        self.frame_image.setMaximumSize(QSize(100, 100))
        self.frame_image.setStyleSheet(u"QFrame#frame_image {\n"
"	background-color: transparent;\n"
"}")
        self.frame_image.setFrameShape(QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_image)


        self.verticalLayout_41.addWidget(self.frame_weather_image)

        self.frame_16 = QFrame(self.rightFrame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 70))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_16)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_weather_temp = QLabel(self.frame_16)
        self.label_weather_temp.setObjectName(u"label_weather_temp")
        self.label_weather_temp.setFont(font4)
        self.label_weather_temp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_weather_temp)

        self.label_weather_description = QLabel(self.frame_16)
        self.label_weather_description.setObjectName(u"label_weather_description")
        self.label_weather_description.setFont(font4)
        self.label_weather_description.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_weather_description)


        self.verticalLayout_41.addWidget(self.frame_16)

        self.frame_weather_info = QFrame(self.rightFrame_2)
        self.frame_weather_info.setObjectName(u"frame_weather_info")
        self.frame_weather_info.setFrameShape(QFrame.StyledPanel)
        self.frame_weather_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_weather_info)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_weather_feelslike = QLabel(self.frame_weather_info)
        self.label_weather_feelslike.setObjectName(u"label_weather_feelslike")
        self.label_weather_feelslike.setFont(font4)
        self.label_weather_feelslike.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_weather_feelslike)

        self.label_weather_humidity = QLabel(self.frame_weather_info)
        self.label_weather_humidity.setObjectName(u"label_weather_humidity")
        self.label_weather_humidity.setFont(font4)
        self.label_weather_humidity.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_weather_humidity)

        self.label_weather_visibility = QLabel(self.frame_weather_info)
        self.label_weather_visibility.setObjectName(u"label_weather_visibility")
        self.label_weather_visibility.setFont(font4)
        self.label_weather_visibility.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_weather_visibility)

        self.label_weather_wind = QLabel(self.frame_weather_info)
        self.label_weather_wind.setObjectName(u"label_weather_wind")
        self.label_weather_wind.setFont(font4)
        self.label_weather_wind.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_weather_wind)

        self.label_weather_sunrise = QLabel(self.frame_weather_info)
        self.label_weather_sunrise.setObjectName(u"label_weather_sunrise")
        self.label_weather_sunrise.setFont(font4)
        self.label_weather_sunrise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_weather_sunrise)

        self.label_weather_sunset = QLabel(self.frame_weather_info)
        self.label_weather_sunset.setObjectName(u"label_weather_sunset")
        self.label_weather_sunset.setFont(font4)
        self.label_weather_sunset.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_weather_sunset)


        self.verticalLayout_41.addWidget(self.frame_weather_info)


        self.horizontalLayout_6.addWidget(self.rightFrame_2)

        self.stackedWidget.addWidget(self.page_weather)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_theme = QPushButton(self.topMenus)
        self.btn_theme.setObjectName(u"btn_theme")
        sizePolicy2.setHeightForWidth(self.btn_theme.sizePolicy().hasHeightForWidth())
        self.btn_theme.setSizePolicy(sizePolicy2)
        self.btn_theme.setMinimumSize(QSize(0, 45))
        self.btn_theme.setFont(font)
        self.btn_theme.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_theme.setLayoutDirection(Qt.LeftToRight)
        self.btn_theme.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_theme)

        self.btn_titlebar = QPushButton(self.topMenus)
        self.btn_titlebar.setObjectName(u"btn_titlebar")
        sizePolicy2.setHeightForWidth(self.btn_titlebar.sizePolicy().hasHeightForWidth())
        self.btn_titlebar.setSizePolicy(sizePolicy2)
        self.btn_titlebar.setMinimumSize(QSize(0, 45))
        self.btn_titlebar.setFont(font)
        self.btn_titlebar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_titlebar.setLayoutDirection(Qt.LeftToRight)
        self.btn_titlebar.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_titlebar)

        self.btn_save_settings = QPushButton(self.topMenus)
        self.btn_save_settings.setObjectName(u"btn_save_settings")
        sizePolicy2.setHeightForWidth(self.btn_save_settings.sizePolicy().hasHeightForWidth())
        self.btn_save_settings.setSizePolicy(sizePolicy2)
        self.btn_save_settings.setMinimumSize(QSize(0, 45))
        self.btn_save_settings.setFont(font)
        self.btn_save_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_save_settings.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_save_settings)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setBold(False)
        font8.setItalic(False)
        self.creditsLabel.setFont(font8)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_21.addWidget(self.bgApp)


        self.appMargins.addWidget(self.backMainFrame)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Python Program 2021", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0423\u043c\u0435\u043d\u044c\u0448\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("MainWindow", u"          \u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"  \u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f - \u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
#if QT_CONFIG(tooltip)
        self.btn_export.setToolTip(QCoreApplication.translate("MainWindow", u"          \u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
#endif // QT_CONFIG(tooltip)
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"  \u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
#if QT_CONFIG(tooltip)
        self.btn_import.setToolTip(QCoreApplication.translate("MainWindow", u"          \u0418\u043c\u043f\u043e\u0440\u0442", None))
#endif // QT_CONFIG(tooltip)
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"  \u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
#if QT_CONFIG(tooltip)
        self.btn_save.setToolTip(QCoreApplication.translate("MainWindow", u"          \u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"  \u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0432 \u0411\u0414", None))
#if QT_CONFIG(tooltip)
        self.btn_weather.setToolTip(QCoreApplication.translate("MainWindow", u"          \u041f\u043e\u0433\u043e\u0434\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btn_weather.setText(QCoreApplication.translate("MainWindow", u"  \u041f\u043e\u0433\u043e\u0434\u0430", None))
#if QT_CONFIG(tooltip)
        self.toggleLeftBox.setToolTip(QCoreApplication.translate("MainWindow", u"     \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_info.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.btn_db.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.btn_author.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0438\u043b\u0438 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438\n"
"\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u041a\u043e\u0434.\n"
"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0434 \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 Enter\n"
"\u0447\u0442\u043e\u0431\u044b \u0443\u0432\u0438\u0434\u0435\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e\n"
"\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0435, \u0432 \u043d\u0438\u0436\u043d\u0435\u043c \u0431\u043b\u043e\u043a\u0435.\n"
"\u041a\u043e\u0434 \u0433\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439!", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0442\u043e\u0433\u043e, \u0447\u0442\u043e\u0431\u044b \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443\n"
"\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f \u043a \u0411\u0414. \u0414\u043b\u044f\n"
"\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u043d\u0435\n"
"\u043d\u0443\u0436\u043d\u043e \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0430\u0442\u044c\u0441\u044f, \u043d\u043e \u0435\u0441\u043b\u0438 \u0432\u044b\n"
"\u0437\u0430\u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443, \u0442\u043e\n"
"\u043d\u0443\u0436\u043d\u043e \u0431\u0443\u0434\u0435\u0442 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445, \u0442\u0435\u043c\u044b \u0438\n"
"\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f \u0432\n"
"\u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e\u043c \u0444\u0430\u0439\u043b\u0435 \"config.ini\". \u0415\u0441\u043b\u0438\n"
"\u043e\u043d \u0443\u0434\u0430\u043b\u0438\u0442\u0441\u044f, \u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\n"
"\u0437\u0430\u043d\u043e\u0432\u043e \u0441 \u0441\u0442\u043e\u043a\u043e\u0432\u044b\u043c\u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c\u0438.", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u0432 \u043f\u0430\u043f\u043a\u0443\n"
"Export, \u0430 \u0434\u0430\u043b\u044c\u0448\u0435 \u0441\u043e\u0437\u0434\u0430\u0435\u0442\u0441\u044f \u043f\u0430\u043f\u043a\u0430, \u0441\n"
"\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435\u043c \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0432 \u0411\u0414.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DB", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0411\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.btn_db_connector.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.btn_db_loadconfig.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.btn_db_save.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.label_2.setText("")
        self.label_author_1.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b: \u0413\u0430\u0431\u0434\u0443\u043b\u043b\u0438\u043d \u0410.\u041c.", None))
        self.label_author_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435: KZ, Pavlodar", None))
        self.label_author_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0438: 2021 \u0433.", None))
        self.label_author_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u044c: @theRoone (Telegram)", None))
        self.label_author_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0441\u0435\u0432\u0434\u043e\u043d\u0438\u043c \u0430\u0432\u0442\u043e\u0440\u0430: theRoone", None))
        self.label_Title.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0430", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
        self.text_id.setText("")
        self.btn_Remove.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_Update.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_lastname.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_firstname.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.label_middlename.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_gender.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b", None))
        self.label_age.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.label_phone.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u043e\u0432\u044b\u0439", None))
        self.label_city.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.text_lastname.setText("")
        self.box_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0443\u0436\u0441\u043a\u043e\u0439", None))
        self.box_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0416\u0435\u043d\u0441\u043a\u0438\u0439", None))

        self.text_age.setText("")
        self.btn_Append.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_text_clean.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e:", None))
        self.box_find.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
        self.box_find.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.box_find.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.box_find.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.box_find.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b", None))
        self.box_find.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.box_find.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u043e\u0432\u044b\u0439", None))
        self.box_find.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))

        self.text_find.setText("")
        self.box_gender_select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0443\u0436\u0441\u043a\u043e\u0439", None))
        self.box_gender_select.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0416\u0435\u043d\u0441\u043a\u0438\u0439", None))

        self.btn_Find.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.btn_find_clean.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e:", None))
        self.box_sort.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
        self.box_sort.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.box_sort.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.box_sort.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.box_sort.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b", None))
        self.box_sort.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.box_sort.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u043e\u0432\u044b\u0439", None))
        self.box_sort.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))

        self.label_name_import.setText("")
        self.btn_table_refresh.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u043e\u0432\u044b\u0439", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None));
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.rb_ip.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e IP \u0430\u0434\u0440\u0435\u0441\u0443", None))
        self.rb_text.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u0433\u043e\u0440\u043e\u0434\u0430", None))
        self.btn_weather_enter.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_weather_title.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0433\u043e\u0440\u043e\u0434: \u041f\u0430\u0432\u043b\u043e\u0434\u0430\u0440", None))
        self.label_weather_last.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435:", None))
        self.label_weather_temp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430:", None))
        self.label_weather_description.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0441\u043d\u043e", None))
        self.label_weather_feelslike.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0449\u0443\u0449\u0430\u0435\u0442\u0441\u044f \u043a\u0430\u043a:", None))
        self.label_weather_humidity.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_weather_visibility.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0438\u043c\u043e\u0441\u0442\u044c:", None))
        self.label_weather_wind.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0442\u0435\u0440:", None))
        self.label_weather_sunrise.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0432\u0435\u0442:", None))
        self.label_weather_sunset.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0442:", None))
        self.btn_theme.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430 \u0421\u0432\u0435\u0442\u043b\u0443\u044e \u0442\u0435\u043c\u0443", None))
        self.btn_titlebar.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.btn_save_settings.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u" Copyright \u00a9 theRoone 2021", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"version 1.0", None))
    # retranslateUi

