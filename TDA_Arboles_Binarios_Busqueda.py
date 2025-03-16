from graphviz import Digraph # type: ignore
import copy as cp

class ABB:
  def __init__(self):
    self.__raiz = None
  def estaVacio(self)->bool:
    return self.__raiz == None
  def vaciar(self)->None:
    self.__raiz = None

  def treePlot(self, fileName='arbol')->None:
    if not self.estaVacio():
      treeDot = DiGraph()
      treeDot.node(str(self.__raiz.dato), str(self.__raiz.dato))
      self.__raiz.treePlot(treeDot)
      treeDot.render(fileName, view=True)

  ##################################################################
  ##################################################################
  class __NodoArbol:
    def __init__(self, dato):
      self.dato = dato
      self.izquierdo = None
      self.derecho = None
    def tieneIzquierdo(self)->bool:
      return self.izquierdo != None
    def tieneDerecho(self)->bool:
      return self.derecho != None
    def grado(self)->int:
      cantHijos = 0
      if self.tieneIzquierdo():
        cantHijos += 1
      if self.tieneDerecho():
        cantHijos += 1
      return cantHijos
    def esHoja(self)->bool:
      return self.grado() == 0

    def treePlot(self, dot:Digraph)->None:
      if self.tieneIzquierdo():
        dot.node(str(self.izquierdo.dato), str(self.izquierdo.dato))
        dot.edge(str(self.dato), str(self.izquierdo.dato))
        self.izquierdo.treePlot(dot)
      else:
        dot.node("-"+str(self.dato)+"l", "-")
        dot.edge(str(self.dato), "-"+str(self.dato)+"l")
      if self.tieneDerecho():
        dot.node(str(self.derecho.dato), str(self.derecho.dato))
        dot.edge(str(self.dato), str(self.derecho.dato))
        self.derecho.treePlot(dot)
      else:
        dot.node("-"+str(self.dato)+"r", "-")
        dot.edge(str(self.dato), "-"+str(self.dato)+"r")
        
#Insertar
class ABB(ABB):
  def insertar(self, dato:int)->None:
    nodoNuevo = ABB.__NodoArbol(dato)
    if self.estaVacio():
      self.__raiz = nodoNuevo
    else:
      self.__raiz.insertarNodo(nodoNuevo)

  class __NodoArbol(ABB.__NodoArbol):
    def insertarNodo(self, nodoNuevo)->None:
      if nodoNuevo.dato < self.dato:
        if self.tieneIzquierdo():
          self.izquierdo.insertarNodo(nodoNuevo)
        else:
          self.izquierdo = nodoNuevo
      elif nodoNuevo.dato > self.dato:
        if self.tieneDerecho():
          self.derecho.insertarNodo(nodoNuevo)
        else:
          self.derecho = nodoNuevo
      else:
        raise Exception("Dato repetido")   

#Buscar
class ABB(ABB):
  def buscar(self, datoBusc:int)->bool:
    estaDato = False
    if not self.estaVacio():
      estaDato = self.__raiz.buscarNodo(datoBusc)!=None
    return estaDato

  class __NodoArbol(ABB.__NodoArbol):
    def buscarNodo(self, datoBusc):
      nodoDatoBusc = None
      if self.dato == datoBusc:
        nodoDatoBusc = self
      elif datoBusc < self.dato:
        if self.tieneIzquierdo():
          nodoDatoBusc = self.izquierdo.buscarNodo(datoBusc)
      else:
        if self.tieneDerecho():
          nodoDatoBusc = self.derecho.buscarNodo(datoBusc)
      return nodoDatoBusc

#Pre-Orden
class ABB(ABB):
  def preOrden(self)->None:
    if not self.estaVacio():
      self.__raiz.preOrdenNodo()

  class __NodoArbol(ABB.__NodoArbol):
    def preOrdenNodo(self)->None:
      print(self.dato)
      if self.tieneIzquierdo():
        self.izquierdo.preOrdenNodo()
      if self.tieneDerecho():
        self.derecho.preOrdenNodo()

#Post-Orden
class ABB(ABB):
  def postOrden(self)->None:
    if not self.estaVacio():
      self.__raiz.postOrdenNodo()

  class __NodoArbol(ABB.__NodoArbol):
    def postOrdenNodo(self)->None:
      if self.tieneIzquierdo():
        self.izquierdo.postOrdenNodo()
      if self.tieneDerecho():
        self.derecho.postOrdenNodo()
      print(self.dato)

