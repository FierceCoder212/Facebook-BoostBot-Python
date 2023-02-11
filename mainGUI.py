# -*- coding: utf-8 -*-
import json
import threading
from json import JSONDecodeError

import requests

from addUsersGUI import Ui_add_users
from removeUsersGUI import Ui_rempve_users
from showBlockedGUI import Ui_Dialog
from postsUI import Ui_posts_ui
from dialog_box import Ui_Dialog

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        self.api_key = '538dcca636f3c67f4b69c1626d8f202d'
        self.api_string = 'https://smmfollows.com/api/v2'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 682)
        MainWindow.showMaximized()
        MainWindow.setAttribute(Qt.WA_DeleteOnClose)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/facebook (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background:rgb(22, 33, 62)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(801, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.right_buttons_wgt = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_buttons_wgt.sizePolicy().hasHeightForWidth())
        self.right_buttons_wgt.setSizePolicy(sizePolicy)
        self.right_buttons_wgt.setMinimumSize(QtCore.QSize(200, 0))
        self.right_buttons_wgt.setMaximumSize(QtCore.QSize(200, 16777215))
        self.right_buttons_wgt.setObjectName("right_buttons_wgt")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.right_buttons_wgt)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.unselect_all_btn = QtWidgets.QPushButton(self.right_buttons_wgt)
        self.unselect_all_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.unselect_all_btn.setStyleSheet("QPushButton { \n"
                                            "    background:rgb(160, 132, 202); \n"
                                            "    color:white;\n"
                                            "    border: 2px solid rgb(164, 136, 207);\n"
                                            "      border-radius: 5px;\n"
                                            "    height:20px;\n"
                                            "    width:50px;\n"
                                            " }\n"
                                            "QPushButton:hover { \n"
                                            "    background:rgb(164, 136, 207);\n"
                                            "border: 2px solid rgb(160, 132, 202);\n"
                                            "      border-radius: 5px;\n"
                                            "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/eliminate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unselect_all_btn.setIcon(icon1)
        self.unselect_all_btn.setObjectName("unselect_all_btn")
        self.verticalLayout.addWidget(self.unselect_all_btn)
        self.select_all_btn = QtWidgets.QPushButton(self.right_buttons_wgt)
        self.select_all_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_all_btn.setStyleSheet("QPushButton { \n"
                                          "    background:rgb(160, 132, 202); \n"
                                          "    color:white;\n"
                                          "    border: 2px solid rgb(164, 136, 207);\n"
                                          "      border-radius: 5px;\n"
                                          "    height:20px;\n"
                                          "    width:50px;\n"
                                          " }\n"
                                          "QPushButton:hover { \n"
                                          "    background:rgb(164, 136, 207);\n"
                                          "border: 2px solid rgb(160, 132, 202);\n"
                                          "      border-radius: 5px;\n"
                                          "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/selection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_all_btn.setIcon(icon2)
        self.select_all_btn.setObjectName("select_all_btn")
        self.verticalLayout.addWidget(self.select_all_btn)
        self.block_btn = QtWidgets.QPushButton(self.right_buttons_wgt)
        self.block_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.block_btn.setStyleSheet("QPushButton { \n"
                                     "    background:rgb(160, 132, 202); \n"
                                     "    color:white;\n"
                                     "    border: 2px solid rgb(164, 136, 207);\n"
                                     "      border-radius: 5px;\n"
                                     "    height:20px;\n"
                                     "    width:50px;\n"
                                     " }\n"
                                     "QPushButton:hover { \n"
                                     "    background:rgb(164, 136, 207);\n"
                                     "border: 2px solid rgb(160, 132, 202);\n"
                                     "      border-radius: 5px;\n"
                                     "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.block_btn.setIcon(icon3)
        self.block_btn.setObjectName("block_btn")
        self.verticalLayout.addWidget(self.block_btn)
        self.show_btn = QtWidgets.QPushButton(self.right_buttons_wgt)
        self.show_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_btn.setStyleSheet("QPushButton { \n"
                                    "    background:rgb(160, 132, 202); \n"
                                    "    color:white;\n"
                                    "    border: 2px solid rgb(164, 136, 207);\n"
                                    "      border-radius: 5px;\n"
                                    "    height:20px;\n"
                                    "    width:50px;\n"
                                    " }\n"
                                    "QPushButton:hover { \n"
                                    "    background:rgb(164, 136, 207);\n"
                                    "border: 2px solid rgb(160, 132, 202);\n"
                                    "      border-radius: 5px;\n"
                                    "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/visibility.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_btn.setIcon(icon4)
        self.show_btn.setObjectName("show_btn")
        self.verticalLayout.addWidget(self.show_btn)
        self.gridLayout.addWidget(self.right_buttons_wgt, 3, 3, 3, 1, QtCore.Qt.AlignTop)
        self.title_wgt = QtWidgets.QWidget(self.centralwidget)
        self.title_wgt.setObjectName("title_wgt")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.title_wgt)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_style_wgt = QtWidgets.QWidget(self.title_wgt)
        self.title_style_wgt.setObjectName("title_style_wgt")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_style_wgt)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fb_icon_lbl = QtWidgets.QLabel(self.title_style_wgt)
        self.fb_icon_lbl.setText("")
        self.fb_icon_lbl.setPixmap(QtGui.QPixmap("images/facebook (3).png"))
        self.fb_icon_lbl.setObjectName("fb_icon_lbl")
        self.horizontalLayout.addWidget(self.fb_icon_lbl)
        self.title_lbl = QtWidgets.QLabel(self.title_style_wgt)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("color:rgb(127, 188, 210);")
        self.title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.horizontalLayout.addWidget(self.title_lbl)
        self.verticalLayout_2.addWidget(self.title_style_wgt)
        self.underline_lbl = QtWidgets.QLabel(self.title_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.underline_lbl.sizePolicy().hasHeightForWidth())
        self.underline_lbl.setSizePolicy(sizePolicy)
        self.underline_lbl.setMinimumSize(QtCore.QSize(125, 2))
        self.underline_lbl.setMaximumSize(QtCore.QSize(125, 4))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        self.underline_lbl.setFont(font)
        self.underline_lbl.setStyleSheet("QLabel{\n"
                                         "background:rgb(127, 188, 210);\n"
                                         "}")
        self.underline_lbl.setText("")
        self.underline_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.underline_lbl.setObjectName("underline_lbl")
        self.verticalLayout_2.addWidget(self.underline_lbl, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.title_wgt, 0, 0, 1, 4, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.copyRight_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.copyRight_lbl.setFont(font)
        self.copyRight_lbl.setStyleSheet("color:rgb(255, 255, 255);\n"
                                         "font: 8pt \"OCR A Extended\";")
        self.copyRight_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.copyRight_lbl.setObjectName("copyRight_lbl")
        self.gridLayout.addWidget(self.copyRight_lbl, 7, 0, 1, 4)
        self.combo_box_wgt = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_box_wgt.sizePolicy().hasHeightForWidth())
        self.combo_box_wgt.setSizePolicy(sizePolicy)
        self.combo_box_wgt.setObjectName("combo_box_wgt")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.combo_box_wgt)
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.wgt = QtWidgets.QWidget(self.combo_box_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wgt.sizePolicy().hasHeightForWidth())
        self.wgt.setSizePolicy(sizePolicy)
        self.wgt.setObjectName("wgt")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wgt)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.wgt)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.services_label_wgt = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.services_label_wgt.sizePolicy().hasHeightForWidth())
        self.services_label_wgt.setSizePolicy(sizePolicy)
        self.services_label_wgt.setObjectName("services_label_wgt")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.services_label_wgt)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.services_icon_lbl = QtWidgets.QLabel(self.services_label_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.services_icon_lbl.sizePolicy().hasHeightForWidth())
        self.services_icon_lbl.setSizePolicy(sizePolicy)
        self.services_icon_lbl.setText("")
        self.services_icon_lbl.setPixmap(QtGui.QPixmap("images/info.png"))
        self.services_icon_lbl.setObjectName("services_icon_lbl")
        self.horizontalLayout_4.addWidget(self.services_icon_lbl)
        self.services_lbl = QtWidgets.QLabel(self.services_label_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.services_lbl.sizePolicy().hasHeightForWidth())
        self.services_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.services_lbl.setFont(font)
        self.services_lbl.setStyleSheet("color:white;")
        self.services_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.services_lbl.setObjectName("services_lbl")
        self.horizontalLayout_4.addWidget(self.services_lbl)
        self.horizontalLayout_5.addWidget(self.services_label_wgt, 0, QtCore.Qt.AlignBottom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.refresh_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_btn.sizePolicy().hasHeightForWidth())
        self.refresh_btn.setSizePolicy(sizePolicy)
        self.refresh_btn.setMinimumSize(QtCore.QSize(25, 25))
        self.refresh_btn.setMaximumSize(QtCore.QSize(25, 25))
        self.refresh_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_btn.setToolTip("")
        self.refresh_btn.setStyleSheet("QPushButton { \n"
                                       "    background:rgb(160, 132, 202); \n"
                                       "    color:white;\n"
                                       "    border: 2px solid rgb(164, 136, 207);\n"
                                       "      border-radius: 5px;\n"
                                       "    height:20px;\n"
                                       "    width:50px;\n"
                                       " }\n"
                                       "QPushButton:hover { \n"
                                       "    background:rgb(164, 136, 207);\n"
                                       "border: 2px solid rgb(160, 132, 202);\n"
                                       "      border-radius: 5px;\n"
                                       "}")
        self.refresh_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/refresh-page-option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon5)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout_5.addWidget(self.refresh_btn)
        self.verticalLayout_3.addWidget(self.widget)
        self.followers_cmboBox = QtWidgets.QComboBox(self.wgt)
        self.followers_cmboBox.setMinimumSize(QtCore.QSize(0, 20))
        self.followers_cmboBox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.followers_cmboBox.setStyleSheet("QComboBox QAbstractItemView{\n"
                                             "background-color:white;\n"
                                             "}\n"
                                             "QComboBox QAbstractItemView QScrollBar:vertical\n"
                                             "                            {\n"
                                             "                       color:black;\n"
                                             "background:white;\n"
                                             "                            }\n"
                                             "\n"
                                             "QComboBox {\n"
                                             "border: 1px solid  rgb(164, 136, 207);\n"
                                             "background-color:white;\n"
                                             "border-radius:5px;\n"
                                             "height:20px;\n"
                                             "}")
        self.followers_cmboBox.setIconSize(QtCore.QSize(20, 20))
        self.followers_cmboBox.setObjectName("followers_cmboBox")
        self.verticalLayout_3.addWidget(self.followers_cmboBox)
        self.verticalLayout_5.addWidget(self.wgt)
        self.gridLayout.addWidget(self.combo_box_wgt, 4, 0, 1, 3)
        self.top_buttons_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_buttons_widget.sizePolicy().hasHeightForWidth())
        self.top_buttons_widget.setSizePolicy(sizePolicy)
        self.top_buttons_widget.setMinimumSize(QtCore.QSize(400, 0))
        self.top_buttons_widget.setObjectName("top_buttons_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_buttons_widget)
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addUsers_btn = QtWidgets.QPushButton(self.top_buttons_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addUsers_btn.sizePolicy().hasHeightForWidth())
        self.addUsers_btn.setSizePolicy(sizePolicy)
        self.addUsers_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.addUsers_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addUsers_btn.setToolTip("")
        self.addUsers_btn.setAutoFillBackground(False)
        self.addUsers_btn.setStyleSheet("QPushButton { \n"
                                        "    background: rgb(0, 179, 0); \n"
                                        "    color:white;\n"
                                        "    border: 2px solid rgb(0, 190, 0);\n"
                                        "      border-radius: 5px;\n"
                                        "    height:20px;\n"
                                        "    width:50px;\n"
                                        "    icon.name: \"add-user\";\n"
                                        "    icon.source: \"images/add-user.png\";\n"
                                        "    icon.color: black;\n"
                                        " }\n"
                                        "QPushButton:hover { \n"
                                        "    background: rgb(0, 190, 0);\n"
                                        "    border: 2px solid  rgb(0, 179, 0);\n"
                                        "      border-radius: 5px;\n"
                                        "}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/addUser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addUsers_btn.setIcon(icon6)
        self.addUsers_btn.setObjectName("addUsers_btn")
        self.horizontalLayout_3.addWidget(self.addUsers_btn)
        self.removeUser_btn = QtWidgets.QPushButton(self.top_buttons_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeUser_btn.sizePolicy().hasHeightForWidth())
        self.removeUser_btn.setSizePolicy(sizePolicy)
        self.removeUser_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.removeUser_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeUser_btn.setToolTip("")
        self.removeUser_btn.setStyleSheet("QPushButton { \n"
                                          "    background:rgb(218, 0, 0); \n"
                                          "    color:white;\n"
                                          "    border: 2px solid rgb(234, 0, 0);\n"
                                          "      border-radius: 5px;\n"
                                          "    height:20px;\n"
                                          "    width:50px;\n"
                                          " }\n"
                                          "QPushButton:hover { \n"
                                          "    background: rgb(234, 0, 0);\n"
                                          "border: 2px solid rgb(218, 0, 0);\n"
                                          "      border-radius: 5px;\n"
                                          "}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/remove-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeUser_btn.setIcon(icon7)
        self.removeUser_btn.setObjectName("removeUser_btn")
        self.horizontalLayout_3.addWidget(self.removeUser_btn)
        self.gridLayout.addWidget(self.top_buttons_widget, 1, 0, 1, 1)
        self.bottom_buttons_wgt = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_buttons_wgt.sizePolicy().hasHeightForWidth())
        self.bottom_buttons_wgt.setSizePolicy(sizePolicy)
        self.bottom_buttons_wgt.setMinimumSize(QtCore.QSize(200, 0))
        self.bottom_buttons_wgt.setObjectName("bottom_buttons_wgt")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.bottom_buttons_wgt)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bottom_txt_wgt = QtWidgets.QWidget(self.bottom_buttons_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_txt_wgt.sizePolicy().hasHeightForWidth())
        self.bottom_txt_wgt.setSizePolicy(sizePolicy)
        self.bottom_txt_wgt.setMinimumSize(QtCore.QSize(400, 0))
        self.bottom_txt_wgt.setObjectName("bottom_txt_wgt")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_txt_wgt)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.quantity_lbl = QtWidgets.QLabel(self.bottom_txt_wgt)
        self.quantity_lbl.setStyleSheet("color:white;")
        self.quantity_lbl.setObjectName("quantity_lbl")
        self.horizontalLayout_2.addWidget(self.quantity_lbl)
        self.quantity_txt = QtWidgets.QLineEdit(self.bottom_txt_wgt)
        self.quantity_txt.setStyleSheet("background:white;")
        self.quantity_txt.setObjectName("quantity_txt")
        self.horizontalLayout_2.addWidget(self.quantity_txt)
        self.price_lbl = QtWidgets.QLabel(self.bottom_txt_wgt)
        self.price_lbl.setStyleSheet("color:white;")
        self.price_lbl.setObjectName("price_lbl")
        self.horizontalLayout_2.addWidget(self.price_lbl)
        self.price_txt = QtWidgets.QLineEdit(self.bottom_txt_wgt)
        self.price_txt.setStyleSheet("background:white;")
        self.price_txt.setReadOnly(True)
        self.price_txt.setObjectName("price_txt")
        self.horizontalLayout_2.addWidget(self.price_txt)
        self.verticalLayout_4.addWidget(self.bottom_txt_wgt)
        self.process_posts_chk_box = QtWidgets.QCheckBox(self.bottom_buttons_wgt)
        self.process_posts_chk_box.setStyleSheet("color:white;")
        self.process_posts_chk_box.setObjectName("process_posts_chk_box")
        self.verticalLayout_4.addWidget(self.process_posts_chk_box)
        self.process_user_chk_box = QtWidgets.QCheckBox(self.bottom_buttons_wgt)
        self.process_user_chk_box.setStyleSheet("color:white;")
        self.process_user_chk_box.setObjectName("process_user_chk_box")
        self.verticalLayout_4.addWidget(self.process_user_chk_box)
        self.process_request_btn = QtWidgets.QPushButton(self.bottom_buttons_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_request_btn.sizePolicy().hasHeightForWidth())
        self.process_request_btn.setSizePolicy(sizePolicy)
        self.process_request_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.process_request_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.process_request_btn.setStyleSheet("QPushButton { \n"
                                               "    background:rgb(160, 132, 202); \n"
                                               "    color:white;\n"
                                               "    border: 2px solid rgb(164, 136, 207);\n"
                                               "      border-radius: 5px;\n"
                                               "    height:20px;\n"
                                               "    width:50px;\n"
                                               " }\n"
                                               "QPushButton:hover { \n"
                                               "    background:rgb(164, 136, 207);\n"
                                               "border: 2px solid rgb(160, 132, 202);\n"
                                               "      border-radius: 5px;\n"
                                               "}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/followers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.process_request_btn.setIcon(icon8)
        self.process_request_btn.setObjectName("process_request_btn")
        self.verticalLayout_4.addWidget(self.process_request_btn)
        self.gridLayout.addWidget(self.bottom_buttons_wgt, 6, 0, 1, 2, QtCore.Qt.AlignLeft)
        self.userTabel_tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.userTabel_tbl.setStyleSheet("QTableWidget{\n"
                                         "background:white;\n"
                                         "color:black;\n"
                                         "border: 2px solid rgb(160, 132, 202);\n"
                                         "border-radius:5px;\n"
                                         "}")
        self.userTabel_tbl.setAlternatingRowColors(True)
        self.userTabel_tbl.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.userTabel_tbl.verticalHeader().setVisible(False)
        # self.userTabel_tbl.setSelectionBehavior(QtWidgets.QAbstractItemView.NoSelection)
        self.userTabel_tbl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.userTabel_tbl.setColumnCount(3)
        self.userTabel_tbl.setObjectName("userTabel_tbl")
        self.userTabel_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.userTabel_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTabel_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTabel_tbl.setHorizontalHeaderItem(2, item)
        self.userTabel_tbl.horizontalHeader().setCascadingSectionResizes(True)
        self.userTabel_tbl.horizontalHeader().setSortIndicatorShown(True)
        # self.userTabel_tbl.horizontalHeader().setStretchLastSection(True)
        # self.userTabel_tbl.verticalHeader().setStretchLastSection(True)
        header = self.userTabel_tbl.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.userTabel_tbl.setColumnWidth(0, 5)
        self.userTabel_tbl.setColumnWidth(2, 200)
        self.gridLayout.addWidget(self.userTabel_tbl, 3, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setup_buttons()
        self.load_data()
        self.get_services()

    def setup_buttons(self):
        self.addUsers_btn.clicked.connect(self.add_users)
        self.removeUser_btn.clicked.connect(self.remove_users)
        self.show_btn.clicked.connect(self.show_blocked)
        self.select_all_btn.clicked.connect(self.select_all)
        self.unselect_all_btn.clicked.connect(self.unselect_all)
        self.block_btn.clicked.connect(self.block_selected)
        self.refresh_btn.clicked.connect(self.get_services)
        self.process_request_btn.clicked.connect(self.process_request)
        self.quantity_txt.textChanged.connect(self.set_price)

    def set_price(self):
        try:
            quantity = int(self.quantity_txt.text()) / 1000
            index = self.followers_cmboBox.currentIndex()
            service = self.fb_service_list[index]
            rate = float(service['rate'])
            total = rate * quantity
            self.price_txt.setText(str(round(total, 6)) + '$')
        except ValueError:
            pass

    def load_data(self):
        try:
            users = open('users.json', 'r')
            data = dict(json.load(users))
            row_index = self.userTabel_tbl.rowCount()
            for row in range(0, row_index):
                self.userTabel_tbl.removeRow(0)
            for key in data:
                for user_status in data[key]:
                    selected = user_status
                    if 'true' in selected:
                        row_index = self.userTabel_tbl.rowCount()
                        self.userTabel_tbl.insertRow(row_index)
                        check_box = QtWidgets.QTableWidgetItem()
                        check_box.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        check_box.setCheckState(QtCore.Qt.Checked)
                        posts_btn = self.get_button()
                        self.set_post_button(posts_btn, key)
                        self.userTabel_tbl.setItem(row_index, 0, check_box)
                        self.userTabel_tbl.setItem(row_index, 1, QtWidgets.QTableWidgetItem(key))
                        self.userTabel_tbl.setCellWidget(row_index, 2, posts_btn)
        except (FileNotFoundError, JSONDecodeError):
            pass

    def set_post_button(self, button: QtWidgets.QPushButton, data: str):
        button.clicked.connect(lambda: self.show_posts(data))

    def process_request(self):
        request_str = f'{self.api_string}?key={self.api_key}&action=balance'
        response = requests.get(request_str)
        if response.status_code == 200:
            response = response.json()
            try:
                balance = float(response['balance'])
                amount = float(self.price_txt.text().replace('$', '').strip())
                if balance >= amount:
                    index = self.followers_cmboBox.currentIndex()
                    selected_service = self.fb_service_list[index]
                    min_quantity = int(selected_service['min'])
                    max_quantity = int(selected_service['max'])
                    try:
                        selected_quantity = int(self.quantity_txt.text().strip())
                        if min_quantity <= selected_quantity <= max_quantity:
                            if self.process_posts_chk_box.checkState() == 2 and self.process_user_chk_box.checkState() == 2:
                                self.process_order(selected_service, selected_quantity, posts=True, user=True)
                            elif self.process_posts_chk_box.checkState() == 2:
                                self.process_order(selected_service, selected_quantity, posts=True, user=False)
                            elif self.process_user_chk_box.checkState() == 2:
                                self.process_order(selected_service, selected_quantity, posts=False, user=True)
                            else:
                                self.show_dialogue(f'No process selected', 'Error')
                        else:
                            self.show_dialogue(f'Quantity should be between {min_quantity}-{max_quantity}', 'Error')
                    except ValueError:
                        self.show_dialogue('Quantity Error', 'Error')
                else:
                    self.show_dialogue('Your current balance is not sufficient', 'Error')
            except ValueError:
                self.show_dialogue('Quantity not set', 'Error')
        else:
            self.show_dialogue('Server Error', 'Error')

    def process_order(self, service: dict, quantity: int, posts: bool, user: bool):
        try:
            users = open('users.json', 'r')
            data = dict(json.load(users))
            output = ''
            for key in data:
                for user_status in data[key]:
                    selected = user_status
                    if 'true' in selected:
                        if user:
                            request_str = f'{self.api_string}?key={self.api_key}&action=add&service={service["service"]}&link={key}&quantity={quantity}'
                            response = requests.get(request_str)
                            output += f'{key} : {response.json()}\n'
                        else:
                            output += f'{key}\n'
                        if posts:
                            for post_data in data[key][user_status]:
                                for post in post_data:
                                    selected = post_data[post]
                                    if selected:
                                        request_str = f'{self.api_string}?key={self.api_key}&action=add&service={service["service"]}&link={post}&quantity={quantity}'
                                        response = requests.get(request_str)
                                        output += f'\t{post} : {response.json()}\n'
            self.show_dialogue(output, 'Output')
        except FileNotFoundError:
            self.show_dialogue('No users present', 'Error')

    def show_dialogue(self, message: str, title: str):
        dlg = Ui_Dialog(title, message, self)
        dlg.exec_()

    def show_posts(self, data: str):
        dlg = Ui_posts_ui(self, data)
        dlg.exec()

    def get_button(self):
        button = QtWidgets.QPushButton(self.top_buttons_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addUsers_btn.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy)
        button.setMaximumSize(QtCore.QSize(200, 16777215))
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setToolTip("View Posts")
        button.setAutoFillBackground(False)
        button.setText('Posts')
        button.setStyleSheet("QPushButton { \n"
                             "    background:rgb(160, 132, 202); \n"
                             "    color:white;\n"
                             "    border: 2px solid rgb(164, 136, 207);\n"
                             "      border-radius: 5px;\n"
                             "    height:20px;\n"
                             "    width:50px;\n"
                             " }\n"
                             "QPushButton:hover { \n"
                             "    background:rgb(164, 136, 207);\n"
                             "border: 2px solid rgb(160, 132, 202);\n"
                             "      border-radius: 5px;\n"
                             "}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/visibility.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon7)
        button.setObjectName("button")
        return button

    def add_users(self):
        dlg = Ui_add_users(self)
        if dlg.exec():
            self.load_data()

    def remove_users(self):
        dlg = Ui_rempve_users(self)
        if dlg.exec():
            self.load_data()

    def show_blocked(self):
        dlg = Ui_Dialog(self)
        dlg.exec()
        self.load_data()

    def select_all(self):
        # self.userTabel_tbl.setCol
        for row in range(0, self.userTabel_tbl.rowCount()):
            col = self.userTabel_tbl.item(row, 0)
            col.setCheckState(QtCore.Qt.Checked)

    def unselect_all(self):
        # self.userTabel_tbl.setCol
        for row in range(0, self.userTabel_tbl.rowCount()):
            col = self.userTabel_tbl.item(row, 0)
            col.setCheckState(QtCore.Qt.Unchecked)

    def block_selected(self):
        try:
            previous_data = open('users.json', 'r')
            data = dict(json.load(previous_data))
            for row in range(0, self.userTabel_tbl.rowCount()):
                selected = True if self.userTabel_tbl.item(row, 0).checkState() == 2 else False
                user = self.userTabel_tbl.item(row, 1).text()
                if selected:
                    posts = data[user]['true']
                    data[user] = {False: posts}
            with open('users.json', 'w') as file:
                file.write(json.dumps(data, indent=4))
            self.load_data()
        except FileNotFoundError:
            return

    def get_services(self):
        request_str = f'{self.api_string}?key={self.api_key}&action=services'
        response = requests.get(request_str)
        if response.status_code == 200:
            response_data = response.json()
            self.fb_service_list = []
            for data in response_data:
                if 'Facebook' in data['name']:
                    self.fb_service_list.append(data)
                    self.followers_cmboBox.addItem(data['name'])
            self.followers_cmboBox.setCurrentIndex(0)
        else:
            self.show_dialogue('Server Error', 'Error')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The CM"))
        self.unselect_all_btn.setText(_translate("MainWindow", "Unselect All"))
        self.select_all_btn.setText(_translate("MainWindow", "Select All"))
        self.block_btn.setText(_translate("MainWindow", "Block Selected"))
        self.show_btn.setText(_translate("MainWindow", "Show Blocked"))
        self.title_lbl.setText(_translate("MainWindow", "THE CM - Software"))
        self.copyRight_lbl.setText(_translate("MainWindow", "Copyright@byKJL"))
        self.services_lbl.setText(_translate("MainWindow", "Services"))
        self.followers_cmboBox.setCurrentText(_translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(4, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(5, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(6, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(7, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(8, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(9, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(10, _translate("MainWindow", "New Item"))
        self.followers_cmboBox.setItemText(11, _translate("MainWindow", "New Item"))
        self.addUsers_btn.setText(_translate("MainWindow", "Add User"))
        self.removeUser_btn.setText(_translate("MainWindow", "Remove User"))
        self.quantity_lbl.setText(_translate("MainWindow", "Quantity"))
        self.price_lbl.setText(_translate("MainWindow", "Amount"))
        self.process_request_btn.setText(_translate("MainWindow", "Process Request"))
        self.process_posts_chk_box.setText(_translate("MainWindow", "Process on posts"))
        self.process_user_chk_box.setText(_translate("MainWindow", "Process on user"))
        item = self.userTabel_tbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.userTabel_tbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Link"))
        item = self.userTabel_tbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Post"))
