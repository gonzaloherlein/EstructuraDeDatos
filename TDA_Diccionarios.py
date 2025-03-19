import copy as cp

class Diccionario: # principal
  #######TDA tupla clave-significado#########################
  class __TuplaDic: # propósito principal será definir la igualdad por la clave de la relación
    def __init__(self, key, value): # contiene clave y significado
      self.__data = (key,value)

    def __repr__(self):
      return str(self.__data)

    def __eq__(self, key):
      return self.__data[0] == key

    def __hash__(self):
      return hash(self.__data[0])

    def getKey(self):
      return self.__data[0] # parte izquierda

    def getValue(self):
      return self.__data[1] # parte derecha
  ############################################################

  ###Constructor recibe dos listas de claves y significados en orden
  def __init__(self, keys = None, values = None):
    self.__diccionario = set() #conjunto
    if keys != None:
      if len(keys) == len(values):
        for i in range(len(keys)):
          self[keys[i]] = values[i]
      else:
        raise Exception("Las listas de pares clave-significado deben tener la misma cantidad")

  def __repr__(self):
    return str(self.__diccionario)

  ###Asignacion usando [], se recibe clave entre corchetes / Permite reemplazar aunque exista la clave
  def __setitem__(self, key = None, value = None):
    if key != None: # si la clave esta definida
      if key in self: # y si la clave ya existia
        self.__diccionario.remove(key) # la borramos
      self.__diccionario.add(Diccionario.__TuplaDic(key,value)) # la volvemos a definir

  ###No inserta si existe la clave, es decir, si la clave existe en el dicc no modifica el valor
  def insert(self, key = None, value = None):
    if key != None:
      self.__diccionario.add(Diccionario.__TuplaDic(key,value))

  ###Elimina si existe la clave, es decir, si la clave existe en el dicc elimina el par clave-valor
  ###Sino existe la clave, no hace nada
  def remove(self, key):
    if key in self:
        valor = self[key]
        self.__diccionario.remove(key)
        return valor

  ###Vacia dicc
  def clear(self):
    self.__diccionario = set()

  ###Clonar dicc
  def clone(self):
    return cp.deepcopy(self)

  ###Acceso a valores usando [], se recibe clave entre corchetes
  def __getitem__(self, key):
    value = None
    flag = False
    for tuplaDic in self.__diccionario:
      if tuplaDic.getKey() == key:
        value = tuplaDic.getValue()
        flag = True
    if flag:
      return value
    else:
      raise Exception("No existe la clave %s en el diccionario" % (key))

  ###Retorna valor de la clave que se recibe por parametro
  def get(self, key): # dado una clave, me devuelve el significado
    value = None
    flag = False
    for tuplaDic in self.__diccionario: # in definido abajo
      if tuplaDic.getKey() == key:
        value = tuplaDic.getValue()
        flag = True
    if flag:
      return value
    else:
      raise Exception("No existe la clave %s en el diccionario" % (key))

  ###Retorna lista con claves
  def keys(self): # por cada tupla del diccionario, la parte izquierda de la tupla.
    return [x.getKey() for x in self.__diccionario]

  ###Retorna lista con valores
  def values(self): # por cada tupla del diccionario, la parte derecha de la tupla.
    return [x.getValue() for x in self.__diccionario]

  ###Operador "in"
  def __contains__(self, key): #busca por la clave
    return key in self.__diccionario

  ###Tamaño de diccionario
  def len(self):
    return len(self.__diccionario)

#Ejercicio 9
  def contarCantidadDeVeces(lista,numero):
    contador = 0
    for elemento in lista:
        if elemento == numero:
            contador = contador + 1
    return contador

  def listaToDic(lista):
    dicSalida = Diccionario()
    for elemento in lista:
        formaMatriz = contarCantidadDeVeces(lista,elemento)
        matrizChirolas = np.full([formaMatriz,formaMatriz],elemento)
        dicSalida.insert(elemento,matrizChirolas)
    return dicSalida

#Ejercicio 10
  def promedios(listaDeMaterias,listaDeNotas):
    diccionario = Diccionario()
    for i in range(len(listaDeMaterias)):
        materia = listaDeMaterias[i]
        nota = listaDeNotas[i]
        if materia in diccionario:
        # Si la materia ya esta en el diccionario, actualizar el promedio
            promedio_actual = diccionario[materia]
            cantidad_notas = contarCantidadDeVeces(listaDeMaterias,materia)
            nuevo_promedio = (promedio_actual * (cantidad_notas - 1) + nota) / cantidad_notas
            diccionario[materia] = int(nuevo_promedio)
        else:
        #Si la materia no esta en el diccionario, agregarla con la nota actual
            diccionario[materia] = nota
    return diccionario
  
  def juntarPorValores(dic):
    dicSalida = Diccionario()
    for clave in dic.keys():
      claveDicSalida = dic[clave]
      if claveDicSalida not in dicSalida:
        dicSalida[claveDicSalida] = [clave]
      else:
        dicSalida[claveDicSalida].append(clave)
    return dicSalida
  
  def interseccion(dic1,dic2):
    inter = Diccionario()
    for clave in dic1.keys():
      if clave in dic2.keys():
        inter[clave] = (dic1[clave],dic2[clave])
    return inter
  
  def maximoPorClave(dic1):
    for clave in dic1.keys():
      listaNumeros = dic1[clave]
      dic1[clave] = max(listaNumeros)
  
  def posEnListas(lista1:list,lista2:list):
    dicSalida = Diccionario()
    for index in range(len(lista1)):
      if lista1[index] in lista2:
        if lista1[index] not in dicSalida:
          dicSalida.insert(lista1[index],[index])
        else:
          dicSalida[lista1[index]].append(index)
    for index in range(len(lista2)):
       dicSalida[lista2[index]].append(index)
    return dicSalida
  
  
  def traduccion(listaMorse,significado,mensaje):
    dic = Diccionario()
    mensajeSalida = []
    for index in range(len(listaMorse)):
      dic.insert(listaMorse[index],significado[index])
    for elemento in mensaje:
      if elemento in dic:
        mensajeSalida.append(dic[elemento])
    return mensajeSalida
    

listaMorse = ['000','001','010','100','011','110','111','002']
significado = ['k','r','c','d','e','o',' ','l']
mensaje = ['011','002','111','001','110','010','000']
mensajeSalida = Diccionario.traduccion(listaMorse,significado,mensaje)
print(mensajeSalida)
