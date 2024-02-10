class Persona:
    def __init__(self, name, age):
        self.nombre = name
        self.edad = age

    def saludar(self):
        print(f"Hola me llamo {self.nombre} tengo: {self.edad} años.") 
        
# Crear objeto persona
persona1 = Persona("Durán", 79)
persona1.saludar()

esposa = Persona("Gabriela", 29)
esposa.saludar()


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando el grado {self.grado}.")

estudiante1 = Estudiante("Gabriela", 29, "Maestría")
estudiante1.saludar()
estudiante1.estudiar()