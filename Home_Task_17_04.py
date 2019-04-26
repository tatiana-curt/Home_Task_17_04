
while True:
    Polish_N = list(input('Введите выражение (формат: + 2 2): ').split())

    try:
      if len(Polish_N) != 3:
        raise Exception ('Чтобы получить результат введите 2 числа в павильном формате')
      elif int(Polish_N[1]) < 0 or int(Polish_N[2]) < 0:
        raise Exception('Введите положительные числа')
      else:
        assert str(Polish_N[0]) in ['+', '-', '*', '/'], 'Введите верный оператор: (+, -, *, /)'
        if Polish_N[0] == '+':
          print('Результат:', int(Polish_N[1]) + int(Polish_N[2]))
        elif Polish_N[0] == '-':
          print('Результат:', int(Polish_N[1]) - int(Polish_N[2]))
        elif Polish_N[0] == '*':
          print('Результат:', int(Polish_N[1]) * int(Polish_N[2]))
        elif Polish_N[0] == '/':
          print('Результат:', int(Polish_N[1]) / int(Polish_N[2]))
    except Exception as e:
      print(f'{type(e)}: {e}')
