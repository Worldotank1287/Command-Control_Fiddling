
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './python/ui/agent_command_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommandDialogue(object):
    def setupUi(self, CommandDialogue):
        CommandDialogue.setObjectName("CommandDialogue")
        CommandDialogue.resize(400, 173)
        self.buttonBox = QtWidgets.QDialogButtonBox(CommandDialogue)
        self.buttonBox.setGeometry(QtCore.QRect(-70, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Title = QtWidgets.QLabel(CommandDialogue)
        self.Title.setGeometry(QtCore.QRect(10, 10, 131, 19))
        self.Title.setObjectName("Title")
        self.Info = QtWidgets.QLabel(CommandDialogue)
        self.Info.setGeometry(QtCore.QRect(20, 50, 221, 19))
        self.Info.setObjectName("Info")
        self.Input = QtWidgets.QLineEdit(CommandDialogue)
        self.Input.setGeometry(QtCore.QRect(20, 80, 351, 25))
        self.Input.setObjectName("Input")

        self.retranslateUi(CommandDialogue)
        self.buttonBox.accepted.connect(CommandDialogue.accept)
        self.buttonBox.rejected.connect(CommandDialogue.reject)
        QtCore.QMetaObject.connectSlotsByName(CommandDialogue)

    def retranslateUi(self, CommandDialogue):
        _translate = QtCore.QCoreApplication.translate
        CommandDialogue.setWindowTitle(_translate("CommandDialogue", "Dialog"))
        self.Title.setText(_translate("CommandDialogue", "Command Dialogue"))
        self.Info.setText(_translate("CommandDialogue", "Enter Command to Send to Agent"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './python/ui/agent_compile_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AgentCompile(object):
    def setupUi(self, AgentCompile):
        AgentCompile.setObjectName("AgentCompile")
        AgentCompile.resize(357, 227)
        self.buttonBox = QtWidgets.QDialogButtonBox(AgentCompile)
        self.buttonBox.setGeometry(QtCore.QRect(-10, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Title = QtWidgets.QLabel(AgentCompile)
        self.Title.setGeometry(QtCore.QRect(10, 10, 191, 19))
        self.Title.setObjectName("Title")
        self.ServerIP = QtWidgets.QLineEdit(AgentCompile)
        self.ServerIP.setGeometry(QtCore.QRect(20, 80, 181, 25))
        self.ServerIP.setObjectName("ServerIP")
        self.ServerPort = QtWidgets.QLineEdit(AgentCompile)
        self.ServerPort.setGeometry(QtCore.QRect(20, 140, 101, 25))
        self.ServerPort.setObjectName("ServerPort")
        self.IPLable = QtWidgets.QLabel(AgentCompile)
        self.IPLable.setGeometry(QtCore.QRect(20, 50, 61, 19))
        self.IPLable.setObjectName("IPLable")
        self.PortLabel = QtWidgets.QLabel(AgentCompile)
        self.PortLabel.setGeometry(QtCore.QRect(20, 110, 61, 19))
        self.PortLabel.setObjectName("PortLabel")

        self.retranslateUi(AgentCompile)
        self.buttonBox.accepted.connect(AgentCompile.accept)
        self.buttonBox.rejected.connect(AgentCompile.reject)
        QtCore.QMetaObject.connectSlotsByName(AgentCompile)

    def retranslateUi(self, AgentCompile):
        _translate = QtCore.QCoreApplication.translate
        AgentCompile.setWindowTitle(_translate("AgentCompile", "Dialog"))
        self.Title.setText(_translate("AgentCompile", "Agent Compilation Options"))
        self.IPLable.setText(_translate("AgentCompile", "Server IP"))
        self.PortLabel.setText(_translate("AgentCompile", "Port"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './python/ui/agent_download_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AgentDownload(object):
    def setupUi(self, AgentDownload):
        AgentDownload.setObjectName("AgentDownload")
        AgentDownload.resize(344, 171)
        self.buttonBox = QtWidgets.QDialogButtonBox(AgentDownload)
        self.buttonBox.setGeometry(QtCore.QRect(-90, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Path = QtWidgets.QLineEdit(AgentDownload)
        self.Path.setGeometry(QtCore.QRect(30, 80, 271, 25))
        self.Path.setObjectName("Path")
        self.Title = QtWidgets.QLabel(AgentDownload)
        self.Title.setGeometry(QtCore.QRect(10, 20, 201, 19))
        self.Title.setObjectName("Title")
        self.AgentPathLabel = QtWidgets.QLabel(AgentDownload)
        self.AgentPathLabel.setGeometry(QtCore.QRect(30, 50, 131, 19))
        self.AgentPathLabel.setObjectName("AgentPathLabel")

        self.retranslateUi(AgentDownload)
        self.buttonBox.accepted.connect(AgentDownload.accept)
        self.buttonBox.rejected.connect(AgentDownload.reject)
        QtCore.QMetaObject.connectSlotsByName(AgentDownload)

    def retranslateUi(self, AgentDownload):
        _translate = QtCore.QCoreApplication.translate
        AgentDownload.setWindowTitle(_translate("AgentDownload", "Dialog"))
        self.Title.setText(_translate("AgentDownload", "Agent File Download Dialogue"))
        self.AgentPathLabel.setText(_translate("AgentDownload", "Path to File (Agent)"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './python/ui/agent_registration_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AgentRegister(object):
    def setupUi(self, AgentRegister):
        AgentRegister.setObjectName("AgentRegister")
        AgentRegister.resize(198, 191)
        self.buttonBox = QtWidgets.QDialogButtonBox(AgentRegister)
        self.buttonBox.setGeometry(QtCore.QRect(-160, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Title = QtWidgets.QLabel(AgentRegister)
        self.Title.setGeometry(QtCore.QRect(10, 10, 181, 19))
        self.Title.setObjectName("Title")
        self.Username = QtWidgets.QLineEdit(AgentRegister)
        self.Username.setGeometry(QtCore.QRect(20, 60, 161, 25))
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(AgentRegister)
        self.Password.setGeometry(QtCore.QRect(20, 120, 161, 25))
        self.Password.setObjectName("Password")
        self.UsernameLabel = QtWidgets.QLabel(AgentRegister)
        self.UsernameLabel.setGeometry(QtCore.QRect(20, 40, 181, 19))
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.PasswordLabel = QtWidgets.QLabel(AgentRegister)
        self.PasswordLabel.setGeometry(QtCore.QRect(20, 100, 181, 19))
        self.PasswordLabel.setObjectName("PasswordLabel")

        self.retranslateUi(AgentRegister)
        self.buttonBox.accepted.connect(AgentRegister.accept)
        self.buttonBox.rejected.connect(AgentRegister.reject)
        QtCore.QMetaObject.connectSlotsByName(AgentRegister)

    def retranslateUi(self, AgentRegister):
        _translate = QtCore.QCoreApplication.translate
        AgentRegister.setWindowTitle(_translate("AgentRegister", "Dialog"))
        self.Title.setText(_translate("AgentRegister", "Agent Registration Options"))
        self.UsernameLabel.setText(_translate("AgentRegister", "Username"))
        self.PasswordLabel.setText(_translate("AgentRegister", "Password"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './python/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AgentSelect = QtWidgets.QScrollArea(self.centralwidget)
        self.AgentSelect.setGeometry(QtCore.QRect(0, 0, 331, 551))
        self.AgentSelect.setWidgetResizable(True)
        self.AgentSelect.setObjectName("AgentSelect")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 327, 547))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.AgentList = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.AgentList.setGeometry(QtCore.QRect(10, 10, 311, 531))
        self.AgentList.setObjectName("AgentList")
        self.AgentSelect.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(340, 510, 451, 31))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Terminal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Terminal.setContentsMargins(0, 0, 0, 0)
        self.Terminal.setObjectName("Terminal")
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Terminal.addWidget(self.line_2)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(340, 390, 451, 116))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PushFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PushFile.setObjectName("PushFile")
        self.gridLayout.addWidget(self.PushFile, 0, 1, 1, 1)
        self.PullFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PullFile.setObjectName("PullFile")
        self.gridLayout.addWidget(self.PullFile, 0, 0, 1, 1)
        self.GetLoot = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GetLoot.setObjectName("GetLoot")
        self.gridLayout.addWidget(self.GetLoot, 1, 0, 1, 1)
        self.PushModule = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PushModule.setObjectName("PushModule")
        self.gridLayout.addWidget(self.PushModule, 1, 1, 1, 1)
        self.ExecComm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ExecComm.setObjectName("ExecComm")
        self.gridLayout.addWidget(self.ExecComm, 2, 0, 1, 1)
        self.RevSh = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RevSh.setObjectName("RevSh")
        self.gridLayout.addWidget(self.RevSh, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(340, 370, 451, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.BackendStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.BackendStatusLabel.setGeometry(QtCore.QRect(340, 530, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackendStatusLabel.setFont(font)
        self.BackendStatusLabel.setObjectName("BackendStatusLabel")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(339, 3, 451, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 447, 367))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.HostnameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.HostnameLabel.setGeometry(QtCore.QRect(10, 10, 81, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.HostnameLabel.setFont(font)
        self.HostnameLabel.setTextFormat(QtCore.Qt.AutoText)
        self.HostnameLabel.setObjectName("HostnameLabel")
        self.ConnectionTimeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ConnectionTimeLabel.setGeometry(QtCore.QRect(10, 40, 121, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ConnectionTimeLabel.setFont(font)
        self.ConnectionTimeLabel.setTextFormat(QtCore.Qt.RichText)
        self.ConnectionTimeLabel.setObjectName("ConnectionTimeLabel")
        self.ProcOwnerLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ProcOwnerLabel.setGeometry(QtCore.QRect(10, 70, 111, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ProcOwnerLabel.setFont(font)
        self.ProcOwnerLabel.setTextFormat(QtCore.Qt.RichText)
        self.ProcOwnerLabel.setObjectName("ProcOwnerLabel")
        self.Hostname = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.Hostname.setGeometry(QtCore.QRect(90, 10, 381, 25))
        self.Hostname.setText("")
        self.Hostname.setTextFormat(QtCore.Qt.AutoText)
        self.Hostname.setObjectName("Hostname")
        self.ConnectionTime = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ConnectionTime.setGeometry(QtCore.QRect(135, 40, 331, 25))
        self.ConnectionTime.setText("")
        self.ConnectionTime.setTextFormat(QtCore.Qt.RichText)
        self.ConnectionTime.setObjectName("ConnectionTime")
        self.ProcOwner = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ProcOwner.setGeometry(QtCore.QRect(120, 70, 341, 25))
        self.ProcOwner.setText("")
        self.ProcOwner.setTextFormat(QtCore.Qt.RichText)
        self.ProcOwner.setObjectName("ProcOwner")
        self.InterfacesLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.InterfacesLabel.setGeometry(QtCore.QRect(10, 100, 111, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.InterfacesLabel.setFont(font)
        self.InterfacesLabel.setTextFormat(QtCore.Qt.RichText)
        self.InterfacesLabel.setObjectName("InterfacesLabel")
        self.InterfaceTable = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.InterfaceTable.setGeometry(QtCore.QRect(10, 120, 431, 241))
        self.InterfaceTable.setObjectName("InterfaceTable")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.BackendStatus = QtWidgets.QLabel(self.centralwidget)
        self.BackendStatus.setGeometry(QtCore.QRect(450, 530, 331, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.BackendStatus.setFont(font)
        self.BackendStatus.setText("")
        self.BackendStatus.setObjectName("BackendStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 30))
        self.menubar.setObjectName("menubar")
        self.menuAgents_Available = QtWidgets.QMenu(self.menubar)
        self.menuAgents_Available.setObjectName("menuAgents_Available")
        self.menuLocal = QtWidgets.QMenu(self.menubar)
        self.menuLocal.setObjectName("menuLocal")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCompile_Client = QtWidgets.QAction(MainWindow)
        self.actionCompile_Client.setObjectName("actionCompile_Client")
        self.actionRegister_Client_Creds = QtWidgets.QAction(MainWindow)
        self.actionRegister_Client_Creds.setObjectName("actionRegister_Client_Creds")
        self.actionOpen_Terminal = QtWidgets.QAction(MainWindow)
        self.actionOpen_Terminal.setObjectName("actionOpen_Terminal")
        self.actionChange_C2_Server = QtWidgets.QAction(MainWindow)
        self.actionChange_C2_Server.setObjectName("actionChange_C2_Server")
        self.actionStart_Backend = QtWidgets.QAction(MainWindow)
        self.actionStart_Backend.setObjectName("actionStart_Backend")
        self.menuAgents_Available.addAction(self.actionCompile_Client)
        self.menuAgents_Available.addAction(self.actionRegister_Client_Creds)
        self.menuAgents_Available.addAction(self.actionStart_Backend)
        self.menuAgents_Available.addSeparator()
        self.menuAgents_Available.addAction(self.actionChange_C2_Server)
        self.menuLocal.addAction(self.actionOpen_Terminal)
        self.menubar.addAction(self.menuAgents_Available.menuAction())
        self.menubar.addAction(self.menuLocal.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Control Console"))
        self.PushFile.setText(_translate("MainWindow", "Push File"))
        self.PullFile.setText(_translate("MainWindow", "Pull File"))
        self.GetLoot.setText(_translate("MainWindow", "Get Loot"))
        self.PushModule.setText(_translate("MainWindow", "Push Module"))
        self.ExecComm.setText(_translate("MainWindow", "Execute Command"))
        self.RevSh.setText(_translate("MainWindow", "Reverse Shell"))
        self.BackendStatusLabel.setText(_translate("MainWindow", "Backend status: "))
        self.HostnameLabel.setText(_translate("MainWindow", "Hostname: "))
        self.ConnectionTimeLabel.setText(_translate("MainWindow", "Connection Time: "))
        self.ProcOwnerLabel.setText(_translate("MainWindow", "Process Owner: "))
        self.InterfacesLabel.setText(_translate("MainWindow", "Interfaces:"))
        self.menuAgents_Available.setTitle(_translate("MainWindow", "Server"))
        self.menuLocal.setTitle(_translate("MainWindow", "Local"))
        self.actionCompile_Client.setText(_translate("MainWindow", "Compile Client"))
        self.actionRegister_Client_Creds.setText(_translate("MainWindow", "Register Client Creds"))
        self.actionOpen_Terminal.setText(_translate("MainWindow", "Open Terminal"))
        self.actionChange_C2_Server.setText(_translate("MainWindow", "Change C2 Server"))
        self.actionStart_Backend.setText(_translate("MainWindow", "Start Backend"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './python/ui/manager_connection_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManagerServerConnect(object):
    def setupUi(self, ManagerServerConnect):
        ManagerServerConnect.setObjectName("ManagerServerConnect")
        ManagerServerConnect.resize(272, 207)
        self.IP = QtWidgets.QLineEdit(ManagerServerConnect)
        self.IP.setGeometry(QtCore.QRect(30, 70, 211, 25))
        self.IP.setObjectName("IP")
        self.Connect = QtWidgets.QPushButton(ManagerServerConnect)
        self.Connect.setGeometry(QtCore.QRect(30, 170, 214, 29))
        self.Connect.setObjectName("Connect")
        self.Title = QtWidgets.QLabel(ManagerServerConnect)
        self.Title.setGeometry(QtCore.QRect(10, 20, 191, 19))
        self.Title.setObjectName("Title")
        self.Port = QtWidgets.QLineEdit(ManagerServerConnect)
        self.Port.setGeometry(QtCore.QRect(30, 130, 81, 25))
        self.Port.setObjectName("Port")
        self.IPLabel = QtWidgets.QLabel(ManagerServerConnect)
        self.IPLabel.setGeometry(QtCore.QRect(30, 50, 191, 19))
        self.IPLabel.setObjectName("IPLabel")
        self.PortLabel = QtWidgets.QLabel(ManagerServerConnect)
        self.PortLabel.setGeometry(QtCore.QRect(30, 110, 191, 19))
        self.PortLabel.setObjectName("PortLabel")

        self.retranslateUi(ManagerServerConnect)
        QtCore.QMetaObject.connectSlotsByName(ManagerServerConnect)

    def retranslateUi(self, ManagerServerConnect):
        _translate = QtCore.QCoreApplication.translate
        ManagerServerConnect.setWindowTitle(_translate("ManagerServerConnect", "Dialog"))
        self.Connect.setText(_translate("ManagerServerConnect", "Connect"))
        self.Title.setText(_translate("ManagerServerConnect", "Server Connection Dialogue"))
        self.IPLabel.setText(_translate("ManagerServerConnect", "Server IP Address"))
        self.PortLabel.setText(_translate("ManagerServerConnect", "Server Port (defualt 22)"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './python/ui/server_backend_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_server_backend_dialog(object):
    def setupUi(self, server_backend_dialog):
        server_backend_dialog.setObjectName("server_backend_dialog")
        server_backend_dialog.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(server_backend_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.avail_backends_label = QtWidgets.QLabel(server_backend_dialog)
        self.avail_backends_label.setGeometry(QtCore.QRect(20, 20, 441, 20))
        self.avail_backends_label.setObjectName("avail_backends_label")
        self.port_label = QtWidgets.QLabel(server_backend_dialog)
        self.port_label.setGeometry(QtCore.QRect(30, 360, 81, 20))
        self.port_label.setObjectName("port_label")
        self.port_edit = QtWidgets.QLineEdit(server_backend_dialog)
        self.port_edit.setGeometry(QtCore.QRect(120, 360, 113, 32))
        self.port_edit.setObjectName("port_edit")
        self.scrollArea = QtWidgets.QScrollArea(server_backend_dialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 50, 601, 291))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 597, 287))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.avail_backends_list = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.avail_backends_list.setGeometry(QtCore.QRect(0, 0, 601, 291))
        self.avail_backends_list.setObjectName("avail_backends_list")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(server_backend_dialog)
        self.buttonBox.accepted.connect(server_backend_dialog.accept)
        self.buttonBox.rejected.connect(server_backend_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(server_backend_dialog)

    def retranslateUi(self, server_backend_dialog):
        _translate = QtCore.QCoreApplication.translate
        server_backend_dialog.setWindowTitle(_translate("server_backend_dialog", "Dialog"))
        self.avail_backends_label.setText(_translate("server_backend_dialog", "Available Backends"))
        self.port_label.setText(_translate("server_backend_dialog", "Port to use: "))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './python/ui/terminal_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Terminal(object):
    def setupUi(self, Terminal):
        Terminal.setObjectName("Terminal")
        Terminal.resize(890, 512)

        self.retranslateUi(Terminal)
        QtCore.QMetaObject.connectSlotsByName(Terminal)

    def retranslateUi(self, Terminal):
        _translate = QtCore.QCoreApplication.translate
        Terminal.setWindowTitle(_translate("Terminal", "Dialog"))
