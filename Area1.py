import tkinter as tk
import random
janela = tk.Tk()
janela.title("Area 1")
janela.geometry("900x700")
canvas = tk.Canvas(janela, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
area_x1 = 100
area_y1 = 100
area_x2 = 800
area_y2 = 600
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
        self.prioridade_comida = 0
        self.prioridade_fuga = 0
        self.prioridade_explorar = 0 
        self.fome = 100
        self.agressividade = 0
        self.medo = 0
        self.canvas = canvas
        self.tamanho = 50
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
    def lembrar_perigo(self,x,y):
        self.memoria_perigo.append({
            "x": x,
            "y": y,
            "forca": 100
        })
        posicao = (x,y)
        if posicao not in self.memoria_perigo:
            self.memoria_perigo.append(posicao)
    def lembrar_presa(self,x,y):
        self.memoria_presa.append({
            "x": x,
            "y": y
        })
        posicao = (x,y)
        if posicao not in self.memoria_presa:
            self.memoria_presa.append(posicao)
    def verificar_memoria_perigo(self):
        for perigo in self.memoria_perigo:
            distancia = (
            (perigo["x"] - self.x) ** 2 +
            (perigo["y"] - self.y)** 2 
            ) ** 0.5
            if distancia < 100:
                self.medo += perigo["forca"] * 0.01
                self.estado = "fugindo"
   
    def interagir(self):
        if self.distancia_ate(ameaca) <20:
            self.vida -= 5
            self.medo += 15
            self.lembrar_perigo(
                ameaca.x,
                ameaca.y
            )
        if self.distancia_ate(comida) <30:
            self.fome = 100
            self.vida += 5
            if self.vida >= 100:
                self.vida = 100
            self.lembrar_presa(
                comida.x,
                comida.y
            )
        if self.distancia_ate(comida2) <30:
            self.fome = 100
            self.vida += 5
            self.lembrar_presa(
                comida.x,
                comida.y
            )
    def detectar_ameaca(self):
        if self.distancia_ate(ameaca) <100:
            self.perigo = ameaca

    def detectar_comida(self):
        if self.distancia_ate(comida) < 150:
            self.alvo = comida
        if self.distancia_ate(comida) > self.distancia_ate(comida2):
            self.alvo = comida2
            


    def atualizar_medo(self):
        if self.medo < 0 :
            self.medo = 0
        if self.medo > 0:
            self.medo -= 0.01
 
    def atualizar_fome(self):
        self.fome -= 0.01
        self.velocidade = self.velocidade_base
        if self.fome < 0 :
            self.fome = 0
        if self.fome <= 35:
            self.vida -= 0.1
    def atualizar_agressividade(self):
        self.agressividade = (
            (100 - self.vida) +
            (100 - self.fome)
        ) / 2
    def explorando(self):
        if random.randint(1,20) == 1:
            self.velocidade_x = random.randint(-5,5)
            self.velocidade_y = random.randint(-5,5)
    def observar(self,comida,comida2,ameaca):
        distancia_comida = self.distancia_ate(comida)
        distancia_comida = self.distancia_ate(comida2)
        distancia_ameaca = self.distancia_ate(ameaca)
        print("comida")
        distancia_comida = (
            (comida.x - self.x) ** 2 +
            (comida.y - self.y) ** 2
        ) ** 0.5
        if distancia_comida < 150:
            self.alvo = comida
        distancia_comida = (
            (comida2.x - self.x) ** 2 +
            (comida2.y - self.y) ** 2
        ) ** 0.5
        if distancia_comida < 150:
            self.alvo = comida2
        else:
            self.alvo = None
        print("perigo")
        distancia_ameaca = (
            (ameaca.x - self.x) ** 2 +
            (ameaca.y - self.y) ** 2
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
        if self.fome >= 75:
            self.explorando()
    def atualizar_fuga(self):
        if self.medo <= 20:
            self.explorando()
    def atualizar_prioridades(self):
        self.prioridade_comida = 100 - self.fome

        self.prioridade_fuga = self.medo
        
        self.prioridade_explorar = 20

    def estados(self):
        if self.estado == "cacando":
            self.cacando()
        elif self.estado == "explorando":
            self.explorando()
        elif self.estado == "fugindo":
            self.fugindo()
        print(self.estado)
    def decidir(self):
        prioridades = {
            "cacando": self.prioridade_comida,
            "fugindo": self.prioridade_fuga,
            "explorando": self.prioridade_explorar
        }
        self.estado = max(
            prioridades,
            key=prioridades.get
        )
        self.estados()

    

        self.estados() 
    def atualizar(self):
        if self.vida <=0:
            self.canvas.delete(self.objeto)
            return
        self.movimentacao()
        self.colisao()
        self.interagir()
        self.observar(comida,comida2,ameaca)
        self.decidir()
        self.atualizar_prioridades()
        self.atualizar_fome()
        self.detectar_comida()
        self.atualizar_fuga()
        self.atualizar_medo()
        self.atualizar_agressividade()
        self.detectar_ameaca()
        print(self.memoria_presa)
        print(self.prioridade_comida)
        print(self.memoria_perigo)
        print(self.prioridade_fuga)
        print(self.vida)
        print(self.fome)
        print(self.medo)
        print(self.agressividade)
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
        self.tamanho = 40
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
class presa2:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.vida = 100
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.velocidade = 5
        self.velocidade_base = self.velocidade
        self.movendo =  True
        self.tamanho = 40
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
        self.tamanho = 40
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
comida2 = presa2(canvas,200,200)
ameaca = ostil(canvas,200,200)
ia.atualizar()
comida.atualizar()
comida2.atualizar()
ameaca.atualizar()
janela.mainloop()







        

        



