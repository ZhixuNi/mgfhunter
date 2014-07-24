# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\EricWorkSpace\mgfHunter_ui_ver1.ui'
#
# Created: Thu Jul 24 10:30:07 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from lib.ConfigReader import ConfigParser 
from lib.IONcfg import CFGparser
from mgfHunterCore import Hunter

import os
import codecs
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mgfHunterGUI(object):
    def setupUi(self, mgfHunterGUI):
        mgfHunterGUI.setObjectName(_fromUtf8("mgfHunterGUI"))
        mgfHunterGUI.resize(650, 663)
        self.centralWidget = QtGui.QWidget(mgfHunterGUI)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.TabFrame = QtGui.QTabWidget(self.centralWidget)
        self.TabFrame.setGeometry(QtCore.QRect(10, 30, 631, 561))
        self.TabFrame.setObjectName(_fromUtf8("TabFrame"))
        self.Config_Tab = QtGui.QWidget()
        self.Config_Tab.setObjectName(_fromUtf8("Config_Tab"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.Config_Tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 593, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Threshold_LB = QtGui.QLabel(self.horizontalLayoutWidget)
        self.Threshold_LB.setObjectName(_fromUtf8("Threshold_LB"))
        self.horizontalLayout.addWidget(self.Threshold_LB)
        self.Threshold_txt = QtGui.QTextEdit(self.horizontalLayoutWidget)
        self.Threshold_txt.setMaximumSize(QtCore.QSize(50, 30))
        self.Threshold_txt.setObjectName(_fromUtf8("Threshold_txt"))
        self.horizontalLayout.addWidget(self.Threshold_txt)
        self.line_4 = QtGui.QFrame(self.horizontalLayoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.MS2Low_LB = QtGui.QLabel(self.horizontalLayoutWidget)
        self.MS2Low_LB.setObjectName(_fromUtf8("MS2Low_LB"))
        self.horizontalLayout.addWidget(self.MS2Low_LB)
        self.MS2Low_txt = QtGui.QTextEdit(self.horizontalLayoutWidget)
        self.MS2Low_txt.setMaximumSize(QtCore.QSize(50, 30))
        self.MS2Low_txt.setObjectName(_fromUtf8("MS2Low_txt"))
        self.horizontalLayout.addWidget(self.MS2Low_txt)
        self.MS2High_LB = QtGui.QLabel(self.horizontalLayoutWidget)
        self.MS2High_LB.setObjectName(_fromUtf8("MS2High_LB"))
        self.horizontalLayout.addWidget(self.MS2High_LB)
        self.MS2High_txt = QtGui.QTextEdit(self.horizontalLayoutWidget)
        self.MS2High_txt.setMaximumSize(QtCore.QSize(50, 30))
        self.MS2High_txt.setObjectName(_fromUtf8("MS2High_txt"))
        self.horizontalLayout.addWidget(self.MS2High_txt)
        self.MS2unit_LB = QtGui.QLabel(self.horizontalLayoutWidget)
        self.MS2unit_LB.setObjectName(_fromUtf8("MS2unit_LB"))
        self.horizontalLayout.addWidget(self.MS2unit_LB)
        self.line_3 = QtGui.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.Socre1_LB = QtGui.QLabel(self.horizontalLayoutWidget)
        self.Socre1_LB.setObjectName(_fromUtf8("Socre1_LB"))
        self.horizontalLayout.addWidget(self.Socre1_LB)
        self.Score1_txt = QtGui.QTextEdit(self.horizontalLayoutWidget)
        self.Score1_txt.setMaximumSize(QtCore.QSize(50, 30))
        self.Score1_txt.setObjectName(_fromUtf8("Score1_txt"))
        self.horizontalLayout.addWidget(self.Score1_txt)
        self.Score2_LB = QtGui.QLabel(self.horizontalLayoutWidget)
        self.Score2_LB.setObjectName(_fromUtf8("Score2_LB"))
        self.horizontalLayout.addWidget(self.Score2_LB)
        self.Score2_txt = QtGui.QTextEdit(self.horizontalLayoutWidget)
        self.Score2_txt.setMaximumSize(QtCore.QSize(50, 30))
        self.Score2_txt.setObjectName(_fromUtf8("Score2_txt"))
        self.horizontalLayout.addWidget(self.Score2_txt)
        self.ConName_PB = QtGui.QPushButton(self.Config_Tab)
        self.ConName_PB.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.ConName_PB.setObjectName(_fromUtf8("ConName_PB"))
        self.ConName_txt = QtGui.QTextEdit(self.Config_Tab)
        self.ConName_txt.setGeometry(QtCore.QRect(100, 10, 491, 31))
        self.ConName_txt.setObjectName(_fromUtf8("ConName_txt"))
        self.ConSave_PB = QtGui.QPushButton(self.Config_Tab)
        self.ConSave_PB.setGeometry(QtCore.QRect(350, 90, 75, 23))
        self.ConSave_PB.setObjectName(_fromUtf8("ConSave_PB"))
        self.ConSaveAs_PB = QtGui.QPushButton(self.Config_Tab)
        self.ConSaveAs_PB.setGeometry(QtCore.QRect(430, 90, 75, 23))
        self.ConSaveAs_PB.setObjectName(_fromUtf8("ConSaveAs_PB"))
        self.Con_profile_List_txt = QtGui.QTextEdit(self.Config_Tab)
        self.Con_profile_List_txt.setGeometry(QtCore.QRect(100, 50, 491, 31))
        self.Con_profile_List_txt.setObjectName(_fromUtf8("Con_profile_List_txt"))
        self.ConUse_PB_txt = QtGui.QTextEdit(self.Config_Tab)
        self.ConUse_PB_txt.setGeometry(QtCore.QRect(100, 90, 241, 31))
        self.ConUse_PB_txt.setObjectName(_fromUtf8("ConUse_PB_txt"))
        self.Con_profile_List_LB = QtGui.QLabel(self.Config_Tab)
        self.Con_profile_List_LB.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.Con_profile_List_LB.setObjectName(_fromUtf8("Con_profile_List_LB"))
        self.ConUse_PB = QtGui.QPushButton(self.Config_Tab)
        self.ConUse_PB.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.ConUse_PB.setObjectName(_fromUtf8("ConUse_PB"))
        self.ConDelete_PB = QtGui.QPushButton(self.Config_Tab)
        self.ConDelete_PB.setGeometry(QtCore.QRect(520, 90, 75, 23))
        self.ConDelete_PB.setObjectName(_fromUtf8("ConDelete_PB"))
        self.inSetFile_PB = QtGui.QPushButton(self.Config_Tab)
        self.inSetFile_PB.setGeometry(QtCore.QRect(10, 220, 141, 23))
        self.inSetFile_PB.setObjectName(_fromUtf8("inSetFile_PB"))
        self.inSetFile_txt = QtGui.QTextEdit(self.Config_Tab)
        self.inSetFile_txt.setGeometry(QtCore.QRect(170, 220, 421, 31))
        self.inSetFile_txt.setObjectName(_fromUtf8("inSetFile_txt"))
        self.ShowTypeList_LB = QtGui.QLabel(self.Config_Tab)
        self.ShowTypeList_LB.setGeometry(QtCore.QRect(10, 270, 141, 16))
        self.ShowTypeList_LB.setObjectName(_fromUtf8("ShowTypeList_LB"))
        self.ShowTypeList_txt = QtGui.QTextEdit(self.Config_Tab)
        self.ShowTypeList_txt.setGeometry(QtCore.QRect(170, 260, 421, 31))
        self.ShowTypeList_txt.setObjectName(_fromUtf8("ShowTypeList_txt"))
        self.ShowFullSettings__LB = QtGui.QLabel(self.Config_Tab)
        self.ShowFullSettings__LB.setGeometry(QtCore.QRect(250, 300, 101, 16))
        self.ShowFullSettings__LB.setObjectName(_fromUtf8("ShowFullSettings__LB"))
        self.ShowFullSettings_txt = QtGui.QTextEdit(self.Config_Tab)
        self.ShowFullSettings_txt.setGeometry(QtCore.QRect(10, 320, 581, 211))
        self.ShowFullSettings_txt.setObjectName(_fromUtf8("ShowFullSettings_txt"))
        self.setintro_LB = QtGui.QLabel(self.Config_Tab)
        self.setintro_LB.setGeometry(QtCore.QRect(10, 200, 271, 16))
        self.setintro_LB.setObjectName(_fromUtf8("setintro_LB"))
        self.line = QtGui.QFrame(self.Config_Tab)
        self.line.setGeometry(QtCore.QRect(10, 180, 581, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.TabFrame.addTab(self.Config_Tab, _fromUtf8(""))
        self.mgfHunter_Tab = QtGui.QWidget()
        self.mgfHunter_Tab.setObjectName(_fromUtf8("mgfHunter_Tab"))
        self.formLayoutWidget_5 = QtGui.QWidget(self.mgfHunter_Tab)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(10, 50, 601, 231))
        self.formLayoutWidget_5.setObjectName(_fromUtf8("formLayoutWidget_5"))
        self.formLayout_5 = QtGui.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        #self.formLayout_5.setMargin(0)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.Filter1_LB = QtGui.QLabel(self.formLayoutWidget_5)
        self.Filter1_LB.setObjectName(_fromUtf8("Filter1_LB"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.Filter1_LB)
        self.Filter_in_PB = QtGui.QPushButton(self.formLayoutWidget_5)
        self.Filter_in_PB.setObjectName(_fromUtf8("Filter_in_PB"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.Filter_in_PB)
        self.Filter_in_txt = QtGui.QTextEdit(self.formLayoutWidget_5)
        self.Filter_in_txt.setMaximumSize(QtCore.QSize(450, 50))
        self.Filter_in_txt.setObjectName(_fromUtf8("Filter_in_txt"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.Filter_in_txt)
        self.Filter2_LB = QtGui.QLabel(self.formLayoutWidget_5)
        self.Filter2_LB.setObjectName(_fromUtf8("Filter2_LB"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.Filter2_LB)
        self.Filter_out_PB = QtGui.QPushButton(self.formLayoutWidget_5)
        self.Filter_out_PB.setObjectName(_fromUtf8("Filter_out_PB"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.Filter_out_PB)
        self.Filter_out_txt = QtGui.QTextEdit(self.formLayoutWidget_5)
        self.Filter_out_txt.setMaximumSize(QtCore.QSize(450, 50))
        self.Filter_out_txt.setObjectName(_fromUtf8("Filter_out_txt"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.Filter_out_txt)
        self.Filter3_LB = QtGui.QLabel(self.formLayoutWidget_5)
        self.Filter3_LB.setObjectName(_fromUtf8("Filter3_LB"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.Filter3_LB)
        self.Filter_run_PB = QtGui.QPushButton(self.formLayoutWidget_5)
        self.Filter_run_PB.setObjectName(_fromUtf8("Filter_run_PB"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.LabelRole, self.Filter_run_PB)
        self.Filter_run_txt = QtGui.QTextEdit(self.formLayoutWidget_5)
        self.Filter_run_txt.setMaximumSize(QtCore.QSize(450, 50))
        self.Filter_run_txt.setObjectName(_fromUtf8("Filter_run_txt"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.FieldRole, self.Filter_run_txt)
        self.line_2 = QtGui.QFrame(self.mgfHunter_Tab)
        self.line_2.setGeometry(QtCore.QRect(10, 290, 601, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.formLayoutWidget_6 = QtGui.QWidget(self.mgfHunter_Tab)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(10, 350, 601, 171))
        self.formLayoutWidget_6.setObjectName(_fromUtf8("formLayoutWidget_6"))
        self.formLayout_6 = QtGui.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        #self.formLayout_6.setMargin(0)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.extractor1_LB = QtGui.QLabel(self.formLayoutWidget_6)
        self.extractor1_LB.setObjectName(_fromUtf8("extractor1_LB"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.extractor1_LB)
        self.extractor_in_PB = QtGui.QPushButton(self.formLayoutWidget_6)
        self.extractor_in_PB.setObjectName(_fromUtf8("extractor_in_PB"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.extractor_in_PB)
        self.extractor_in_txt = QtGui.QTextEdit(self.formLayoutWidget_6)
        self.extractor_in_txt.setMaximumSize(QtCore.QSize(450, 30))
        self.extractor_in_txt.setObjectName(_fromUtf8("extractor_in_txt"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.extractor_in_txt)
        self.extractor2_LB = QtGui.QLabel(self.formLayoutWidget_6)
        self.extractor2_LB.setObjectName(_fromUtf8("extractor2_LB"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.extractor2_LB)
        self.extractor_out_PB = QtGui.QPushButton(self.formLayoutWidget_6)
        self.extractor_out_PB.setObjectName(_fromUtf8("extractor_out_PB"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.LabelRole, self.extractor_out_PB)
        self.extractor_out_txt = QtGui.QTextEdit(self.formLayoutWidget_6)
        self.extractor_out_txt.setMaximumSize(QtCore.QSize(450, 30))
        self.extractor_out_txt.setObjectName(_fromUtf8("extractor_out_txt"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.FieldRole, self.extractor_out_txt)
        self.extractor3_LB = QtGui.QLabel(self.formLayoutWidget_6)
        self.extractor3_LB.setObjectName(_fromUtf8("extractor3_LB"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.FieldRole, self.extractor3_LB)
        self.extractor_run_PB = QtGui.QPushButton(self.formLayoutWidget_6)
        self.extractor_run_PB.setObjectName(_fromUtf8("extractor_run_PB"))
        self.formLayout_6.setWidget(5, QtGui.QFormLayout.LabelRole, self.extractor_run_PB)
        self.extractor_run_txt = QtGui.QTextEdit(self.formLayoutWidget_6)
        self.extractor_run_txt.setMaximumSize(QtCore.QSize(450, 30))
        self.extractor_run_txt.setObjectName(_fromUtf8("extractor_run_txt"))
        self.formLayout_6.setWidget(5, QtGui.QFormLayout.FieldRole, self.extractor_run_txt)
        self.hunterBanner_LB = QtGui.QLabel(self.mgfHunter_Tab)
        self.hunterBanner_LB.setGeometry(QtCore.QRect(180, 10, 261, 31))
        self.hunterBanner_LB.setObjectName(_fromUtf8("hunterBanner_LB"))
        self.extractor0_LB = QtGui.QLabel(self.mgfHunter_Tab)
        self.extractor0_LB.setGeometry(QtCore.QRect(180, 320, 241, 16))
        self.extractor0_LB.setObjectName(_fromUtf8("extractor0_LB"))
        self.TabFrame.addTab(self.mgfHunter_Tab, _fromUtf8(""))
        self.Calc_Tab = QtGui.QWidget()
        self.Calc_Tab.setObjectName(_fromUtf8("Calc_Tab"))
        self.TabFrame.addTab(self.Calc_Tab, _fromUtf8(""))
        self.exitRun = QtGui.QPushButton(self.centralWidget)
        self.exitRun.setGeometry(QtCore.QRect(970, 600, 75, 23))
        self.exitRun.setObjectName(_fromUtf8("exitRun"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 610, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.Exit_PB = QtGui.QPushButton(self.centralWidget)
        self.Exit_PB.setGeometry(QtCore.QRect(550, 610, 75, 23))
        self.Exit_PB.setObjectName(_fromUtf8("Exit_PB"))
        #mgfHunterGUI.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(mgfHunterGUI)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuSettings = QtGui.QMenu(self.menuBar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        #mgfHunterGUI.setMenuBar(self.menuBar)
        self.actionAbout_LPPbox = QtGui.QAction(mgfHunterGUI)
        self.actionAbout_LPPbox.setObjectName(_fromUtf8("actionAbout_LPPbox"))
        self.actionAbout_LPPbox_2 = QtGui.QAction(mgfHunterGUI)
        self.actionAbout_LPPbox_2.setObjectName(_fromUtf8("actionAbout_LPPbox_2"))
        self.actionBoxHelp = QtGui.QAction(mgfHunterGUI)
        self.actionBoxHelp.setObjectName(_fromUtf8("actionBoxHelp"))
        self.actionDefault_folders = QtGui.QAction(mgfHunterGUI)
        self.actionDefault_folders.setObjectName(_fromUtf8("actionDefault_folders"))
        self.menuHelp.addAction(self.actionAbout_LPPbox_2)
        self.menuHelp.addAction(self.actionBoxHelp)
        self.menuSettings.addAction(self.actionDefault_folders)
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        # ###default config#
        HunterPATH = os.getcwd()
        cfgPATH = HunterPATH + r'\config.txt'
        print (cfgPATH)
        self.ConName_txt.setText(cfgPATH)
        ConfigName = self.ConName_txt.toPlainText()
        config = ConfigParser()
        config.read(ConfigName)
        
        Con_profile_List = config.sections()
        self.Con_profile_List_txt.setText(str(Con_profile_List))
        self.ConUse_PB_txt.setText('Default_Settings')
        
        SECTION = self.ConUse_PB_txt.toPlainText()
        
        infoThreshold = config.get(SECTION,'THMS2')
        self.Threshold_txt.setText(infoThreshold)
        
        infoMS2Low = config.get(SECTION,'MS2TLLow')
        self.MS2Low_txt.setText(infoMS2Low)
        
        infoMS2High = config.get(SECTION,'MS2TLHigh')
        self.MS2High_txt.setText(infoMS2High)
        
        infoScore1 = config.get(SECTION,'score1')
        self.Score1_txt.setText(infoScore1)

       
        infoScore2 = config.get(SECTION,'score2')
        self.Score2_txt.setText(infoScore2)

        
        # ###default config end# 
        
        
        # # set default tab #
        self.retranslateUi(mgfHunterGUI)
        self.TabFrame.setCurrentIndex(1)
        
        # # Connect push buttons to corresponding functions#
        # # #QT connectors bookmark1#
        QtCore.QObject.connect(self.Exit_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), mgfHunterGUI.close)
        QtCore.QMetaObject.connectSlotsByName(mgfHunterGUI)
        
        # #----------------Merge Config Tab trigger------------------#
        QtCore.QObject.connect(self.ConName_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.conFile)        
        QtCore.QObject.connect(self.ConUse_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.conUseSec)        
        QtCore.QObject.connect(self.ConSave_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.conChangeSec)        
        QtCore.QObject.connect(self.ConSaveAs_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.conAddSec)        
        QtCore.QObject.connect(self.ConDelete_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.conRemoveSec)
        # #----------------Merge Config Tab trigger-END-----------------# 
        
        # #----------------Merge NL-settings Tab trigger------------------#
        QtCore.QObject.connect(self.inSetFile_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SetIONinfo)        
        # #----------------Merge NL-settings Tab trigger-END-----------------# 
        
        # #----------------Merge Core Tab trigger------------------#
        QtCore.QObject.connect(self.Filter_in_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.inFile)
        QtCore.QObject.connect(self.Filter_out_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.outFile)
        QtCore.QObject.connect(self.Filter_run_PB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.StartRun)
        # #----------------Merge Core Tab trigger-END-----------------#

    def retranslateUi(self, mgfHunterGUI):
        mgfHunterGUI.setWindowTitle(_translate("mgfHunterGUI", "mgfHunter_alpha", None))
        self.Threshold_LB.setText(_translate("mgfHunterGUI", "Threshold(%): ", None))
        self.MS2Low_LB.setText(_translate("mgfHunterGUI", "MS2 tolerance:  -", None))
        self.MS2High_LB.setText(_translate("mgfHunterGUI", "Da  to +", None))
        self.MS2unit_LB.setText(_translate("mgfHunterGUI", "Da", None))
        self.Socre1_LB.setText(_translate("mgfHunterGUI", "Score", None))
        self.Score2_LB.setText(_translate("mgfHunterGUI", "to", None))
        self.ConName_PB.setText(_translate("mgfHunterGUI", "Config File", None))
        self.ConSave_PB.setText(_translate("mgfHunterGUI", "Save", None))
        self.ConSaveAs_PB.setText(_translate("mgfHunterGUI", "Save As..", None))
        self.Con_profile_List_LB.setText(_translate("mgfHunterGUI", "Saved Profile list", None))
        self.ConUse_PB.setText(_translate("mgfHunterGUI", "Use Profile", None))
        self.ConDelete_PB.setText(_translate("mgfHunterGUI", "Delete", None))
        self.inSetFile_PB.setText(_translate("mgfHunterGUI", "Open Frag/NL Settings .csv", None))
        self.ShowTypeList_LB.setText(_translate("mgfHunterGUI", "Names to be searched:", None))
        self.ShowFullSettings__LB.setText(_translate("mgfHunterGUI", "Detailed settings:", None))
        self.setintro_LB.setText(_translate("mgfHunterGUI", "Specify fragment ion / neutral loss settings below:", None))
        self.TabFrame.setTabText(self.TabFrame.indexOf(self.Config_Tab), _translate("mgfHunterGUI", "Settings", None))
        self.Filter1_LB.setText(_translate("mgfHunterGUI", "1. select the .mgf file", None))
        self.Filter_in_PB.setText(_translate("mgfHunterGUI", "Open input.mgf", None))
        self.Filter2_LB.setText(_translate("mgfHunterGUI", "2. Choose where to save the output.mgf", None))
        self.Filter_out_PB.setText(_translate("mgfHunterGUI", "Save output as", None))
        self.Filter3_LB.setText(_translate("mgfHunterGUI", "3. Click RUN to process.", None))
        self.Filter_run_PB.setText(_translate("mgfHunterGUI", "RUN-->mgfHunter!", None))
        self.extractor1_LB.setText(_translate("mgfHunterGUI", "1. select the .mgf file", None))
        self.extractor_in_PB.setText(_translate("mgfHunterGUI", "Open input.mgf", None))
        self.extractor2_LB.setText(_translate("mgfHunterGUI", "2. Choose where to save the output.mgf", None))
        self.extractor_out_PB.setText(_translate("mgfHunterGUI", "Save .csv as", None))
        self.extractor3_LB.setText(_translate("mgfHunterGUI", "3. Click RUN to process.", None))
        self.extractor_run_PB.setText(_translate("mgfHunterGUI", "RUN-->scan info  list", None))
        self.hunterBanner_LB.setText(_translate("mgfHunterGUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">The main filter function</span></p></body></html>", None))
        self.extractor0_LB.setText(_translate("mgfHunterGUI", "Extract scan info from .mgf file to a .csv table", None))
        self.TabFrame.setTabText(self.TabFrame.indexOf(self.mgfHunter_Tab), _translate("mgfHunterGUI", "mgf Hunter core", None))
        self.TabFrame.setTabText(self.TabFrame.indexOf(self.Calc_Tab), _translate("mgfHunterGUI", "Tools", None))
        self.exitRun.setText(_translate("mgfHunterGUI", "Exit", None))
        self.label.setText(_translate("mgfHunterGUI", "(C) BBZ @ University of Leipzig", None))
        self.Exit_PB.setText(_translate("mgfHunterGUI", "Exit", None))
        self.menuHelp.setTitle(_translate("mgfHunterGUI", "Help", None))
        self.menuSettings.setTitle(_translate("mgfHunterGUI", "Settings", None))
        self.actionAbout_LPPbox.setText(_translate("mgfHunterGUI", "About LPPbox", None))
        self.actionAbout_LPPbox_2.setText(_translate("mgfHunterGUI", "About LPPbox", None))
        self.actionBoxHelp.setText(_translate("mgfHunterGUI", "BoxHelp", None))
        self.actionDefault_folders.setText(_translate("mgfHunterGUI", "Default folders", None))


####------------------------------------------------------------------------------------------------#
    def conFile(self):
        
        
        conPath=QtGui.QFileDialog.getOpenFileName(None,"open file dialog","/","CSV(*.txt)")
        self.ConName_txt.setText(conPath[0])
        
        ConfigName = self.ConName_txt.toPlainText()
        config = ConfigParser()
        config.read(ConfigName)
        
        config = ConfigParser()
        config.read(ConfigName)
        
        Con_profile_List = config.sections()
        self.Con_profile_List_txt.setText(str(Con_profile_List))
        self.ConUse_PB_txt.setText('Default_Settings')
        
        SECTION = self.ConUse_PB_txt.toPlainText()
        
        infoThreshold = config.get(SECTION,'THMS2')
        self.Threshold_txt.setText(infoThreshold)
        
        infoMS2Low = config.get(SECTION,'MS2TLLow')
        self.MS2Low_txt.setText(infoMS2Low)
        
        infoMS2High = config.get(SECTION,'MS2TLHigh')
        self.MS2High_txt.setText(infoMS2High)
        
        infoScore1 = config.get(SECTION,'score1')
        self.Score1_txt.setText(infoScore1)

       
        infoScore2 = config.get(SECTION,'score2')
        self.Score2_txt.setText(infoScore2)
        
        
        
        
    def conUseSec(self):
        
        ConfigName = self.ConName_txt.toPlainText()
        config = ConfigParser()
        config.read(ConfigName)
        
        rawSECTION = self.ConUse_PB_txt.toPlainText()

        prSECTION = rawSECTION.strip('u,[]\'')
        SecList = config.sections()
        
        if prSECTION in SecList:
            SECTION = prSECTION
            self.ConUse_PB_txt.setText(SECTION)
        else:
            NoSec = "Can not find:"+rawSECTION+"-->Use Default_Settings"
            self.ConUse_PB_txt.setText(NoSec)
            SECTION = "Default_Settings"
            
        SECTION = self.ConUse_PB_txt.toPlainText()
        
        infoThreshold = config.get(SECTION,'THMS2')
        self.Threshold_txt.setText(infoThreshold)
        
        infoMS2Low = config.get(SECTION,'MS2TLLow')
        self.MS2Low_txt.setText(infoMS2Low)
        
        infoMS2High = config.get(SECTION,'MS2TLHigh')
        self.MS2High_txt.setText(infoMS2High)
        
        infoScore1 = config.get(SECTION,'score1')
        self.Score1_txt.setText(infoScore1)

       
        infoScore2 = config.get(SECTION,'score2')
        self.Score2_txt.setText(infoScore2)
        
    def conChangeSec(self):
        # # Save New settings as a profile in the Config file#
        ConfigName = self.ConName_txt.toPlainText()
        config = ConfigParser()
        config.read(ConfigName)
        
        rawSECTION = self.ConUse_PB_txt.toPlainText()

        prSECTION = rawSECTION.strip('u,[]\'')
        SecList = config.sections()
        
        rawTHMS2 = self.Threshold_txt.toPlainText()
        rawMS2TLLow = self.MS2Low_txt.toPlainText()
        rawMS2TLHigh = self.MS2High_txt.toPlainText()
        rawScore1 = self.Score1_txt.toPlainText()
        rawScore2 = self.Score2_txt.toPlainText()

        
        prTHMS2 = rawTHMS2.strip('\'')
        prMS2TLLow = rawMS2TLLow.strip('\'')
        prMS2TLHigh = rawMS2TLHigh.strip('\'')
        prScore1 = rawScore1.strip('\'')
        prScore2 = rawScore2.strip('\'')

        
        
        # # if the profile name is already there# 
        if prSECTION in SecList:
            
            config.set(prSECTION, 'thms2', prTHMS2) 
            config.set(prSECTION, 'MS2TLLow', prMS2TLLow) 
            config.set(prSECTION, 'MS2TLHigh', prMS2TLHigh) 
            config.set(prSECTION, 'score1', prScore1) 
            config.set(prSECTION, 'score2', prScore2) 

            
            #write back to configure file
            config.write(open(ConfigName, "w+")) 

            #SecList.append(ProfileName)
            nSecList = config.sections()
            self.Con_profile_List_txt.setText(str(nSecList))
            conInSec = "Profile:"+rawSECTION+"-->in the list has changed"
            self.ConUse_PB_txt.setText(conInSec)
        
        # # if the profile name is Not there, save the profile# 
        else:

            config.add_section(str(prSECTION)) 
            
            config.set(prSECTION, 'thms2', prTHMS2) 
            config.set(prSECTION, 'MS2TLLow', prMS2TLLow) 
            config.set(prSECTION, 'MS2TLHigh', prMS2TLHigh) 
            config.set(prSECTION, 'score1', prScore1) 
            config.set(prSECTION, 'score2', prScore2) 
            
            #write back to configure file
            config.write(open(ConfigName, "w+")) 

            conInSec = "Profile:"+prSECTION+"-->Saved in the list"
            self.ConUse_PB_txt.setText(conInSec)
            #SecList.append(ProfileName)
            nSecList = config.sections()
            print(nSecList)
            self.Con_profile_List_txt.setText(str(nSecList))
        
    def conAddSec(self):
        # # Save New settings as a profile in the Config file#
        ConfigName = self.ConName_txt.toPlainText()
        config = ConfigParser()
        config.read(ConfigName)
        
        rawSECTION = self.ConUse_PB_txt.toPlainText()

        prSECTION = rawSECTION.strip('u,[]\'')
        SecList = config.sections()
        
        rawTHMS2 = self.Threshold_txt.toPlainText()
        rawMS2TLLow = self.MS2Low_txt.toPlainText()
        rawMS2TLHigh = self.MS2High_txt.toPlainText()
        rawScore1 = self.Score1_txt.toPlainText()
        rawScore2 = self.Score2_txt.toPlainText()

        
        prTHMS2 = rawTHMS2.strip('\'')
        prMS2TLLow = rawMS2TLLow.strip('\'')
        prMS2TLHigh = rawMS2TLHigh.strip('\'')
        prScore1 = rawScore1.strip('\'')
        prScore2 = rawScore2.strip('\'')
        
        
        # # if the profile name is already there# 
        if prSECTION in SecList:
            conInSec = "Profile:"+rawSECTION+"-->already in the list-->Not saved"
            self.ConUse_PB_txt.setText(conInSec)
        
        # # if the profile name is Not there, save the profile# 
        else:

            config.add_section(str(prSECTION)) 
            
            config.set(prSECTION, 'thms2', prTHMS2) 
            config.set(prSECTION, 'MS2TLLow', prMS2TLLow) 
            config.set(prSECTION, 'MS2TLHigh', prMS2TLHigh) 
            config.set(prSECTION, 'score1', prScore1) 
            config.set(prSECTION, 'score2', prScore2)
            
            #write back to configure file
            config.write(open(ConfigName, "w+")) 

            conInSec = "Profile:"+prSECTION+"-->Saved in the list"
            self.ConUse_PB_txt.setText(conInSec)
            nSecList = config.sections()
            self.Con_profile_List_txt.setText(str(nSecList))
            
            
    def conRemoveSec(self):
        # # Save New settings as a profile in the Config file#
        ConfigName = self.ConName_txt.toPlainText()
        config = ConfigParser()
        config.read(ConfigName)
        
        rawSECTION = self.ConUse_PB_txt.toPlainText()

        prSECTION = rawSECTION.strip('u,[]\'')
        SecList = config.sections()
        
        
        # # if the profile name is already there# 
        if prSECTION in SecList:

            
            config.remove_section(prSECTION) 
            #write back to configure file
            config.write(open(ConfigName, "w+")) 
            #get new section list#
            nSecList = config.sections()
            self.Con_profile_List_txt.setText(str(nSecList))
            SECTION = "Default_Settings"
            
            infoThreshold = config.get(SECTION,'THMS2')
            self.Threshold_txt.setText(infoThreshold)
            
            infoMS2Low = config.get(SECTION,'MS2TLLow')
            self.MS2Low_txt.setText(infoMS2Low)
            
            infoMS2High = config.get(SECTION,'MS2TLHigh')
            self.MS2High_txt.setText(infoMS2High)
            
            infoScore1 = config.get(SECTION,'score1')
            self.Score1_txt.setText(infoScore1)
    
        
            infoScore2 = config.get(SECTION,'score2')
            self.Score2_txt.setText(infoScore2)
            
            ReSec = "Profile:"+rawSECTION+" ->deleted-->Use Default_Settings"
            self.ConUse_PB_txt.setText(ReSec)
            
        
        # # if the profile name is Not there, save the profile# 
        else:

            SECTION = "Default_Settings"
                
            infoThreshold = config.get(SECTION,'THMS2')
            self.Threshold_txt.setText(infoThreshold)
            
            infoMS2Low = config.get(SECTION,'MS2TLLow')
            self.MS2Low_txt.setText(infoMS2Low)
            
            infoMS2High = config.get(SECTION,'MS2TLHigh')
            self.MS2High_txt.setText(infoMS2High)
            
            infoScore1 = config.get(SECTION,'score1')
            self.Score1_txt.setText(infoScore1)
    
        
            infoScore2 = config.get(SECTION,'score2')
            self.Score2_txt.setText(infoScore2)
            
            nSecList = config.sections()
            self.Con_profile_List_txt.setText(str(nSecList))
            ReSec = "Profile:"+rawSECTION+"NOT correct-->Use Default_Settings"
            self.ConUse_PB_txt.setText(ReSec)
            
        
    def SetIONinfo(self):
        ionCFGsetPath=QtGui.QFileDialog.getOpenFileName(None,"open file dialog","/","CSV(*.csv)")
        self.inSetFile_txt.setText(ionCFGsetPath[0])   
        cfgNAME = self.inSetFile_txt.toPlainText()
        
        IONcfg = CFGparser(cfgNAME)
        ionNames = IONcfg.GFGionNAME()
        ionNameINFO = ';  '.join(ionNames)
        
        self.ShowTypeList_txt.setText(ionNameINFO)
        ShowION = codecs.open(cfgNAME,'r','cp936').read()
        self.ShowFullSettings_txt.setText(ShowION)
        
        #print (sumFrame)
        
    
    # # book mark 2 main functions # #
    
    def inFile(self):
        inPath=QtGui.QFileDialog.getOpenFileName(None,"Open file dialog","/","mgf(*.mgf)")     
        self.Filter_in_txt.setText(inPath[0])

    
    def outFile(self):
        outPath=QtGui.QFileDialog.getSaveFileName(None,"Save file dialog","/","mgf(*.mgf)")
        self.Filter_out_txt.setText(outPath[0])
    
    def StartRun(self):
        
        StartTime = time.clock()
      
        
        inmgf = self.Filter_in_txt.toPlainText()
        outmgf = self.Filter_out_txt.toPlainText()
        INcfgNAME = self.ConName_txt.toPlainText()
        INcfgSection = self.ConUse_PB_txt.toPlainText()
        INionCSVname = self.inSetFile_txt.toPlainText()
        
        print 'INcfgNAME',INcfgNAME
        print 'INcfgSection',INcfgSection
        print 'INionCSVname',INionCSVname
                
        Hunter(inmgf,outmgf,cfgNAME=INcfgNAME,cfgSection = INcfgSection,ionCSVname = INionCSVname)
        
        Finishedinfo = 'Finifhed ! time:' + str(time.clock() - StartTime)
        
        self.Filter_run_txt.setText(Finishedinfo)
        print (Finishedinfo) 

####------------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance()
    if app == None:
        app = QtGui.QApplication(sys.argv)
    LX_ToolBox = QtGui.QDialog()
    ui = Ui_mgfHunterGUI()
    ui.setupUi(LX_ToolBox)
    LX_ToolBox.show()
    #sys.exit(app.exec_())
    sys.exit()
#-----------------------------------------------End script-----------------------------------#


