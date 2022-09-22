import random
from supermercado import Cliente
from supermercado import to_string

__author__ = 'Lucas Dellamaggiore'


# FUNCIÓN PARA VALIDAR LA ENTRADA DE NÚMEROS

def validate(num):
    n = int(input('Valor (mayor a ' + str(num) + ' por favor): '))
    while n <= num:
        n = int(input('Ingrese un valor correcto por favor... Cargue nuevamente: '))
    return n

# FUNCIÓN PARA VALIDAR QUE EL CÓDIGO SEA UN NÚMERO ENTRE 0 Y 6

def validate_code(min =0, max=6):
    code = int(input('Ingrese el código (Mayor o igual a ' + str(min) + ' y menor o igual a ' + str(max) + ':)'))
    while code < min or code > max:
        code = int(input('Ingrese un código válido por favor (Mayor o igual a ' + str(min) + ' y menor o igual a ' + str(max) + ':)'))
    return code

# FUNCIÓN PARA CARGAR DATOS MANUALMENTE
def read(supermercado):
    n = len(supermercado)
    for i in range(n):
        code = input('Patente[' + str(i) + ']:')
        
        print('Ingrese número de caja...')
        caja = validate_code(0, 6)
        
        print('Ingrese importe pagado...')
        importe = validate(-1)
        
        supermercado[i] = Cliente(code,caja,importe)
        print()

def opcion1(supermercado):
    print()
    print('Cargue los datos de los vehiculos: ')
    read(supermercado)

# FUNCIÓN PARA CARGAR DATOS ALEATORIAMENTE
def generate(supermercado):
    letras = ("A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    n = len(supermercado)
    for i in range(n):
        c1 = random.choices(letras, k=3)
        c1_str = "".join(c1)
        c2 = str(random.randint(100, 1000))
        code = c1_str + c2
        caja = random.randint(0,6)
        importe = random.randint(500,10000)
        
        supermercado[i] = Cliente(code, caja, importe)
    
    print('Hecho... Los datos fueron cargados exitosamente')
    
def opcion2(supermercado):
    print('Presione <enter> para cargar los datos automáticamente...')
    input()
    generate(supermercado)

#FUNCION PARA ORDENAR LOS CLIENTES POR SUS CODIGOS
def sort(supermercado):
    n = len(supermercado)
    for i in range(n-1):
        for j in range(i+1, n ):
            if(supermercado[i].code > supermercado[j].code):
                supermercado[i], supermercado[j] = supermercado[j], supermercado[i]


# FUNCION PARA MOSTRAR TODOS LOS DATOS DEL SUPERMERCADO
def display_all(supermercado):
    print()
    print('Lista completa de datos del supermercado: ')
    print()
    for c in supermercado:
        print(to_string(c))


def opcion3(supermercado):
    if supermercado[0] is None:
        print('No hay datos cargados en este momento...')
        return
    sort(supermercado)
    display_all(supermercado)


def display(supermercado, x):
    print()
    print('Listado de clientes que pasaron por la caja ', x ,'')
    for c in supermercado:
        if c.caja == x:
            print(to_string(c))

def opcion4(supermercado):
    if supermercado[0] is None:
        print('No hay datos cargados en este momento...')
        return
    x = validate_code(0, 6)
    display(supermercado, x)

def count(supermercado):
    vc = 7 * [0]
    va = 7* [0]
    for v in supermercado:
        d = v.caja
        vc[d] += 1
        va[d] += v.importe
    print('Cantidad de clientes e importe acumulado por cada caja: ')
    for i in range(7):
        if vc[i] != 0:
            print('Caja: ', '{:<4}'.format(str(i)), end='')
            print('Cantidad de clientes: ', '{:<6}'.format(str(vc[i])), end='')
            print('Total recaudado: ', '{:<10}'.format(str(va[i])))
            

def opcion5(supermercado):
    if supermercado[0] is None:
        print('No hay datos cargados en este momento...')
        return
    count(supermercado)
    
def principal():
    print('Ingrese la cantidad de clientes a cargar: ')
    n = validate(0)
    supermercado = n * [None]
    opcion = 0
    while opcion !=6:
        print('\nMenú de opciones: ')
        print('1. Cargar clientes en forma manual')
        print('2. Cargar clientes en forma automática')
        print('3. Listado de clientes ordenados por código')
        print('4. Clientes que pasaron por x caja')
        print('5. Conteo de clientes e importe acumulado (por caja)')
        print('6. Salir')
        print()
        print()
        opcion = int(input('Ingrese su opción: '))
        print()
        print()
        
        if opcion == 1:
            opcion1(supermercado)
        elif opcion == 2:
            opcion2(supermercado)
        elif opcion == 3:
            opcion3(supermercado)
        elif opcion == 4:
            opcion4(supermercado)
        elif opcion == 5:
            opcion5(supermercado)
        elif opcion == 6:
            print('---Saliendo del programa---')
        else:
            print('Opción seleccionada inválida')
            

#SCRIPT PRINCIPAL

if __name__ == "__main__":
    principal()