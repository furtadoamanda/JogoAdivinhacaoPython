# Jogo de Adivinhacao em Python 🎯🐍

Criei esse projeto para praticar os conhecimentos em Python.  
Trata-se de um jogo simples de adivinhação numérica, no qual é proposto ao usuário que acerte, em 5 tentativas, um número de 1 a 100.

O código se inicia importanto a biblioteca random e, em seguida, é definida a função principal da aplicação, *jogo_de_adivinhacao*
```python
def jogo_de_adivinhacao():
    tentativas = 5
    senha = random.randrange(1, 101)
```
Nessa parte inicial da função, o número inicial de tentativas é setado como 5, ao passo que a senha é definida como um número aleatório gerado pela função *random.randrange* entre os números 1 e 100.  
✏️ Aqui, vale ressaltar que tal função é definida nos moldes (start, stop), sendo que o número de start é inclusivo e o número de stop é exclusivo, razão pela qual se utiliza o número 101 como stop.  

## Laço while:
```python
try:
    while tentativas > 0:
                palpite = int(input("Escolha um número de 1 a 100: "))
                if palpite > 100 or palpite < 0:
                    print("Número inválido. Tente novamente.")
                else:
                    (...)
```
Inicialmente, o laço é definido para ser executado enquanto o número de tentativas for superior a 0, sendo que, sempre que for realizada uma nova execução, o usuário deverá inserir um novo palpite.  
A primeira verificação executada, definida no primeiro bloco if-else, refere-se a palpites que não se enquadrem no intervalo de 1 a 100, sendo palpites inválidos. Se o palpite não for inválido, será executado o bloco else, que engloba um novo bloco if-elif-else, com as principais funções do programa.
```python
            (...)
            else:
                if palpite > senha:
                    tentativas -= 1
                    print(
                        f"Você errou! O número secreto é menor. \nRestam *{tentativas}* tentativas.")
                elif palpite < senha:
                    tentativas -= 1
                    print(
                        f"Você errou! O número secreto é maior. \nRestam *{tentativas}* tentativas.")
                (...)
```
Nesse momento, são definidas as possibilidades de o palpite do usuário ser menor ou maior do que a senha. Em ambos os casos, o usuário é orientado sobre seu erro e se a senha é maior ou menor; ainda, são informadas quantas tentativas restam.  
Como no início do código as tentativas foram definidas como 5, a cada novo palpite do usuário esse total é decrescido de 1.
```python
                (...)
                elif palpite == senha:
                    tentativas -= 1
                    print(f"Você acertou!! Foram feitas {
                          5 - tentativas} tentativas. O número secreto é ** {senha} **.")
                    break
                (...)
```
Em seguida, é definida a alternativa em que o palpite do usuário corresponde à senha, sendo informado o acerto, o número de tentativas realizadas e qual a senha.  
Além disso, para o caso de acerto, é definida a quebra do laço while com o *break*, o que faz com que não seja solicitado um novo palpite do usuário, uma vez que a quebra força o encerramento do laço.
```python
        (...)
        else:
            print(
                f"Acabaram as tentativas... O número secreto era ** {senha} **.")
```
Finalmente, o bloco else acima refere-se ao próprio laço while, sendo executado, portanto, quando o número de tentativas atingir 0. Nesse caso, é informado ao usuário o fim de suas tentativas, bem como qual era a senha correta.

## Nova rodada:
```python
nova_rodada = int(input("""Novo jogo? 
            [1] - Sim
            [2] - Não
            >> """))
        if nova_rodada == 1:
            jogo_de_adivinhacao()
        else:
            print("Saindo...")
```
Ainda dentro da função *jogo_de_adivinhacao*, após encerradas as 5 tentativas ou acertada a senha, o usuário é proposto a indicar se quer jogar uma nova rodada, com uma nova senha e novas 5 tentativas.  
Se o usuário selecionar a alternativa 1, para jogar uma nova rodada, a função jogo_de_adivinhacao é chamada novamente à execução; ao passo que, se não for inserida a opção 1, o programa será encerrado a após a exibição da mensagem de saída.

## Exceção:
Importante destacar que a função *jogo_de_adivinhacao* possui um bloco try-except, dentro do qual é executado todo o laço while, bem como a possibilidade de nova rodada.  
Durante a execução, caso seja inserida pelo usuário uma entrada diferente de um número inteiro, será gerado um ValueError. Porém, como foi definida a exceção para esse caso, o programa não quebrará, mas sim será exibida a mensagem "Valor inválido. Programa encerrado", encerrando o programa sem quebras.
```python
except ValueError:
        print("Valor inválido. Programa encerrado.")
```

## Chamada da função:
```python
print(f"{"*" * 5} JOGO DE ADIVINHAÇÃO {"*" * 5}")
jogo_de_adivinhacao()
```
Encerrada a definição da função, as seguintes linhas de código definem o que será executado para o usuário, isto é, a mensagem de boas-vindas do jogo e a chamada para execução da função *jogo_de_adivinhacao* em si.