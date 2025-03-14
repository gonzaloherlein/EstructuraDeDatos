import copy as cp

class Lista:
  #TDA NodoLista
  class __NodoLista:
    def __init__(self, dato:any):
      self.dato = dato
      self.siguiente = None
    def tieneSiguiente(self)->bool:
      return self.siguiente != None

  ####Operaciones de TDA Lista
  def __init__(self, datoInicial:tuple=None):
    self.__primero = None
    if datoInicial != None:
      for dato in datoInicial:
        self.agregarAlFinal(dato)

  def estaVacia(self)->bool:
    return self.__primero == None

  def __repr__(self)->str:
    listaRepr = "primero"
    nodoAux = self.__primero
    while nodoAux != None:
      listaRepr += f" -> {nodoAux.dato}"
      nodoAux = nodoAux.siguiente
    listaRepr += " -|"
    return listaRepr

  def tamaño(self)->int:
    cantNodos = 0
    nodoAux = self.__primero
    while nodoAux != None:
      cantNodos += 1
      nodoAux = nodoAux.siguiente
    return cantNodos

  def agregarAlFinal(self, dato:any)->None:
    nodoNuevo = Lista.__NodoLista(dato)
    if self.estaVacia():
      self.__primero = nodoNuevo
    else:
      nodoAux = self.__primero
      while nodoAux.tieneSiguiente():
        nodoAux = nodoAux.siguiente
      nodoAux.siguiente = nodoNuevo

  def insertar(self, posIns:int, dato:any)->None:
    nodoNuevo = Lista.__NodoLista(dato)
    if posIns >= 0:
      if self.estaVacia():
        self.__primero = nodoNuevo
      elif posIns == 0:
        nodoNuevo.siguiente = self.__primero
        self.__primero = nodoNuevo
      else: #Posicion de insercion mayor a cero en lista no vacia
        nodoAux = self.__primero
        posAux = 0
        while posAux < posIns-1 and nodoAux.tieneSiguiente():
          nodoAux = nodoAux.siguiente
          posAux += 1
        #inserto el nodo nuevo en la posIns
        nodoNuevo.siguiente = nodoAux.siguiente
        nodoAux.siguiente = nodoNuevo
    else:
      raise IndexError("Posicion inválida")

  def eliminar(self, posDel:int)->any:
    datoDel = None
    if 0 <= posDel < self.tamaño():
      if posDel == 0:
        datoDel = self.__primero.dato
        self.__primero = self.__primero.siguiente
      else: #Posicion de borrrado mayor a cero (valida)
        nodoAux = self.__primero
        posAux = 0
        while posAux < posDel-1:
          nodoAux = nodoAux.siguiente
          posAux += 1
        #inserto el nodo nuevo en la posIns
        datoDel = nodoAux.siguiente.dato
        nodoAux.siguiente = nodoAux.siguiente.siguiente
    else:
      raise IndexError("Posicion inválida")
    return datoDel

  def obtener(self, posGet:int)->any:
    if 0 <= posGet < self.tamaño():
      dato = None
      nodoAux = self.__primero
      posAux = 0
      while posAux < posGet:
        nodoAux = nodoAux.siguiente
        posAux += 1
      dato = nodoAux.dato
    else:
      raise IndexError("Posicion inválida")
    return dato

  def intercambiarPrimeros(self):
    if self.__primero.siguiente != None:
      primerNodo = self.__primero #Accedo al primer nodo
      segundoNodo = primerNodo.siguiente #Accedo al segundo nodo
      primerNodo.siguiente = segundoNodo.siguiente #Cambio el link del primer nodo por el del segundo
      segundoNodo.siguiente = primerNodo # Cambio el link del segundo nodo por el primer
      self.__primero = segundoNodo #Cambio de lugar el segundo nodo con el primero

  def vaciar(self)->None:
    self.__primero = None

  def clonar(self):#->Lista
    return cp.deepcopy(self)

  def primero(self):
    return self.__primero

  def set_primero(self,nodo):
    self.__primero = nodo
    
   
#Ejercicio 3
#Escribir la operación del TDA Lista buscaElemento() que busque un elemento que recibe por parámetro. 
#La operación debe retornar una lista con las ubicaciones del elemento en la lista de entrada.
  def buscaElemento(self, elementoABuscar:int):
    listaPosiciones = Lista()
    if not self.estaVacia():
      nodoAux = self.__primero
      posAux = 0 # Vamos contando la posicion del elemento a buscar
      while nodoAux != None:
        if elementoABuscar == nodoAux.dato:
          listaPosiciones.agregarAlFinal(posAux)#Agregar un nodoal final de la lista listaPosiciones
        nodoAux = nodoAux.siguiente
        posAux += 1
    return listaPosiciones

#Ejercicio 4
#Escribir una operación del TDA Lista que elimine todas las ocurrencias de un elemento que recibe por parámetro y devuelva la cantidad de veces que se elimino el elemento
#Se deben eliminar todos los nodos que contengan al elemento
  def eliminarOcurrencias(self,elemento)->int:
    cantDeVeces = 0
    if not self.estaVacia():
        nodoAux = self.__primero
        posAux = 0
        while nodoAux != None:
            if elemento == nodoAux.dato:
                self.eliminar(posAux)
                cantDeVeces += 1
                posAux -= 1
            nodoAux = nodoAux.siguiente
            posAux += 1
    return cantDeVeces 
    
    
