from enum import Enum

#Creamos una clase Order con un atributo 'status' al cual le pasamos el parametro choices
#Que es una lista de tuplas que itera la clase OrderStatus que hereda de la clase Enum(sirve para crear constantes enumeradas)

class OrderStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

choices = [ (tag, tag.value) for tag in OrderStatus ]