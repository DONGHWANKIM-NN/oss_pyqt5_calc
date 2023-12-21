import sys
from PyQt5.QtWidgets import *


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        

    def init_ui(self):
        main_layout = QVBoxLayout()
        
        integratelayout1_layout = QVBoxLayout()
        integratelayout2_layout = QHBoxLayout()



        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QGridLayout()
        layout_clear_equal = QGridLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        
        # issue 1번(#1) 숫자 입력 / 표시 부분 통합
        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_SumIO = QLabel("Line: ")
        self.SumIO = QLineEdit("")
        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(label_SumIO, self.SumIO)
    





        ### 사칙연산 버튼 및 equal(=), backspace 버튼 생성 (기존 나눠져 있던 부분 통합)
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        
        button_equal = QPushButton("=")
        button_backspace = QPushButton("Backspace")


        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        button_equal.clicked.connect(self.button_equal_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)


        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_operation.addWidget(button_plus, 4, 0)
        layout_operation.addWidget(button_minus, 3, 0)
        layout_operation.addWidget(button_product, 2, 0)
        layout_operation.addWidget(button_division, 1, 0)

        layout_operation.addWidget(button_backspace, 0, 0)
        layout_operation.addWidget(button_equal, 5, 0)






        ### %, C, CE, 1/x, x^2, 2√x 버튼 생성
        button_rest = QPushButton("%")
        button_ClearEntry = QPushButton("CE")
        button_Clear = QPushButton("C")
        button_inverse = QPushButton("1/x")
        button_pow = QPushButton("x^2")
        button_root = QPushButton("√x")


        ### %, C, CE, 1/x, x^2, 2√x 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_rest, 0 ,0)
        layout_clear_equal.addWidget(button_Clear, 0, 1)
        layout_clear_equal.addWidget(button_ClearEntry,0 ,2)
        layout_clear_equal.addWidget(button_inverse, 1 ,0)
        layout_clear_equal.addWidget(button_pow, 1, 1)
        layout_clear_equal.addWidget(button_root,1 ,2)






        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], 2+x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 5, 1)






        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 5, 0)






        ### 각 레이아웃을 main_layout 레이아웃에 추가
        integratelayout1_layout.addLayout(layout_clear_equal)
        integratelayout1_layout.addLayout(layout_number)
        
        integratelayout2_layout.addLayout(integratelayout1_layout)
        integratelayout2_layout.addLayout(layout_operation)
        
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(integratelayout2_layout)
        

        self.setLayout(main_layout)
        self.show()






    #################
    ### functions ###
    #################
    
    
    
    
    def number_button_clicked(self, num):
        equation = self.SumIO.text()
        equation += str(num)
        self.SumIO.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.SumIO.text()
        equation += operation
        self.SumIO.setText(equation)

    def button_equal_clicked(self):
        equation = self.SumIO.text()
        solution = eval(equation)
        self.SumIO.setText(str(solution))

    def button_clear_clicked(self):
        self.SumIO.setText("")
        self.SumIO.setText("")

    def button_backspace_clicked(self):
        equation = self.SumIO.text()
        equation = equation[:-1]
        self.SumIO.setText(equation)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())