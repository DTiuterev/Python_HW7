# Выбор типа калькулятора, ввод чисел и математической операции, вывод результата на консоль.
type_num = 'r'
num_value = 0
num_oper = '+'

def get_type(type):
    global type_num
    if type == 0:
        check = True
        while(check):
            check = True
            type_num = input('Выберите тип чисел для использования калькулятора (введите r для рациональных чисел, c - для комплексных): ')
            if type_num in ('r', 'c'):
                check = False
            else:
                print('Вы ввели некорректный символ. Проверьте правильность ввода и раскладку клавиатуры.')
    elif type == 1:
        type_num = 'r'
    elif type == 2:
        type_num = 'c'
    return type_num


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_complex(value):
    try:
        complex(value)
        if complex(value).imag == 0:
            return False
        else:
            return True
    except ValueError:
        return False

def get_value(type):
    global num_value
    if type == 0:
        check = True
        while(check):
            check = True
            if type_num == 'r':
                num_value = input("Введите рациональное число (если число дробное, то разделитель . (точка): ")
                if is_float(num_value):
                    check = False
                else:
                    print('Вы ввели не рациональное число, повторите ввод. Проверьте символ разделителя.')
            if type_num == 'c':
                num_value = input('Введите комплексное число вида a+bj, где a и b вещественные числа, j - символ мнимой единицы (например, 5+3j или 3.2-4.12j): ')
                if is_complex(num_value):
                    check = False
                else:
                    print('Вы ввели не комплексное число, повторите ввод.\nПроверьте символ разделителя дробной части (.), отсутствие пробелов и наличие j (символа мнимой единицы).')
    return num_value

def get_oper(type):
    global num_oper
    op = ['+', '-', '*', '/']
    if type == 0:
        check = True
        while(check):
            check = True
            num_oper = input('Введите арифметическую операцию (+, -, * или /): ')
            if num_oper in op:
                check = False
            else:
                print('Вы ввели некорректный символ арифметической операции. Проверьте и повторите ввод.')
    return num_oper

def view_res(type, res):
    if type == 0:
        print(f'Результат операции = {res}')
    return res

def menu_collection(type):
    get_type(type)
    return (get_value(type), get_value(type), get_oper(type))