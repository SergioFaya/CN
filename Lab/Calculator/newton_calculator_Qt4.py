"""
calculator0
Skeleton for calculator

Implements the inverse of a number using python division '/' 

Usage:
    
1) To open the calculator in graphic mode:
      
   python calculator0_Qt4.py                    
    
2) To use the calculator in command line: 
    
    python calculator0_Qt4.py --inverse number   
    
The result is written to calculator0.txt

"""


from __future__ import print_function
import sys
import PyQt4.QtCore as qtc
import PyQt4.QtGui as qtg
import argparse
import libCalculator as calc


class AppForm(qtg.QMainWindow):
    def __init__(self, parent=None):
        qtg.QMainWindow.__init__(self, parent)
        self.setWindowTitle('Calculator')
        self.create_main_frame()
        self.textbox.setText('')

    
    def create_main_frame(self):
        self.main_frame = qtg.QWidget()
        
        # GUI controls
        self.textbox = qtg.QLineEdit()
        self.textbox.setMinimumWidth(200)
        
        self.inverse_button = qtg.QPushButton('Inverse')
        self.reset_button = qtg.QPushButton('Reset')   
        self.sqrt_button = qtg.QPushButton('Square root')
        self.cbrt_button = qtg.QPushButton('Cubic root')

        # Buttons actions
        @qtc.pyqtSlot()
        def on_click_inverse():
            text = qtg.QLineEdit.text(self.textbox)
            # THIS LINE MUST BE REPLACED BY YOUR FUNCTION
            # TO PROVIDE THE INVERSE AND THE NUMBER OF ITERATIONS
            # PERFORMED BY NEWTON'S METHOD
            # IN THE GRAPHIC INTERFACE, WE DO NOT USE THE NUMBER OF ITERATIONS
            sol, numiter = calc.inverse(text);
            sol_format = '%10.10f' %sol
            self.textbox.setText(sol_format)  
            
        def on_click_reset():
            self.textbox.setText('')  
            
        def on_click_sqrt():
            text = qtg.QLineEdit.text(self.textbox)
            # THIS LINE MUST BE REPLACED BY YOUR FUNCTION
            # TO PROVIDE THE INVERSE AND THE NUMBER OF ITERATIONS
            # PERFORMED BY NEWTON'S METHOD
            # IN THE GRAPHIC INTERFACE, WE DO NOT USE THE NUMBER OF ITERATIONS
            sol, numiter = calc.sqrt(text);
            sol_format = '%10.10f' %sol
            self.textbox.setText(sol_format)  
            
        def on_click_cbrt():
            text = qtg.QLineEdit.text(self.textbox)
            # THIS LINE MUST BE REPLACED BY YOUR FUNCTION
            # TO PROVIDE THE INVERSE AND THE NUMBER OF ITERATIONS
            # PERFORMED BY NEWTON'S METHOD
            # IN THE GRAPHIC INTERFACE, WE DO NOT USE THE NUMBER OF ITERATIONS
            sol, numiter = calc.cbrt(text);
            sol_format = '%10.10f' %sol
            self.textbox.setText(sol_format) 
            
        self.inverse_button.clicked.connect(on_click_inverse)            
        self.reset_button.clicked.connect(on_click_reset)  
        self.sqrt_button.clicked.connect(on_click_sqrt)
        self.cbrt_button.clicked.connect(on_click_cbrt)
        
        # Geometry
        
        hbox1 = qtg.QHBoxLayout()
        hbox1.addWidget(self.textbox)
        hbox1.addWidget(self.reset_button)
        

        hbox2 = qtg.QHBoxLayout()        
        for w in [  self.inverse_button  ]:
            hbox2.addWidget(w)
            hbox2.setAlignment(w, qtc.Qt.AlignVCenter)
            
        hbox3 = qtg.QHBoxLayout()        
        for w in [  self.sqrt_button  ]:
            hbox3.addWidget(w)
            hbox3.setAlignment(w, qtc.Qt.AlignVCenter)
            
        hbox4 = qtg.QHBoxLayout()        
        for w in [  self.cbrt_button  ]:
            hbox4.addWidget(w)
            hbox4.setAlignment(w, qtc.Qt.AlignVCenter)
        
        vbox = qtg.QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)  
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)


#### MAIN

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--inverse')
    parser.add_argument('--sqrt')
    parser.add_argument('--cbrt')
    args = parser.parse_args()
    results = open('./calculator0.txt', 'a')
    if args.inverse:
        # THIS LINE MUST BE REPLACED BY YOUR FUNCTION
        # TO PROVIDE THE INVERSE AND THE NUMBER OF ITERATIONS
        # PERFORMED BY NEWTON'S METHOD
        sol1, numiter1 = calc.inverse(args.inverse);
        print('{:.10e}'.format(sol1),'{:d}'.format(numiter1), file=results)
        results.close() 
        
    elif (args.sqrt):
        sol2, numiter2 = calc.sqrt(args.sqrt);
        print('{:.10e}'.format(sol2),'{:d}'.format(numiter2), file=results)
        results.close() 
        
    elif (args.cbrt):
        sol3, numiter3 = calc.cbrt(args.cbrt);
        print('{:.10e}'.format(sol3),'{:d}'.format(numiter3), file=results)
        results.close() 

    else:
        app = qtg.QApplication(sys.argv)
        form = AppForm()
        form.show()
        app.exec_()

if __name__ == "__main__":
    main()