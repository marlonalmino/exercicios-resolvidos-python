# Crie uma lista com 4 frutas e construa um loop que imprima cada uma.
# frutas = ['banana', 'laranja', 'uva', 'ameixa']
# for fruta in frutas:
#     print(fruta)

# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido

# Código do Gustavo
# while True:
#     n = float(input('Informe uma nota: '))
#     if (n < 0) or (n > 10):
#         print('Digite um valor entre 0 e 10...')
#     else:
#         break
# print(f'A nota informada foi: {n}')


# Código do Harry
# while True:
#     try:
#         nota = float(input('Insira uma nota de 0 a 10: '))
#     except:
#         print('Caractere inválido')
#         continue

    # if (nota < 0 or nota > 10):
    #     print('Valor invalido')
    #     continue
    
    # break

# print(f'Nota: {nota}')