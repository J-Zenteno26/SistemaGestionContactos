class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.cambiar_nombre(nombre)
        self.cambiar_telefono(telefono)
        self.cambiar_correo(correo)
        self.cambiar_direccion(direccion)

    # GETTERS
    def obtener_nombre(self):
        return self._nombre

    def obtener_telefono(self):
        return self._telefono

    def obtener_correo(self):
        return self._correo

    def obtener_direccion(self):
        return self._direccion

    # SETTERS CON VALIDACIÓN
    def cambiar_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre.strip()

    def cambiar_telefono(self, telefono):
        if not telefono.isdigit() or len(telefono) < 8:
            raise ValueError("El teléfono debe contener solo números y al menos 8 dígitos")
        self._telefono = telefono

    def cambiar_correo(self, correo):
        if "@" not in correo or not correo.strip():
            raise ValueError("Correo electrónico inválido")
        self._correo = correo.strip()

    def cambiar_direccion(self, direccion):
        if not direccion or not direccion.strip():
            raise ValueError("La dirección no puede estar vacía")
        self._direccion = direccion.strip()