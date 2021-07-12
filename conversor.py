def conversor(tipo_moneda, valor_dolar):
    moneda = input("¿Cuántos " + tipo_moneda + " tienes?: ")
    moneda = float(moneda)
    dolares = moneda * valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Soles
2 - Pesos colombianos
3 - Pesos argentinos
4 - Pesos mexicanos
Elige una opicón: """

opcion = int(input(menu))

if opcion == 1:
    conversor("soles", 3.95)
elif opcion == 2:
    conversor("pesos colombianos", 0.00026)

elif opcion == 3:
    conversor("pesos mexicanos", 0.010)

elif opcion == 4:
    conversor("pesos argentinos", 0.05)

else:
    print('Por favor ingresa la opción correcta')

