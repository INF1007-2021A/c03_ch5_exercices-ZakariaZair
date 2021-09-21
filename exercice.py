#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
  
    return number if number >= 0 else number * -1


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    list_nom = []

    for letter in prefixes:
        list_nom.append(letter + suffixe)

    return list_nom


def prime_integer_summation() -> int:
    somme = 0
    count = 0
   
    return somme


def factorial(number: int) -> int:
    res = 1
    for i in range(number):
        res *= number-i
    
    return res


def use_continue() -> None:
    for i in range(1,11):
        if i == 5:
            continue
        else:
            print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    res = [None] * 8



    return res


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
