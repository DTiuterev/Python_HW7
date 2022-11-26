# Калькулятор для комплексных чисел.
def calc(first_num, second_num, math_oper):
    a_complex = first_num
    b_complex = second_num
    match math_oper:
        case '+':
            result = str(a_complex + b_complex)
            return result
        case '-':
            result = str(a_complex - b_complex)
            return result
        case '*':
            result = str(a_complex * b_complex)
            return result
        case '/':
            result = str(a_complex / b_complex)
            return result