#In-Order
class ABB(ABB):
  def inOrden(self)->None:
    if not self.estaVacio():
      self.__raiz.inOrdenNodo()

  class __NodoArbol(ABB.__NodoArbol):
    def inOrdenNodo(self)->None:
      if self.tieneIzquierdo():
        self.izquierdo.postOrdenNodo()
      print(self.dato)
      if self.tieneDerecho():
        self.derecho.postOrdenNodo()

#Peso
class ABB(ABB):
  def peso(self)->int:
    cantNodos = 0
    if not self.estaVacio():
      cantNodos = self.__raiz.pesoNodo()
    return cantNodos

  class __NodoArbol(ABB.__NodoArbol):
    def pesoNodo(self)->int:
      cantNodos = 1
      if self.tieneIzquierdo():
        cantNodos += self.izquierdo.pesoNodo()
      if self.tieneDerecho():
        cantNodos += self.derecho.pesoNodo()
      return cantNodos

#Altura
class ABB(ABB):
  def profundidad(self)->int:
    profArbol = 0
    if not self.estaVacio():
      profArbol = self.__raiz.alturaNodo()
    return profArbol

  class __NodoArbol(ABB.__NodoArbol):
    def alturaNodo(self)->int:
      alturaNodoActual = 0
      alturaIzq = 0
      alturaDer = 0
      if not self.esHoja():
        if self.tieneIzquierdo():
          alturaIzq = self.izquierdo.alturaNodo()
        if self.tieneDerecho():
          alturaDer = self.derecho.alturaNodo()
        alturaNodoActual = 1 + max(alturaIzq, alturaDer)
      return alturaNodoActual
  
#Profundidad
class ABB(ABB):
  def profundidadElemento(self, datoBusc:int)->int:
    profElemento = None
    if not self.estaVacio():
      profElemento = self.__raiz.profundidadElementoNodo(datoBusc)
    return profElemento

  class __NodoArbol(ABB.__NodoArbol):
    def profundidadElementoNodo(self, datoBusc:int, nivelActual = 0)->int:
      profElemento = None
      if datoBusc == self.dato:
        profElemento = nivelActual
      elif datoBusc < self.dato:
        if self.tieneIzquierdo():
          profElemento = self.izquierdo.profundidadElementoNodo(datoBusc, nivelActual+1)
      else:
        if self.tieneDerecho():
          profElemento = self.derecho.profundidadElementoNodo(datoBusc, nivelActual+1)
      return profElemento
  
#Maximo
class ABB(ABB):
  def maximo(self)->int:
    maxElemento = None
    if not self.estaVacio():
      maxElemento = self.__raiz.maximoNodo().dato
    return maxElemento

  class __NodoArbol(ABB.__NodoArbol):
    def maximoNodo(self):#->__NodoArbol
      maxNodo = self
      if self.tieneDerecho():
        maxNodo = self.derecho.maximoNodo()
      return maxNodo

#Minimo
class ABB(ABB):
  def minimo(self)->int:
    minElemento = None
    if not self.estaVacio():
      minElemento = self.__raiz.minimoNodo().dato
    return minElemento

  class __NodoArbol(ABB.__NodoArbol):
    def minimoNodo(self):#->__NodoArbol
      minNodo = self
      if self.tieneIzquierdo():
        minNodo = self.izquierdo.minimoNodo()
      return minNodo

#Predecesor Y Sucesor
class ABB(ABB):
  def predYsucRaiz(self)->tuple[int,int]:
    predSuc = None
    if not self.estaVacio():
      predSuc = (self.__raiz.predecesorNodo().dato, self.__raiz.sucesorNodo().dato)
    return predSuc

  class __NodoArbol(ABB.__NodoArbol):
    def predecesorNodo(self):#->__NodoArbol
      nodoPred = None
      if self.tieneIzquierdo():
        nodoPred = self.izquierdo.maximoNodo()
      return nodoPred

    def sucesorNodo(self):#->__NodoArbol
      nodoSuc = None
      if self.tieneDerecho():
        nodoSuc = self.derecho.minimoNodo()
      return nodoSuc
  
