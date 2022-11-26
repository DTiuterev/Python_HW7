Калькулятор для рациональных и комплексных числел содержит модули:
1. Viewer - отвечает за выбор типа калькулятора, ввод чисел (рациональных или комплексных), выбор арифметической операции и вывод результата на консоль.
2. Complex calculator выполняет арифметические операции с комплексными числами с использованием метода complex. Не стал реализовывать округление вещественной части результата умножения и деления комплексных чисел, метод round не применим для метода complex. Видимо, нужно раскладывать результат и округлять цифры после запятой.
3. Rational calculator выполняет арифметические операции с рациональными числами (целыми и десятичными дробями). Округление не реализовано для операции деления, где необходима точность.
4. Controller связывает модули Viewer и Router.
5. Router связывает модули калькуляторов комплексных и рациональных чисел с модулями Viewer и Logger.
6. Logger получает данные пользователя и пополняет Log контент. Ошибки ввода некорректных чисел и операций отсекаются на этапе ввода данных и требуют повторного ввода.