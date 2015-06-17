import sys
from Node import Node
from Widget import GraphWidget
from PySide import QtGui
from Settings import *


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    widget = GraphWidget()

    node1 = Node('NodeA', widget, 120, 40)
    node2 = Node('NodeB', widget, 120, 40)

    node1.add_port(PortTypes.kOutput, 'outA', Colors.kBlue)
    node1.add_port(PortTypes.kOutput, 'outB')

    node2.add_port(PortTypes.kInput, 'inpA')
    node2.add_port(PortTypes.kInput, 'inpB')

    widget.scene_widget.addItem(node1)
    widget.scene_widget.addItem(node2)

    widget.show()
    sys.exit(app.exec_())
