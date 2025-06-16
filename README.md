<h1 align="center"><span style="color: orange">LAB_PROJECT_DIO:</span> Criando um sistema bancário com Python</h1>

<h3 align="center">Laboratório prático de desenvolvimento de software financeiro 💰</h3>
<div align="center">
<img src="https://cdn.lospec.com/gallery/piggy-bank-132881.gif" width="240px">
</div>

<br><br>

<div align="center">

# Objetivo geral e Desafio

"Criar um sistema bancário com as operações: Sacar, Depositar e Visualizar extrato." <br>
"Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e, para isso, escolheu a linguagem Python. Para a primeira versão do sistema, devemos implementar apenas 3 operações: depósito, saque e extrato"
</div>

<br><br>

# Teste o projeto você mesmo!

Você pode testar de duas maneiras:

1) Git clone:
```bash
git clone "https://github.com/JeffsHenrique/banco-python-lab-dio.git"
```

Depois, basta abrir o terminal:
```bash
python banco.py
```

ou

```bash
banco.py
```

2) Copie/cole o código dentro de [`banco.py`](banco.py)

<br><br>

# Funcionalidades do projeto

- [Depósito](#depósito)
- [Saque](#saque)
- [Extrato](#extrato)

<div align="center">

## [<span style="color:rgb(231, 188, 44)">[d]epósito</span>](#funcionalidades-do-projeto)

"Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário. Dessa forma, não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato"

</div>

### Outputs:

Depósito realizado:

```
informe o valor do depósito: 1000
>>> Depósito realizado: R$ 1000.00

>>> Saldo atual: 1000.00
```

<br><br>

<div align="center">

## [<span style="color:rgb(231, 188, 44)">[s]aque</span>](#funcionalidades-do-projeto)

"O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato."

</div>

### Outputs:

Saque efetuado:

```
informe o valor do saque: 500
>>> Depósito realizado: R$ 1000.00
>>> Saque realizado: R$ 500.00

>>> Saldo atual: 500.00
```

<br>

Limite de saque excedido:
```
informe o valor do saque: 800
Falha! O valor do saque excede o limite permitido de R$ 500.00.
>>> Saldo atual: 0.00
```

<br>

Saques diários excedidos:
```
informe o valor do saque: 154
Número de saques diários excedidos. Não é possível realizar mais saques.
```

<br>

Saldo insuficiente para saque:
```
informe o valor do saque: 10
Falha! Você não tem saldo suficiente para realizar essa operação.
>>> Saldo atual: 0.00
```

<br><br>

<div align="center">

## [<span style="color:rgb(231, 188, 44)">[e]xtrato</span>](#funcionalidades-do-projeto)

"Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: <span>Não foram realizadas movimentações.</span> Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: R$ 1500.45"

</div>

### Outputs

Extrato:

```
>>> Depósito realizado: R$ 1000.00
>>> Saque realizado: R$ 500.00
>>> Saque realizado: R$ 500.00

>>> Saldo atual: 0.00
```

<br>

Banco sem movimentações:
```
Não foram realizadas movimentações.
```

<br><br>
