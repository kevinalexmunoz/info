perro = 0
gato = 0

class mascota(self, nombre, cedula, raza):
    self.nombre = nombre
    self.cedula = cedula
    self.raza = raza
    def present(self):
        print(f"Nombre: {self.nombre} / ceula: {self.nivel} / Raza : {self.raza}")


class perro(mascota):
  def __init__(self, nombre, cedula, raza):
    super().__init__(nombre, cedula, raza)

  def present(self):
        super().present()


class medicamento():
    pass

perro = perro()
perro("juan","jose","perro")