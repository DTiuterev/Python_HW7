import viewer as vr
import rational_calculator as rc
import complex_calculator as cc
import logger as lr

def calc(first_numb, second_numb, numb_oper):
    lr.log_info(f'{first_numb} {numb_oper} {second_numb}')

    if vr.is_float(first_numb) and vr.is_float(second_numb):
        first_numb = float(first_numb)
        second_numb = float(second_numb)
        return rc.calc(first_numb, second_numb, numb_oper)

    if vr.is_complex(first_numb) and vr.is_complex(second_numb):
        first_numb = complex(first_numb)
        second_numb = complex(second_numb)
        return cc.calc(first_numb, second_numb, numb_oper)

    err = 'Given numbers have different types or inappropriate format'
    lr.log_error(err)
    return err