# Fonction pour initialiser la grille vide
def initialiser_grille():
    return [[' ' for _ in range(16)] for _ in range(16)]

# Fonction pour afficher la grille
def afficher_grille(grille):
    for ligne in grille:
        print('|'.join(ligne))
        print('-' * 31)

# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(grille, symbole):
    # Vérification des lignes
    for ligne in grille:
        if ''.join(ligne).count(symbole * 4) > 0:
            return True

    # Vérification des colonnes
    for colonne in range(16):
        if ''.join(grille[i][colonne] for i in range(16)).count(symbole * 4) > 0:
            return True

    # Vérification des diagonales
    for i in range(13):
        for j in range(13):
            if ''.join(grille[i + k][j + k] for k in range(4)).count(symbole * 4) > 0:
                return True
            if ''.join(grille[i + k][j + 3 - k] for k in range(4)).count(symbole * 4) > 0:
                return True

    return False

# Fonction principale pour jouer au Tic Tac Toe
def jouer_tic_tac_toe():
    grille = initialiser_grille()
    tour = 0
    symboles = ['X', 'O']

    while True:
        joueur = tour % 2
        symbole = symboles[joueur]

        afficher_grille(grille)

        # Demander au joueur de faire un mouvement
        while True:
            try:
                ligne = int(input(f'Joueur {joueur + 1}, entrez le numéro de ligne (1-16): ')) - 1
                colonne = int(input(f'Joueur {joueur + 1}, entrez le numéro de colonne (1-16): ')) - 1

                if 0 <= ligne < 16 and 0 <= colonne < 16 and grille[ligne][colonne] == ' ':
                    grille[ligne][colonne] = symbole
                    break
                else:
                    print('Mouvement invalide. Veuillez réessayer.')

            except ValueError:
                print('Veuillez entrer des nombres valides.')

        # Vérifier s'il y a un gagnant
        if verifier_victoire(grille, symbole):
            afficher_grille(grille)
            print(f'Le joueur {joueur + 1} ({symbole}) a gagné!')
            break

        # Vérifier s'il y a égalité
        if tour == 15 * 16 - 1:
            afficher_grille(grille)
            print('Match nul!')
            break

        tour += 1

if __name__ == "__main__":
    jouer_tic_tac_toe()
