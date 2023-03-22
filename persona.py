class Persona:
    def __init__(self, nombre, rut, fecha_nac, ciudad, estado, email, usuario, clave):
        self.nombre = nombre
        self.rut = rut
        self.fecha_nac = fecha_nac
        self.ciudad = ciudad
        self.estado = estado
        self.email = email
        self.usuario = usuario
        self.clave = clave
        
    def mostrar_persona(self, datos):
        print("\n")
        for items in datos:
            print("\t" * 7 + f"{items}: {datos[items]}")

    def actualizar_persona(self, datos_actualizados, datos):
        datos = datos_actualizados
        return datos