#Ejercicio 2
#Escribir una operación del TDA ABB que calcule la cantidad de hojas de un árbol.
class ABB(ABB):
  def cantidadHojas(self)->int:
    cantHojas = 0
    if not self.estaVacio():
      cantHojas = self.__raiz.cantidadHojasNodo()
    return cantHojas

  class __NodoArbol(ABB.__NodoArbol):
    def cantidadHojasNodo(self)->int:
      cantHojas = 0
      if self.esHoja():
        cantHojas = 1
      else:
        if self.tieneIzquierdo():
           cantHojas += self.izquierdo.cantidadHojasNodo()
        if self.tieneDerecho():
           cantHojas += self.derecho.cantidadHojasNodo()
      return cantHojas

#Ejercicio 3
#Escribir una operación del TDA ABB que muestre los elementos que estan en el nivel N de un ABB, 
#El nivel se recibe por parámetro.
class ABB(ABB):
  def listaDeElementosEnNivel(self, nivelBuscado:int)->list:
    listaNivel = []
    if not self.estaVacio():
      self.__raiz.listaDeElementosEnNivelNodo(nivelBuscado, listaNivel)
    return listaNivel

  class __NodoArbol(ABB.__NodoArbol):
    def listaDeElementosEnNivelNodo(self, nivelBuscado:int, listaElementos:list, nivelActual:int=0)->None:
      if nivelActual == nivelBuscado:
        listaElementos.append(self.dato)
      elif nivelActual < nivelBuscado:
        if self.tieneIzquierdo():
          self.izquierdo.listaDeElementosEnNivelNodo(nivelBuscado, listaElementos, nivelActual+1)
        if self.tieneDerecho():
          self.derecho.listaDeElementosEnNivelNodo(nivelBuscado, listaElementos, nivelActual+1)

#Ejercicio 4
#Se define por frontera de un árbol, la secuencia formada por los elementos almacenados en las hojas de un árbol, 
#Tomados de izquierda a derecha. Escribir una operación del TDA ABB, que imprima por pantalla la frontera del árbol.
class ABB(ABB):
  def fronteraDeUnArbol(self)->list:
    frontera = []
    if not self.estaVacio():
      self.__raiz.fronteraDeUnArbolNivelNodo(frontera)
    return frontera

  class __NodoArbol(ABB.__NodoArbol):
    def fronteraDeUnArbolNivelNodo(self,frontera:list)->list:
      if self.esHoja():
        frontera.append(self.dato) #Si el nodo donde estoy parado es una HOJA, lo agrego a la lista de Frontera
      if self.tieneIzquierdo():
        self.izquierdo.fronteraDeUnArbolNivelNodo(frontera)
      if self.tieneDerecho():
        self.derecho.fronteraDeUnArbolNivelNodo(frontera)
      return frontera

#Ejercicio 5
#Escribir una operación del TDA ABB que retorne una lista ordenada (de menor a mayor) 
#Con todos los números pares que forman parte del árbol.
class ABB(ABB):
  def listaOrdenadaArbol(self)->list:
    listaOrdenada = []
    if not self.estaVacio():
      self.__raiz.listaOrdenadaNodo(listaOrdenada)
    return listaOrdenada

  class __NodoArbol(ABB.__NodoArbol):
    def listaOrdenadaNodo(self, listaOrdenada:list)-> list:
      if self.dato % 2 == 0:
        listaOrdenada.append(self.dato)
      if self.tieneIzquierdo():
        self.izquierdo.listaOrdenadaNodo(listaOrdenada)
      if self.tieneDerecho():
        self.derecho.listaOrdenadaNodo(listaOrdenada)
      return listaOrdenada.sort()

#Ejercicio 6
#Escribir una operación del TDA ABB, que rote el árbol completo, es decir, 
# los elementos del subárbol izquierdo deben ser mayores a la raíz y los del subárbol derecho menores (para todos los nodos del arbol). 
# No se debe retornar un nuevo arbol, sino modificar el arbol desde el que se llama a la operación.
class ABB(ABB):
  def rotarArbolCompleto(self):
    if not self.estaVacio():
      self.__raiz = self.__raiz.rotarArbolCompletoNodo()

  class __NodoArbol(ABB.__NodoArbol):
    def rotarArbolCompletoNodo(self):
      if self == None:
        return None
      self.izquierdo, self.derecho = self.derecho, self.izquierdo
      if self.tieneIzquierdo():
        self.izquierdo = self.izquierdo.rotarArbolCompletoNodo()
      if self.tieneDerecho():
        self.derecho = self.derecho.rotarArbolCompletoNodo()
      return self

