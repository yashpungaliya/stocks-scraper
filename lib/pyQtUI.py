import sys
from PyQt4.QtGui import *

from lib.getStockVal import *
from lib.plotStockGraph import *

stock_code= ""
times=""
delay=""
def window():
    app = QApplication(sys.argv)
    win = QWidget()
    flo = QFormLayout()
    win.setLayout(flo)
    win.setWindowTitle("Stork")
    win.setGeometry(500,100,500,250)
    win.show()

    line = QLineEdit()
    flo.addRow("Stock Code",line)
    line.textChanged.connect(textChanged)
    line.editingFinished.connect(enterPress)

    b2 = QPushButton()
    b2.setText("Find This")
    flo.addRow(b2)
    if b2.isChecked():
        enterPress()

    b3 = QPushButton()
    b3.setText("Plot Graph")
    flo.addRow(b3)
    b3.clicked.connect(call_plot_graph)


    l1 = QLineEdit()
    flo.addRow("Time Interval", l1)
    l1.setValidator(QDoubleValidator(0.01,100.00,4))
    l1.setText('10')
    l1.textChanged.connect(setDelay)
    l2 = QLineEdit()
    flo.addRow("No. of readings", l2)
    l2.setValidator(QIntValidator())
    l2.setText('5')
    l2.textChanged.connect(setNum)
    l2.setMaxLength(4)

    b4 = QPushButton()
    b4.setText("Triggered")
    b4.setDefault(False)
    flo.addRow(b4)
    b4.clicked.connect(call_random_graph)
	
    sys.exit(app.exec_())

def textChanged(text):
    global stock_code
    stock_code=text

def setDelay(text):
    global delay
    delay=text
    print("delay:"+delay)

def setNum(text):
    global times
    times=text
    print("times:"+times)

def call_plot_graph():
    filename=stock_code+'.csv'
    plot_graph(filename)

def call_random_graph():
    print(times+" "+delay)
    random_loop(times,delay)

def showMessage():

    msg = QMessageBox()
    msg.move(100,100)
    msg.setIcon(QMessageBox.Information)
    msg.setText(stock_code + "=" + str(stockValue))
    msg.setWindowTitle("Stock Value")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def enterPress():
    data=get_html_data(stock_code)
    global stockValue
    stockValue=find_stock_val(data)
    filename=stock_code+'.csv'
    write_to_csv(filename, stockValue)
    return stock_code,stockValue
    #showdialog()
    #showMessage()


if __name__ == '__main__':
    window()