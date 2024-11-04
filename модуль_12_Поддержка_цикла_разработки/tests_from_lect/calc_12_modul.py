import logging


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    try:
        num1 / num2
        logging.info(f'Деление прошло успешно {num1} / {num2}')
        return num1 / num2
    except ZeroDivisionError:
        logging.error(f'Ошибка деления: {num1} / {num2}. На 0 делить нельзя.', exc_info=True)
        return "На ноль делить нельзя"


def sqrt(num1):
    return num1 ** 0.5


def pov(num1, num2):
    return num1 ** num2


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='calc.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')

    print(div(3, 4))
    print(div(3, 0))