#Ejercicio 7
#Escribir una operación del TDA ABB llamada cantidadNodosEnNivel que retorna la cantidad de nodos del arbol en un nivel determinado
class ABB(ABB):
  def listaDeElementosEnNivel(self, nivelBuscado:int)->list:
    listaNivel = []
    if not self.estaVacio():
      self.__raiz.listaDeElementosEnNivelNodo(nivelBuscado, listaNivel)
    return listaNivel

  class __NodoArbol(ABB.__NodoArbol):
    def listaDeElementosEnNivelNodo(self, nivelBuscado:int, listaElementos:list, nivelActual:int=0)->None:
      if nivelActual == nivelBuscado:
        listaElementos.append(self.dato)
      elif nivelActual < nivelBuscado:
        if self.tieneIzquierdo():
          self.izquierdo.listaDeElementosEnNivelNodo(nivelBuscado, listaElementos, nivelActual+1)
        if self.tieneDerecho():
          self.derecho.listaDeElementosEnNivelNodo(nivelBuscado, listaElementos, nivelActual+1)

class ABB(ABB):
  def cantidadNodosEnNivel(self,nivel)->int:
    cantNodos = 0
    if not self.estaVacio():
      cantElementosEnNivel = self.listaDeElementosEnNivel(nivel)
      for elementos in range(len(cantElementosEnNivel)):
        cantNodos += 1
    return cantNodos

class ABB(ABB):
  #Elimina nodo que contiene al datoBuscado si esta en el ABB sino no hace nada
  def eliminar(self, datoBuscado:int)->None:
    if not self.estaVacio():
      if self.__raiz.dato == datoBuscado:
        nodoReemplazo = self.__raiz.eliminarNodoEncontrado()
        self.__raiz = nodoReemplazo
      else:
        self.__raiz.eliminarNodo(datoBuscado)

  class __NodoArbol(ABB.__NodoArbol):
    #Retorna el predecesor o el sucesor del nodo que recibe como parametro o None si ambos no existen
    def predecesorOsucesorNodo(self):#->__NodoArbol
      nodoReemplazo = self.predecesorNodo()
      if not nodoReemplazo:
        nodoReemplazo = self.sucesorNodo()
      return nodoReemplazo

    #Busca datoBuscado en el ABB y retorna el nodo que contiene al dato, su nodo progenitor y de que lado esta
    #Si el datoBuscado no esta en el ABB retorna los tres como None
    def buscarProgenitorYlado(self, datoBuscado:int):#->tuple[__NodoArbol,__NodoArbol, str]
      nodoProgenitor = None
      nodoAeliminar = None
      ladoNodoAeliminar = None
      if datoBuscado < self.dato and self.tieneIzquierdo():
        if datoBuscado == self.izquierdo.dato:
          nodoProgenitor = self
          nodoAeliminar = self.izquierdo
          ladoNodoAeliminar = "izquierdo"
        else:
          nodoProgenitor, nodoAeliminar, ladoNodoAeliminar = self.izquierdo.buscarProgenitorYlado(datoBuscado)
      elif datoBuscado > self.dato and self.tieneDerecho():
        if datoBuscado == self.derecho.dato:
          nodoProgenitor = self
          nodoAeliminar = self.derecho
          ladoNodoAeliminar = "derecho"
        else:
          nodoProgenitor, nodoAeliminar, ladoNodoAeliminar = self.derecho.buscarProgenitorYlado(datoBuscado)
      return nodoProgenitor, nodoAeliminar, ladoNodoAeliminar

    #Elimina el nodo buscado cuando ya fue encontrado y retorna su reemplazante o None si no tiene reemplazo posible
    def eliminarNodoEncontrado(self):#->__NodoArbol
      nodoReemplazo = self.predecesorOsucesorNodo()
      if nodoReemplazo:
        self.eliminarNodo(nodoReemplazo.dato)
        nodoReemplazo.izquierdo = self.izquierdo
        nodoReemplazo.derecho = self.derecho
      return nodoReemplazo

    #Busca y elimina el nodo que contiene al datoBuscado, si no lo encuentra no hace nada
    def eliminarNodo(self, datoBuscado:int)->None:
      nodoProgenitor, nodoAeliminar, ladoNodoAeliminar = self.buscarProgenitorYlado(datoBuscado)
      if nodoProgenitor:
        nodoReemplazo = nodoAeliminar.eliminarNodoEncontrado()
        if ladoNodoAeliminar == "izquierdo":
          nodoProgenitor.izquierdo = nodoReemplazo
        else:
          nodoProgenitor.derecho = nodoReemplazo

