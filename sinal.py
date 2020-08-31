def sinal():
    sinal = str(input('Digite a cor do sinal:')).lower()
    if sinal == 'verde':
        print('Siga')
    elif sinal == 'amarelo':
        print('Atenção')
    else:
        print('Pare')
def main():
    sinal()
if __name__=='__main__':
    main()

