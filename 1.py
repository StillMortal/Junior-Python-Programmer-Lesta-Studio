# В первом, приведённом авторами задачи, случае
# для определения чётности используется взятие остатка при делении на два,
# что выполняется дольше, чем взятие побитового И в функции isEven2.
# Минус функции isEven2, пожалуй, заключается в читаемости:
# вероятно, для большинства программистов первый случай (функция isEven)
# покажется более читаемым.


def isEven(value):
    return value % 2 == 0


def isEven2(value):
    return value & 1 != 0