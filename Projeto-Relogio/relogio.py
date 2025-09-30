import tkinter as tk
from datetime import datetime
import random

def atualizar_relogio():
    """Função para atualizar a hora e a cor do relógio."""
      # Pega a hora atual no formato HH:MM:SS
    hora_atual = datetime.now().strftime('%H:%M:%S')
        
        # Gera uma cor hexadecimal aleatória
    cor_aleatorio = f'#{random.randint(0, 0xffffff):06x}'
        
        # Atualiza o texto e a cor da hora
    label_Relogio.config(text=hora_atual, fg=cor_aleatorio)
        
        # Chama a função novamente após 1000ms (1 segundo)
    janela.after(1000, atualizar_relogio)

# Cria a janela principal
janela = tk.Tk()
janela.title('Relogio Digital')
janela.geometry('400x150')
janela.configure(bg='#000000')  # Fundo preto
# Cria o rótulo (label) para o relógio
label_Relogio = tk.Label(
    janela,
    font =('DS-Digital', 60, 'bold'),
    bg ='#000000',
    fg = '#FFFFFF'
)
label_Relogio.pack(expand=True)
# Chama a função para iniciar o relógio
atualizar_relogio()
# Inicia o loop principal da interface
janela.mainloop()