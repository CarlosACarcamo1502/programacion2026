class Expresion:
  def __add__(self, otro): return Suma(self, otro)
  def __sub__(self, otro): return Resta(self, otro)
  def __mul__(self, otro): return Producto(self, otro)
  def __pow__(self, otro): return Potencia(self, otro)
  def __radd__(self, otro): return Suma(otro, self)
  def __rsub__(self, otro): return Resta(otro, self)
  def __rmul__(self, otro): return Producto(otro, self)
  def _repr_latex_(self): return f"$${self.latex()}$$"


class Numero(Expresion):
    def __init__(self, valor):
        self.valor = valor
    def latex(self):
      return str(self.valor)
    def evaluar(self, variables=None):
        return self.valor

class Variable(Expresion):
    def __init__(self, nombre):
        self.nombre = nombre
    def latex(self):
      return f"\{self.nombre}" if len(self.nombre) > 1 else self.nombre
    def evaluar(self,variables):
      return variables[self.nombre]

class OperacionBinaria(Expresion):
   def __init__(self, izq, der):
        self.izq = Numero(izq) if isinstance(izq, (int, float)) else izq
        self.der = Numero(der) if isinstance(der, (int, float)) else der


class Suma(OperacionBinaria):
    def latex(self):
        return f"{self.izq.latex()} + {self.der.latex()}"
    def evaluar(self, variables):
        return self.izq.evaluar(variables) + self.der.evaluar(variables)

class Resta(OperacionBinaria):
    def latex(self):
      der_txt = f"({self.der.latex()})" if isinstance(self.der,(Suma,Resta)) else self.der.latex()
      return f"{self.izq.latex()} - {der_txt}"
    def evaluar(self, variables):
        return self.izq.evaluar(variables) - self.der.evaluar(variables)

class Producto(OperacionBinaria):
    def latex(self):
      izq_txt = f"({self.izq.latex()})" if isinstance(self.izq,(Suma,Resta)) else self.izq.latex()
      der_txt = f"({self.der.latex()})" if isinstance(self.der,(Suma,Resta)) else self.der.latex()
      return f"{izq_txt} \cdot {der_txt}"
    def evaluar(self, variables):
        return self.izq.evaluar(variables) * self.der.evaluar(variables)

class Potencia(Expresion):
    def __init__(self, base, exponente):
        self.base = Numero(base) if isinstance(base, (int, float)) else base
        self.exp = Numero(exponente) if isinstance(exponente, (int, float)) else exponente
