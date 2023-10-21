import random

def escolher_palavra():
    palavras = ["python", "programacao", "inteligencia", "artificial", "desenvolvimento"]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    palavra_adivinhada = ["_"] * len(palavra)
    tentativas = 6
    letras_usadas = []

    print("Bem-vindo ao Jogo da Forca!")

    while True:
        letra = input(f"Palavra: {' '.join(palavra_adivinhada)}\nLetras usadas: {', '.join(letras_usadas)}\nTentativas restantes: {tentativas}\nDigite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já usou essa letra. Tente outra.")
            continue

        letras_usadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_adivinhada[i] = letra
        else:
            tentativas -= 1
            desenhar_forca(tentativas)

        if "_" not in palavra_adivinhada:
            print(f"Parabéns! Você adivinhou a palavra: {palavra}")
            break

        if tentativas == 0:
            print(f"Fim do jogo! A palavra era: {palavra}")
            break

def desenhar_forca(tentativas):
    desenhos = [
        """
         _______
         |     |
               |
               |
               |
               |
        ______|____
        """,
        """
         _______
         |     |
         O     |
               |
               |
               |
        ______|____
        """,
        """
         _______
         |     |
         O     |
         |     |
               |
               |
        ______|____
        """,
        """
         _______
         |     |
         O     |
        /|     |
               |
               |
        ______|____
        """,
        """
         _______
         |     |
         O     |
        /|\\    |
               |
               |
        ______|____
        """,
        """
         _______
         |     |
         O     |
        /|\\    |
        /      |
               |
        ______|____
        """,
        """
         _______
         |     |
         O     |
        /|\\    |
        / \\    |
               |
        ______|____
        """
    ]

    print(desenhos[6 - tentativas])

if __name__ == "__main__":
    jogar_forca()