class ABB(ABB):
  def mayoresEnNivel(self,nivel,n)->int:
    cantMayoresEnNivel = 0
    if not self.estaVacio():
      cantMayoresEnNivel = self.__raiz.mayoresEnNivelNodo(nivel,n)
    return cantMayoresEnNivel
  
  class __NodoArbol(ABB.__NodoArbol):
    def mayoresEnNivelNodo(self,nivel,n,nivelActual=0)->int:
      cantMayoresEnNivel = 0
      if nivelActual == nivel and self.dato > n:
        cantMayoresEnNivel += 1
      elif nivelActual < nivel:
        if self.tieneIzquierdo():
          cantMayoresEnNivel += self.izquierdo.mayoresEnNivelNodo(nivel,n,nivelActual+1)
        if self.tieneDerecho():
          cantMayoresEnNivel += self.derecho.mayoresEnNivelNodo(nivel,n,nivelActual+1)
      return cantMayoresEnNivel


#Ej 3 (TDA ABB)
class ABB(ABB):
  def padresOcupados(self)->int:
    cantPadresOcupados = 0
    if not self.estaVacio():
      cantPadresOcupados += self.__raiz.padresOcupadosNodo()
    return cantPadresOcupados
  
  class __NodoArbol(ABB.__NodoArbol):
    def padresOcupadosNodo(self)->int:
      cantPadresOcupados = 0
      if self.grado() == 2:
        cantPadresOcupados += 1
      if self.tieneIzquierdo():
        cantPadresOcupados += self.izquierdo.padresOcupadosNodo()
      if self.tieneDerecho():
        cantPadresOcupados += self.derecho.padresOcupadosNodo()
      return cantPadresOcupados

#Ej 4 (TDA ABB)
class ABB(ABB):
 def obtenerHermano(self, n):
        if self.raiz is None:
            return None

        return self._obtenerHermano(n, self.raiz, None)

 class __NodoArbol(ABB.__NodoArbol):
    def _obtenerHermano(self, n, nodo, padre):
        if nodo is None:
            return None
        
        if nodo.dato == n:
            if padre is None:
                return None  # La raíz no tiene hermanos
            
            if padre.izq and padre.izq.dato == n:
                if padre.der:
                    return padre.der.dato
                else:
                    return None
            elif padre.der and padre.der.dato == n:
                if padre.izq:
                    return padre.izq.dato
                else:
                    return None
            
        hermano_izq = self._obtenerHermano(n, nodo.izq, nodo)
        if hermano_izq is not None:
            return hermano_izq
        
        return self._obtenerHermano(n, nodo.der, nodo)

#Ej 5 (TDA ABB)
class ABB(ABB):
  def sumaHojas(self)->list:
    frontera = []
    if not self.estaVacio():
      self.__raiz.fronteraDeUnArbolNivelNodo(frontera)
    return sum(frontera)

  class __NodoArbol(ABB.__NodoArbol):
    def fronteraDeUnArbolNivelNodo(self,frontera:list)->list:
      if self.esHoja():
        frontera.append(self.dato) #Si el nodo donde estoy parado es una HOJA, lo agrego a la lista de Frontera
      if self.tieneIzquierdo():
        self.izquierdo.fronteraDeUnArbolNivelNodo(frontera)
      if self.tieneDerecho():
        self.derecho.fronteraDeUnArbolNivelNodo(frontera)
      return frontera
    
#Ej 6 (TDA ABB)
class ABB(ABB):
  def sumaHastaNivel(self,nivel)->int:
    suma = 0
    if not self.estaVacio():
      suma += self.__raiz.sumaHastaNivelNodo(nivel)
    return suma
  
  class __NodoArbol(ABB.__NodoArbol):
    def sumaHastaNivelNodo(self,nivel,nivelActual = 0):
      suma = 0
      if nivelActual <= nivel:
        suma += self.dato
      if self.tieneIzquierdo():
        suma += self.izquierdo.sumaHastaNivelNodo(nivel,nivelActual + 1)
      if self.tieneDerecho():
        suma += self.derecho.sumaHastaNivelNodo(nivel,nivelActual + 1)
      return suma

arbol1 = ABB()
arbol1.insertar(8),arbol1.insertar(3),arbol1.insertar(10),arbol1.insertar(1);
arbol1.insertar(14),arbol1.insertar(6),arbol1.insertar(4),arbol1.insertar(13);
arbol1.insertar(7);