class Dico:
    def __init__(self):
        with open("mots.txt", encoding="utf-8") as file_words:
            self.words = [line_word for line_word in file_words] # Fetch all the words from a file
        with open("lettres.txt", encoding="utf-8") as file_lettres:
            self.lettres = [line_lettre for line_lettre in file_lettres] # Fetch all the letters from a file
            
    def getDico(self):
        """ This function returns our french dictionnary """
        return self.words

    def getLettres(self):
        """ This function returns our letters """
        return self.lettres

    def exist(self, mot):
        """ This function returns True if a word has been found from the dictionnary """
        if mot in self.words:
            return True
        return False

    def edit(self, mot):
        """ This function tries to change one letter in the word to find to an existing word """
        w = ""
        tab = list(mot)
        for i in range(len(mot)):
            for k in self.lettres:
                older = tab[i]
                tab[i] = k
                for m in tab:
                    w+= m[0]
                if(w in self.words):
                    return w
                w = ""
                tab[i] = older
        return mot


def main():
    """ This function allows you to try my fantastic program :) """
    a = input("Entrez un mot: ")
    dico = Dico()
    if(dico.exist(a)):
        return "Le mot rentré est correct !"
    edit = dico.edit(a + "\n")
    if(edit == a + '\n'):
        return "Le programme n'a rien trouvé ;("
    return "Le programme indique que vous vouliez écrire " + str(edit)

print(main())





