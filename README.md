# Automação com PyAutoGUI

Este script utiliza a biblioteca **PyAutoGUI** para automatizar tarefas no Windows, como abrir o Chrome, buscar Python, abrir o VS Code e interagir com o Explorador de Arquivos.

---

## 🚀 Requisitos

- **Python** instalado.
- Biblioteca **PyAutoGUI**. Instale com:
  ```bash
  pip install pyautogui


## 📝 Funcionalidades
Abre o Chrome e busca por "vscode".
Realiza o download de Python em uma nova aba.
Abre o Explorador de Arquivos.
Exibe uma mensagem indicando o sucesso da instalação.


## ⚠️ Observações
As coordenadas de cliques (x, y) são específicas para a tela onde o script foi criado. Ajuste conforme necessário.
Para descobrir coordenadas, use:
  ```bash
  python
  Copiar código
  import pyautogui
  print(pyautogui.position())
