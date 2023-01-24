class ClassA:
    def f(self):
        print("A")

class ClassB:
    def f(self):
        print("B")

ktora = "A"

vyber ="""
klasa = Class{}()
""".format(ktora)
exec(vyber)

klasa.f()
