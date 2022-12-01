class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 60
    cilindrada = 1200

c = Coche()
print("Color: ", c.color, "\nRuedas: ", c.ruedas, "\nPuertas: ", c.puertas, ""
       "\nVelocidad: ", c.velocidad, "\nCilindrada: ", c.cilindrada)
