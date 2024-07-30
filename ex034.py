sa = float(input('Qual é o salário do funcionário? R$'))
su = (sa*10/100)+sa
inf = (sa*15/100)+sa
if sa<=1250:
    print('O salário deste funcionário teve um aumento de 15%, indo de R${:.2f} para R${:.2f}.'.format(sa, inf))
else:
    print('O salário deste funcionário teve um aumento de 10%, indo de R${:.2f} para R${:.2f}.'.format(sa, su))