class Estudante():
  def __init__(self, nome, matricula, notas): 
    self.nome = nome
    self.matricula = matricula
    self.notas = notas 

  def media(self):
    print(sum(self.notas)/len(self.notas))

Victor = Estudante('Victor', '12345678', [10, 9, 5, 6, 4, 10])