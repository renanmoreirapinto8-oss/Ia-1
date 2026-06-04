import tkinter as tk
import random
janela = tk.Tk()
janela.title("Area 1")
janela.geometry("800x600")
canvas = tk.Canvas(janela, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
area_x1 = 100
area_y1 = 100
area_x2 = 700
area_y2 = 500
width = 3 
canvas.create_rectangle(area_x1, area_y1, area_x2, area_y2, outline="black", width=3)
tamanho = 300
class C1:
    def __init__(self,canvas,x,y):
        self.vida = 100
        self.x = x
        self.y = y
        self.memoria_presa = []
        self.memoria_perigo = []
        self.alvo = None
        self.estado = "explorando"
        self.velocidade = 5
        self.velocidade_base = self.velocidade
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.perigo = None
        self.movendo =  True
        self.fome = 100
        self.agressividade = 0
        self.medo = 0
        self.canvas = canvas
        self.tamanho = 30
        self.objeto = canvas.create_oval(
            x - self.tamanho /2,
            y - self.tamanho /2,
            x + self.tamanho /2,
            y + self.tamanho /2,
            fill="black"
        )
    def distancia_ate(self,alvo):
        return(
            (alvo.x - self.x) ** 2 +
            (alvo.y - self.y) ** 2
        ) ** 0.5
    def movimentacao(self):
        self.canvas.move(self.objeto, self.velocidade_x, self.velocidade_y)
        self.x += self.velocidade_x
        self.y += self.velocidade_y
    def mudar_direcao(self):
        self.velocidade_x = random.randint(-5,5)
        self.velocidade_y = random.randint(-5,5)
    def colisao(self):
        if self.x - self.tamanho /2 <= area_x1:
            self.velocidade_x = abs(self.velocidade_x)
        elif self.x + self.tamanho /2 >= area_x2:
            self.velocidade_x = -abs(self.velocidade_x)
        if self.y - self.tamanho /2 <= area_y1:
            self.velocidade_y = abs(self.velocidade_y)
        elif self.y + self.tamanho /2 >= area_y2:
            self.velocidade_y = -abs(self.velocidade_y)
    def detectar_ameaca(self):
        if self.distancia_ate(ameaca) <100:
            self.perigo = ameaca
        if self.distancia_ate(ameaca) <20:
            self.vida -= 5
    def detectar_comida(self):
        if self.distancia_ate(comida) < 150:
            self.alvo = comida
        if self.distancia_ate(comida) <30:
            self.fome = 100
        if self.distancia_ate(comida) <30:
            self.vida += 5
    def atualizar_medo(self):

        if self.medo < 0 :
            self.medo = 0
        self.medo =((100 - self.vida) // 5) * 5


    
    
    def atualizar_fome(self):
        self.fome -= 0.01
        self.velocidade = self.velocidade_base
        if self.fome < 0 :
            self.fome = 0
        if self.fome <= 35:
            self.vida -= 0.1
    def explorando(self):
        if random.randint(1,20) == 1:
            self.velocidade_x = random.randint(-5,5)
            self.velocidade_y = random.randint(-5,5)
    def observar(self,comida,ameaca):
        distancia_comida = self.distancia_ate(comida)
        distancia_ameaca = self.distancia_ate(ameaca)
        print("comida")
        distancia_comida = (
            (comida.x - self.x) ** 2 +
            (comida.y - self.y) ** 2
        ) ** 0.5
        if distancia_comida < 150:
            self.alvo = comida
        else:
            self.alvo = None
        print("perigo")
        distancia_ameaca = (
            (ameaca.x - self.x) ** 2 +
            (ameaca.y - self.x) ** 2
        ) ** 0.5
        if distancia_ameaca < 100:
            self.achar_perigo = ameaca
        else:
            self.achar_perigo = None
    def fugindo(self):
        distancia = self.distancia_ate(ameaca)
        if distancia < 50:
            if self.x > ameaca.x:
                self.velocidade_x = self.velocidade
            else:
                self.velocidade_x = -self.velocidade
            if self.y > ameaca.y:
                self.velocidade_y = self.velocidade
            else:
                self.velocidade_y = -self.velocidade
        ()
    def cacando(self):
        print("self.alvo")
        print(type(self.alvo))
        print("cacando")
        if self.alvo is None:
            return
        if self.alvo.x > self.x:
            self.velocidade_x = self.velocidade
        else:
            self.velocidade_x = -self.velocidade
        if self.alvo.y > self.y:
            self.velocidade_y = self.velocidade
        else: self.velocidade_y = -self.velocidade        
    def atualizar_cacando(self):
        if self.fome <= 40:
            self.cacando()
        if self.fome >= 75:
            self.explorando()
    def atualizar_fuga(self):
        if self.medo >= 40:
            self.fugindo()
        if self.medo <= 20:
            self.explorando()
    def estados(self):
        if self.estado == "cacando":
            self.cacando()
        elif self.estado == "explorando":
            self.explorando()
        elif self.estado == "fugindo":
            self.fugindo()
        print(self.estado)
    def decidir(self):
        if self.medo >= 40:
            self.estado = "fugindo"
        elif self.fome < 50:
            self.estado = "cacando"
        else:
            self.estado = "explorando"
    

        self.estados() 
    def atualizar(self):
        if self.vida <=0:
            self.canvas.delete(self.objeto)
            return
        print(self.vida)
        print(self.medo)
        print(self.fome)
        self.atualizar_fome()
        print("observar")
        self.observar(comida,ameaca)
        print("fugindo")
        self.atualizar_fuga()
        self.atualizar_medo()
        print("decidir")
        self.decidir()
        print("movendo")
        self.movimentacao()
        print("perigo")
        self.detectar_ameaca()
        print("detectar comida")
        self.detectar_comida()
        self.colisao()
        janela.after(20, self.atualizar)
class presa:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.vida = 100
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.velocidade = 5
        self.velocidade_base = self.velocidade
        self.movendo =  True
        self.tamanho = 30
        self.canvas = canvas
        self.objeto = canvas.create_oval(
            x - self.tamanho /2,
            y - self.tamanho /2,
            x + self.tamanho /2,
            y + self.tamanho /2,
            fill="gray"
        )
    def movimentacao(self):

        if random.randint(1,20) == 1:
            self.velocidade_x = random.randint(-5,5)
            self.velocidade_y = random.randint(-5,5)

        self.canvas.move(
            self.objeto,
            self.velocidade_x,
            self.velocidade_y
        )

        self.x += self.velocidade_x
        self.y += self.velocidade_y
    def mudar_direcao(self):
        self.velocidade_x = random.randint(-5,5)
        self.velocidade_y = random.randint(-5,5)
    def colisao(self):
        if self.x - self.tamanho /2 <= area_x1:
            self.velocidade_x = abs(self.velocidade_x)
        elif self.x + self.tamanho /2 >= area_x2:
            self.velocidade_x = -abs(self.velocidade_x)
        if self.y - self.tamanho /2 <= area_y1:
            self.velocidade_y = abs(self.velocidade_y)
        elif self.y + self.tamanho /2 >= area_y2:
            self.velocidade_y = -abs(self.velocidade_y)
    def atualizar_colisao(self):    
        distancia = (
        (self.x - ia.x) ** 2 +
        (self.y - ia.y) ** 2
        ) ** 0.5
        if distancia < 50:
            if self.x > ia.x:
                self.velocidade_x = self.velocidade
            else:
                self.velocidade_x = -self.velocidade
            if self.y > ia.y:
                self.velocidade_y = self.velocidade
            else:
                self.velocidade_y = -self.velocidade
        if distancia < 30:
            comida.x = random.randint(area_x1 + 30,area_x2 - 30)
            comida.y = random.randint(area_y1 + 30,area_y2 - 30)
            canvas.coords(
                comida.objeto,
                comida.x - comida.tamanho/2,
                comida.y - comida.tamanho/2,
                comida.x + comida.tamanho/2,
                comida.y + comida.tamanho/2
            )
    def atualizar(self):

        

        self.atualizar_colisao()
        self.movimentacao()
        self.colisao()
        janela.after(20, self.atualizar)
class ostil:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.vida = 100
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.velocidade = 7
        self.velocidade_base = self.velocidade
        self.movendo =  True
        self.tamanho = 30
        self.canvas = canvas
        self.objeto = canvas.create_oval(
            x - self.tamanho /2,
            y - self.tamanho /2,
            x + self.tamanho /2,
            y + self.tamanho /2,
            fill="red"
        )
    def movimentacao(self):

        if random.randint(1,20) == 1:
            self.velocidade_x = random.randint(-5,5)
            self.velocidade_y = random.randint(-5,5)

        self.canvas.move(
            self.objeto,
            self.velocidade_x,
            self.velocidade_y
        )

        self.x += self.velocidade_x
        self.y += self.velocidade_y
    def mudar_direcao(self):
        self.velocidade_x = random.randint(-5,5)
        self.velocidade_y = random.randint(-5,5)
    def colisao(self):
        if self.x - self.tamanho /2 <= area_x1:
            self.velocidade_x = abs(self.velocidade_x)
        elif self.x + self.tamanho /2 >= area_x2:
            self.velocidade_x = -abs(self.velocidade_x)
        if self.y - self.tamanho /2 <= area_y1:
            self.velocidade_y = abs(self.velocidade_y)
        elif self.y + self.tamanho /2 >= area_y2:
            self.velocidade_y = -abs(self.velocidade_y)
    def atualizar_colisao(self):    
        distancia = (
        (self.x - ia.x) ** 2 +
        (self.y - ia.y) ** 2
        ) ** 0.5

        if distancia < 20:
            ameaca.x = random.randint(area_x1 + 30,area_x2 - 30)
            ameaca.y = random.randint(area_y1 + 30,area_y2 - 30)
            canvas.coords(
                ameaca.objeto,
                ameaca.x - ameaca.tamanho/2,
                ameaca.y - ameaca.tamanho/2,
                ameaca.x + ameaca.tamanho/2,
                ameaca.y + ameaca.tamanho/2
            )   
    def atualizar(self):
        self.atualizar_colisao()
        self.movimentacao()
        self.colisao()
        janela.after(20, self.atualizar)
ia = C1(canvas, 400, 300)
comida = presa(canvas,200,200)
ameaca = ostil(canvas,200,200)
ia.atualizar()

comida.atualizar()
ameaca.atualizar()

janela.mainloop()







        

        