#Ejercicio 5
#Escribir una operación del TDA Lista que saque el nodo que esta al inicio de la lista (posición cero) y lo ponga en el final. 
#Hacer otra que haga lo contrario, saque el nodo del final y lo ponga al inicio.

  def primeroPorElUltimo(self):
    if not self.estaVacia():
      primerNodo = self.__primero # Nos guardamos el primer nodo de la lista
      self.__primero = primerNodo.siguiente # El segundo nodo de la lista lo pasamos a la primera posicion
      primerNodo.siguiente = None # Borramos la referencia del primer nodo de la lista
      nodoAux = self.__primero
      while nodoAux.siguiente != None:
        nodoAux = nodoAux.siguiente
      nodoAux.siguiente = primerNodo
      
  def ultimoPorElPrimero(self):
    ultimoNodo = None
    if not self.estaVacia():
      nodoAux = self.__primero
      while nodoAux.siguiente.siguiente != None:
        nodoAux = nodoAux.siguiente
      ultimoNodo = nodoAux.siguiente
      ultimoNodo.siguiente = self.__primero
      self.__primero = ultimoNodo
      nodoAux.siguiente = None

#Ejercicio 6
#Escribir una operación del TDA Lista que reemplace todas las ocurrencias de un numero por otro. 
#Ambos números los recibe por parámetro.
  def reemplazar(self,numeroReemplazado, numeroAReemplazar):
    nodoActual = self.__primero
    while nodoActual != None:
      if nodoActual.dato == numeroReemplazado:
          nodoActual.dato = numeroAReemplazar
      nodoActual = nodoActual.siguiente

#Ejercicio 7
#Escribir la operación duplicar() del TDA Lista que duplica el contenido de una lista.
  def duplicar(self):
    nodoActual = self.__primero
    posAux = 0
    tamañoDeLista = self.tamaño()
    while posAux < tamañoDeLista:
      self.agregarAlFinal(nodoActual.dato)
      nodoActual = nodoActual.siguiente
      posAux += 1

#Ejercicio 10
#Escribir una operación del TDA Lista que recibe dos números por parámetro
#La operación recorre la lista, si el elemento del nodo es menor que el primer parámetro se deja igual, 
#Si es mayor o igual, se reemplaza por el mismo número multiplicado por el otro parámetro.
  def reemplazaMayores(self,numeroAComparar,multiplicador):
    if not self.estaVacia():
        nodoAux = self.__primero
        while nodoAux != None:
            if nodoAux.dato >= numeroAComparar:
                self.reemplazar(nodoAux.dato,nodoAux.dato * multiplicador)
            nodoAux = nodoAux.siguiente

#Ejercicio 11
#Escribir una operación del TDA Lista que recibe dos números por parámetro: una posición y un número nuevo. 
#Recorre la lista hasta la posición y reemplaza el número de la lista por el nuevo.
  def reemplazarConPosicion(self,posicion,numeroNuevo):
    if not self.estaVacia():
        nodoAux = self.__primero
        posAux = 0
        while nodoAux != None:
            if posAux == posicion:
                nodoAux.dato = numeroNuevo
                nodoAux = nodoAux.siguiente
                posAux += 1

#Ejercicio 12
#Escribir la operación insertarOrdenado() del TDA Lista,que se llama desde una lista ordenada
#E inserta un número que recibe por parámetro en el lugar correcto (manteniendo el orden)
  def insertarOrdenado(self,numero):
    if not self.estaVacia():
      nodoAux = self.__primero
      posAux = 0
      insertado = False # Declaramos una variable para usarla de bandera si el numero se insertó o no
      while nodoAux != None and not insertado: # El bucle se repite si el nodo actual no es None y si no se insertó ningun numero
        if nodoAux.siguiente == None: # Este if esta en el caso de si es el ultimo nodo de una lista
          self.insertar(posAux + 1,numero)
          insertado = True
        elif numero > nodoAux.dato and numero < nodoAux.siguiente.dato: # Verificamos si el numero es mayor que el anterior o menor que el siguiente
          self.insertar(posAux + 1,numero)
          insertado = True
        nodoAux = nodoAux.siguiente
        posAux += 1
    else:
      self.agregarAlFinal(numero) # En el caso de que sea una lista vacia, lo agregamos

  def cantidadDeImparesEnLista(self):
    cantImpares = 0
    if not self.estaVacia():
      nodoAux = self.__primero
      while nodoAux != None:
        if not (nodoAux.dato % 2 == 0):
          cantImpares += 1
        nodoAux = nodoAux.siguiente
    return cantImpares
  
  def esPar(num:int)->bool:
    return num%2==0
  
  def posicionCantImpares(self,cantImpares):
    posHasta = 0 
    nodoAux = self.__primero
    if self.cantidadDeImparesEnLista() < cantImpares:
      return None
    while nodoAux != None and cantImpares != 0:
      if not (nodoAux.dato % 2 == 0):
        cantImpares -= 1
      posHasta += 1
      nodoAux = nodoAux.siguiente
    return posHasta - 1
  
  def eliminarFinal(self,posicion):
    if posicion > self.tamaño():
      return self
    nodoAux = self.__primero
    posAux = 0
    while nodoAux.tieneSiguiente() and posAux + 1 < posicion:
      nodoAux = nodoAux.siguiente
      posAux += 1
    nodoAux.siguiente = None
  
lista = Lista()
lista.agregarAlFinal(3),lista.agregarAlFinal(5),lista.agregarAlFinal(8),lista.agregarAlFinal(2);
lista.agregarAlFinal(6),lista.agregarAlFinal(7),lista.agregarAlFinal(5),lista.agregarAlFinal(8);
lista.agregarAlFinal(2);
lista.eliminarFinal(5)
print(lista)