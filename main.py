from PyQt5.QtWidgets import QApplication
from DotaToolWindow import DotaToolWindow

app = QApplication([])
win = DotaToolWindow()
win.show()
app.exec_()