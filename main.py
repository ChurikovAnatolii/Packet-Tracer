import threading
from operator import eq

from PyQt6 import QtCore, QtGui, QtWidgets
import UDP_socket
from DLE_RAW_CRC import DLE_Packet

class Ui_Astracer(object):

    def setupUi(self, Astracer):
        Astracer.setObjectName("Astracer")
        Astracer.resize(924, 925)
        font = QtGui.QFont()
        font.setPointSize(10)
        Astracer.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Kazay\\PycharmProjects\\ASTERIX_Packet_Tracer\\../../Downloads/bills.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Astracer.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Astracer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.AutoscrollRaw = QtWidgets.QCheckBox(self.centralwidget)
        self.AutoscrollRaw.setText('Scroll')
        self.AutoscrollRaw.setCheckable(True)
        self.AutoscrollRaw.setChecked(True)
        self.AutoscrollRaw.setTristate(False)
        self.AutoscrollRaw.setObjectName("AutoscrollRaw")
        self.verticalLayout_2.addWidget(self.AutoscrollRaw)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.portnum = QtWidgets.QLineEdit(self.widget)
        self.portnum.setMaximumSize(QtCore.QSize(91, 16777215))
        self.portnum.setObjectName("portnum")
        self.horizontalLayout.addWidget(self.portnum)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        # OpenSocket button
        self.openport = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.openport.setFont(font)
        self.openport.setMouseTracking(False)
        self.openport.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Kazay\\PycharmProjects\\ASTERIX_Packet_Tracer\\../../Downloads/ethernet.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.openport.setIcon(icon1)
        self.openport.setCheckable(True)
        self.openport.setChecked(False)
        self.openport.setAutoRepeat(False)
        self.openport.setAutoDefault(False)
        self.openport.setFlat(False)
        self.openport.setObjectName("openport")
        self.openport.setStyleSheet("background-color:rgb(102,255,102)")
        # -------------------------------------------------------------------
        self.verticalLayout_3.addWidget(self.splitter)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout.addWidget(self.listWidget_2)
        self.AutoscrollDecoded = QtWidgets.QCheckBox(self.centralwidget)
        self.AutoscrollDecoded.setCheckable(True)
        self.AutoscrollDecoded.setChecked(True)
        self.AutoscrollDecoded.setTristate(False)
        self.AutoscrollDecoded.setObjectName("AutoscrollDecoded")
        self.verticalLayout.addWidget(self.AutoscrollDecoded)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.openport_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.openport_2.setFont(font)
        self.openport_2.setMouseTracking(False)
        self.openport_2.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\Kazay\\PycharmProjects\\ASTERIX_Packet_Tracer\\../../Downloads/list-check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.openport_2.setIcon(icon2)
        self.openport_2.setCheckable(False)
        self.openport_2.setChecked(False)
        self.openport_2.setAutoRepeat(False)
        self.openport_2.setAutoDefault(False)
        self.openport_2.setFlat(False)
        self.openport_2.setObjectName("openport_2")
        self.horizontalLayout_2.addWidget(self.openport_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        Astracer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Astracer)
        self.statusbar.setObjectName("statusbar")
        Astracer.setStatusBar(self.statusbar)
        self.retranslateUi(Astracer)
        QtCore.QMetaObject.connectSlotsByName(Astracer)
        self.connect_functions()

    def retranslateUi(self, Astracer):
        _translate = QtCore.QCoreApplication.translate
        Astracer.setWindowTitle(_translate("Astracer", "ASTRACER"))
        self.label.setText(_translate("Astracer", "RAW DATA"))
        self.AutoscrollRaw.setText(_translate("Astracer", "Autoscroll"))
        self.label_2.setText(_translate("Astracer", "Port"))
        self.label_6.setText(_translate("Astracer", "Protocol"))
        self.comboBox.setItemText(0, _translate("Astracer", "UDP"))
        self.comboBox.setItemText(1, _translate("Astracer", "TCP SERVER"))
        self.comboBox.setItemText(2, _translate("Astracer", "TCP CLIENT"))
        self.openport.setText(_translate("Astracer", "Open "))
        self.label_3.setText(_translate("Astracer", "DECODED DATA"))
        self.AutoscrollDecoded.setText(_translate("Astracer", "Autoscroll"))
        self.label_5.setText(_translate("Astracer", "BYTE STAFFING"))
        self.comboBox_3.setItemText(0, _translate("Astracer", "RAW"))
        self.comboBox_3.setItemText(1, _translate("Astracer", "DLE"))
        self.comboBox_3.setItemText(2, _translate("Astracer", "DLE + CRC"))
        self.label_4.setText(_translate("Astracer", "ASTERIX CATEGORY"))
        self.comboBox_2.setItemText(0, _translate("Astracer", "CAT 150"))
        self.comboBox_2.setItemText(1, _translate("Astracer", "CAT 62"))
        self.openport_2.setText(_translate("Astracer", "Decode"))

    def connect_functions(self):
        self.openport.clicked.connect(self.open_port_thread)
        self.openport.clicked.connect(self.check_btn_state)

    def check_btn_state(self):
        if self.openport.isChecked():
            self.openport.setText('Close')
            self.openport.setStyleSheet("background-color:rgb(255,102,102)")
        else:
            self.openport.setText('Open')
            self.openport.setStyleSheet("background-color:rgb(102,255,102)")


    def add_too_list(self, data):
        line = str.upper(data.hex(' ', 1))
        self.listWidget.addItem(line)
        if self.AutoscrollRaw.isChecked():
            self.listWidget.scrollToBottom()
        if self.listWidget.count() >= 100:
            self.listWidget.repaint()


    def add_too_decode_List(self, data):
        line = str.upper(data.hex())
        self.pack_without_dle = DLE_Packet()
        try:
            pck_cut, cut_buffer = self.pack_without_dle.is_self_packet(line)
            if cut_buffer is not None:
                self.listWidget_2.addItem(cut_buffer)
                self.listWidget_2.addItem(pck_cut)
            else:
                self.listWidget_2.addItem(pck_cut)
        except TypeError:
            pass
        if self.AutoscrollDecoded.isChecked():
            self.listWidget.scrollToBottom()
        if self.listWidget_2.count() >= 100:
            self.listWidget_2.repaint()

    def take_portnum(self):
        try:
            port = self.portnum.text()
            return port
        except ValueError:
            pass

    def open_port_thread(self):
        th = threading.Thread(target=self.take_raw_data, args=())
        th.start()

    def take_raw_data(self):
             try:
                self.port = int(self.take_portnum())
                self.sock = UDP_socket.UdpSocket(self.port)
             except OSError:
                   pass
             while self.openport.isChecked():
                raw = self.sock.datarcv()
                self.add_too_list(raw)
                self.add_too_decode_List(raw)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Astracer = QtWidgets.QMainWindow()
    ui = Ui_Astracer()
    ui.setupUi(Astracer)
    Astracer.show()
    sys.exit(app.exec())




