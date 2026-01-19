class Agenda:
    def __init__(self):
        self._contactos = []
        self._contactos_por_telefono = {}

    def agregar_contacto(self, contacto):
        telefono = contacto.obtener_telefono()
        if telefono in self._contactos_por_telefono:
            return False

        self._contactos.append(contacto)
        self._contactos_por_telefono[telefono] = contacto
        return True

    def buscar_por_telefono(self, telefono):
        return self._contactos_por_telefono.get(telefono)

    def buscar_por_nombre(self, nombre):
        nombre = nombre.strip().lower()
        return [
            c for c in self._contactos
            if c.obtener_nombre().lower() == nombre
        ]

    def listar_contactos(self):
        return self._contactos

    # 🔹 NUEVO: editar contacto
    def editar_contacto(self, telefono, nuevo_nombre=None, nuevo_correo=None, nueva_direccion=None):
        contacto = self.buscar_por_telefono(telefono)
        if not contacto:
            return False

        try:
            if nuevo_nombre is not None:
                contacto.cambiar_nombre(nuevo_nombre)
            if nuevo_correo is not None:
                contacto.cambiar_correo(nuevo_correo)
            if nueva_direccion is not None:
                contacto.cambiar_direccion(nueva_direccion)
            return True
        except ValueError:
            return False

    # 🔹 NUEVO: eliminar contacto
    def eliminar_contacto(self, telefono):
        contacto = self.buscar_por_telefono(telefono)
        if not contacto:
            return False

        self._contactos.remove(contacto)
        del self._contactos_por_telefono[telefono]
        return True
