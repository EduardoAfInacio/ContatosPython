def checarOpcaoInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print(f'Apenas números inteiros são aceitos. Tente novamente!')
            continue
        except KeyboardInterrupt:
            print('A opção não foi escolhida. Tente novamente!')
            continue
        else:
            return n


def checarOpcaoStr(msg):
    while True:
        try:
            n = str(input(msg))
        except KeyboardInterrupt:
            print('Não foi digitado nada... Tente novamente.')
            continue
        else:
            return n