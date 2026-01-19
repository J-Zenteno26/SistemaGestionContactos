from agenda import Agenda
from contacto import Contacto

def test_agregar_contacto():
    agenda = Agenda()
    contacto = Contacto("Ana", "987654321", "ana@mail.com")
    agenda.agregar_contacto(contacto)
    assert "987654321" in agenda.contactos
    print("✔ Test agregar contacto OK")

def test_buscar_contacto():
    agenda = Agenda()
    contacto = Contacto("Ana", "987654321", "ana@mail.com")
    agenda.agregar_contacto(contacto)
    resultado = agenda.buscar_por_nombre("Ana")
    assert len(resultado) == 1
    print("✔ Test buscar contacto OK")

if __name__ == "__main__":
    test_agregar_contacto()
    test_buscar_contacto()
