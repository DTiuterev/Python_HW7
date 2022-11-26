# Калькулятор для рациональных чисел.
def calc(first_num, second_num, math_oper):
    a_rational = first_num
    b_rational = second_num
    round_accuracy = int(len(str(a_rational).split('.')[1]) + int(len(str(b_rational).split('.')[1])))
    match math_oper:
        case '+':
            return str(round(a_rational + b_rational, round_accuracy))
        case '-':
            return str(round(a_rational - b_rational, round_accuracy))
        case '*':
            return str(round(a_rational * b_rational, round_accuracy))
        case '/':
            if float(b_rational) == 0.0:
                return 'Делить на 0 нельзя.'
            else:
                return str(a_rational / b_rational)
