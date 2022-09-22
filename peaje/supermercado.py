__author__ = 'Lucas Dellamaggiore'

class Cliente:
    def __init__(self, code, caja, importe = 0.0):
        self.code = code
        self.caja = caja
        self.importe = importe
        

def to_string(cliente):
    r = ''
    r += '{:<20}'.format('Código de cliente: ' + cliente.code)
    r += '{:<20}'.format(' Caja: ' + str(cliente.caja))
    r += '{:<20}'.format(' Importe: ' + str(cliente.importe))
    return r

