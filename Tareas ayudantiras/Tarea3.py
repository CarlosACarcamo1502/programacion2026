class: Playlist

  def __init__(self, nombre):
    self.nombre=nombre
    self.canciones=[]
    
  def añadir_canciones(self, titulo):
    self.canciones.append(titulo)
    print(f"{titulo} añadida a {self.nombres}")
  
  def eliminar_cancion(self, titulo):
    if titulo in self.canciones:
      self.canciones.remove(titulo)
      ptint(f"{titulo} ha sido eliminado de {self.nombres}")
    else:
      print (f"{titulo} no esta en {self.nombre}")

  def total_canciones(self):
    return len (self.canciones)

  def mostrar_playlist(self):
    print (f"Playlist: {self.nombre}")

  for i, titulo in(self.canciones, 1):
    print(f"{i} {titulo}")

  
