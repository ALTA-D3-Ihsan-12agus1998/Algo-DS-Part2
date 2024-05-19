def playing_domino(cards, deck) :
    valid_dominoes = []
    for domino in cards :
        if domino[0] in deck or domino[1] in deck :
            valid_dominoes.append(domino)

    return max(valid_dominoes, default=[])


if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []