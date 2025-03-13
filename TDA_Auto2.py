class Auto:
    def __init__(self, marca, modelo,aire_acondicionado=False, frenos_abs=False, asientos_cuero=False,control_crucero=False):
        self.__marca = marca
        self.__modelo = modelo
        self.__aire_acondicionado = aire_acondicionado
        self.__frenos_abs = frenos_abs
        self.__asientos_cuero = asientos_cuero
        self.__control_crucero = control_crucero

    # Métodos para obtener la información sobre el automóvil
    def obtener_marca(self):
        return self.__marca

    def obtener_modelo(self):
        return self.__modelo

    def obtener_aire_acondicionado(self):
        return self.__aire_acondicionado

    def obtener_frenos_abs(self):
        return self.__frenos_abs

    def obtener_asientos_cuero(self):
        return self.__asientos_cuero

    def obtener_control_crucero(self):
        return self.__control_crucero

    # Métodos para modificar la información sobre el automóvil
    def modificar_marca(self, marca):
        self.__marca = marca

    def modificar_modelo(self, modelo):
        self.__modelo = modelo

    def modificar_aire_acondicionado(self, tiene_aire_acondicionado):
        self.__aire_acondicionado = tiene_aire_acondicionado

    def modificar_frenos_abs(self, tiene_frenos_abs):
        self.__frenos_abs = tiene_frenos_abs

    def modificar_asientos_cuero(self, tiene_asientos_cuero):
        self.__asientos_cuero = tiene_asientos_cuero

    def modificar_control_crucero(self, tiene_control_crucero):
        self.__control_crucero = tiene_control_crucero

    # Metodo para saber las diferencias entre dos autos
    def __sub__(self, otro_auto):
        diferencias = []
        if(self.obtener_aire_acondicionado() != otro_auto.obtener_aire_acondicionado()):
            diferencias.append("Aire acondicionado")
        if(self.obtener_frenos_abs() != otro_auto.obtener_frenos_abs()):
            diferencias.append("Frenos ABS")
        if(self.obtener_asientos_cuero() != otro_auto.obtener_asientos_cuero()):
            diferencias.append("Asientos de cuero")
        if(self.obtener_control_crucero() != otro_auto.obtener_control_crucero()):
            diferencias.append("Control crucero")
        return diferencias

    # Metodo para saber las similitudes entre dos autos
    def __add__(self,otro_auto):
        similitudes = []
        if(self.obtener_aire_acondicionado() == otro_auto.obtener_aire_acondicionado()):
            similitudes.append("Aire acondicionado")
        if(self.obtener_frenos_abs() == otro_auto.obtener_frenos_abs()):
            similitudes.append("Frenos ABS")
        if(self.obtener_asientos_cuero() == otro_auto.obtener_asientos_cuero()):
            similitudes.append("Asientos de cuero")
        if(self.obtener_control_crucero() == otro_auto.obtener_control_crucero()):
            similitudes.append("Control crucero")
        return similitudes

    def __str__(self):
        return f"{self.obtener_marca()} {self.obtener_modelo()} - Aire Acondicionado: {self.obtener_aire_acondicionado()}, Frenos ABS: {self.obtener_frenos_abs()},Asientos de Cuero: {self.obtener_asientos_cuero()}, Control crucero: {self.obtener_control_crucero()}"

    def __repr__(self):
        return f"{self.obtener_marca()} {self.obtener_modelo()} - Aire Acondicionado: {self.obtener_aire_acondicionado()}, Frenos ABS: {self.obtener_frenos_abs()},Asientos de Cuero: {self.obtener_asientos_cuero()}, Control crucero: {self.obtener_control_crucero()}"


# Instanciacion
auto1 = Auto("Chevrolet", "Onix",True,False,False,True)
auto2 = Auto("Renault", "Kangoo",True,False,True,True)

# Cambio de parametros auto 1
auto1.modificar_aire_acondicionado(False)
auto1.modificar_asientos_cuero(True)
print(auto1)

# Cambio de parametros auto 2
auto2.modificar_control_crucero(False)
auto2.modificar_frenos_abs(True)
print(auto2)

# Operaciones entre instancias de la clase Auto
diferencias = auto1 - auto2
similitudes = auto1 + auto2
print(f"Diferencias entre {auto1.obtener_marca()} {auto1.obtener_modelo()} y {auto2.obtener_marca()} {auto2.obtener_modelo()}: {diferencias}")
print("----")
print(f"Similitudes entre {auto1.obtener_marca()} {auto1.obtener_modelo()} y {auto2.obtener_marca()} {auto2.obtener_modelo()}: {similitudes}")