import datetime#pentru data angajarii

class Persoana:
    def __init__(self,nume,prenume,varsta):
        self.nume=nume
        self.prenume=prenume
        self.varsta=varsta
class Membru(Persoana):
    def __init__(self,nume,prenume,varsta,id):
        super().__init__(nume,prenume,varsta)
        self.id=id
        self.carti=[]# lista de carti imprumutate
        self.nr_carti=0# nr de carti imprumutate

    def imprumuta(self,carte):
        if carte.status=="disponibila":
            self.carti.append(carte)# adauga in lista cartea care e disponibila
            carte.status="imprumutata"# o imprumuta
            self.nr_carti += 1# creste nr de carti imprumutate
            print(f"{carte.titlu} a fost imprumutata.")
        else:
            print(f"{carte.titlu} nu este disponibila.")

    def returneaza(self, carte):
        if carte in self.carti:#daca exista o carte imprumutata in lista
            self.carti.remove(carte)# o stergem/o returnam
            carte.status="disponibila"# e disponibila iar
            self.nr_carti -= 1 #stergem cartea din lista cartilor imprumutate de membru
            print(f"{carte.titlu} a fost returnata.")
        else:
            print(f"{carte.titlu} nu e imprumutata de acest membru.")
class Bibliotecar(Persoana):
    def __init__(self,nume,prenume,varsta,data_angajarii):
        super().__init__(nume,prenume,varsta)
        self.data_angajarii=data_angajarii
    def cauta_carte(self,titlu,carti_biblioteca):
        for carte in carti_biblioteca:# cautam cartea in toate cartile din biblioteca
            if carte.titlu == titlu: # alegem titlul cartii
                if isinstance(carte, CarteFizica):#verif daca e de tip carte fizica pt status si locatie
                    print(f"Cartea '{titlu}' este {carte.status} si se afla la: {carte.locatie}.")
                else:
                    print(f"Cartea '{titlu}' a fost gasita.")
                return carte
        print(f"Cartea '{titlu}' nu exista.")
        return None
class Carte:
    def __init__(self,titlu,autor):
        self.titlu=titlu
        self.autor=autor
class CarteFizica(Carte):
    def __init__(self,titlu,autor,locatie,editura):
        super().__init__(titlu,autor)
        self.locatie=locatie
        self.editura=editura
        self.status="disponibila"# initial e disponibila

class Notificare:
    def __init__(self,email):
        self.email=email
    def trimite_notificare(self,notif):
        print(f"{self.email} nu a returnat cartea la timp. Notificare: {notif}")
def citeste_membru():
    nume=input("Numele membrului: ")
    prenume=input("Prenumele membrului: ")
    varsta=int(input("Varsta membrului: "))
    id=input("ID-ul membrului: ")
    return Membru(nume,prenume,varsta,id)
def citeste_bibliotecar():
    nume=input("Numele bibliotecarului: ")
    prenume=input("Prenumele bibliotecarului: ")
    varsta=int(input("Varsta bibliotecarului: "))
    data_angajarii=input("Data angajarii (YYYY-MM-DD) a bibliotecarului: ")
    data_angajarii=datetime.datetime.strptime(data_angajarii, "%Y-%m-%d").date()#convertim sirul in datatime an-luna-zi
    return Bibliotecar(nume,prenume,varsta,data_angajarii)
def citeste_carte():
    titlu=input("Titlul cartii: ")
    autor=input("Autorul cartii: ")
    return Carte(titlu,autor)
def citeste_carte_fizica():
    titlu=input("Titlul cartii fizice: ")
    autor=input("Autorul cartii fizice: ")
    locatie=input("Locatia cartii fizice: ")
    editura=input("Editura cartii fizice: ")
    return CarteFizica(titlu,autor,locatie,editura)
def main():
    membri=[]# lista membri
    bibliotecari=[]# lista bibliotecari
    carti_biblioteca=[]# toate cartile din biblioteca
    while True:
        optiune=input("Selecteaza o optiune: ")
        if optiune == "membru nou":
            membru_nou=citeste_membru()
            membri.append(membru_nou)#adaugam membru nou in lista membri
            print(f"\nMembru nou adaugat: {membru_nou.nume} {membru_nou.prenume}")
        elif optiune == "bibliotecar nou":
            bibliotecar_nou=citeste_bibliotecar()
            bibliotecari.append(bibliotecar_nou)#adaugam bibliotecar nou in lista cu bibliotecari
            print(f"\nBibliotecar nou adaugat: {bibliotecar_nou.nume} {bibliotecar_nou.prenume}")
        elif optiune == "carte noua":
            carte_noua=citeste_carte_fizica()
            carti_biblioteca.append(carte_noua)#adaugam carte noua in lista de carti din biblioteca
            print(f"\nCarte fizica adaugata: {carte_noua.titlu} {carte_noua.autor} {carte_noua.locatie} {carte_noua.editura} {carte_noua.status}")
        elif optiune == "cauta":
            titlu=input("Titlul cartii: ")
            nume_bibliotecar=input("Numele bibliotecarului: ")
            prenume_bibliotecar=input("Prenumele bibliotecarului: ")
            bibliotecar_gasit=None
            for bibliotecar in bibliotecari:#cautam bibliotecarul printre toti angajatii
                if bibliotecar.nume == nume_bibliotecar:#daca numele bibliotecarului exista
                    bibliotecar_gasit=bibliotecar
                    break
            if bibliotecar_gasit:
                carte_gasita=bibliotecar_gasit.cauta_carte(titlu,carti_biblioteca)#daca bibliotecarul exista cauta cartea
                if carte_gasita:
                    print(f"Cartea '{titlu}' a fost gasita.")
            else:
                print(f"Bibliotecarul '{nume_bibliotecar}' nu lucreaza aici")

        elif optiune == "imprumuta":
            id=input("ID-ul membrului: ").strip()#eliminam spatii
            titlu=input("Titlul cartii fizice: ").strip()#eliminam spatii
            membru_gasit=None
            carte_gasita=None
            for membru in membri:#cautam membru in lista
                if membru.id==id:#daca corespunde id-ul
                    membru_gasit=membru#am gasit membrul
                    break
            if membru_gasit:#daca exista membru inregistrat
                for carte in carti_biblioteca:
                    if carte.titlu==titlu:#daca exista cartea ceruta
                        carte_gasita=carte
                        break
                if carte_gasita:
                    membru_gasit.imprumuta(carte_gasita)#mebru imprumuta cartea
                else:
                    print(f"Cartea '{titlu}' nu exista fizic")
            else:
                print(f"Membrul cu ID-ul '{id}' nu e inregistrat aici")
        elif optiune == "returneaza":
            id=input("ID-ul membrului: ").strip()
            titlu=input("Titlul cartii: ").strip()
            membru_gasit=None
            carte_gasita=None
            for membru in membri:
                if membru.id==id:
                    membru_gasit=membru
                    break
            if membru_gasit:
                for carte in carti_biblioteca:
                    if carte.titlu==titlu:
                        carte_gasita=carte
                        break
                if carte_gasita:
                    membru_gasit.returneaza(carte_gasita)
                else:
                    print(f"Cartea '{titlu}' nu a fost imprumutata de aici!")
            else:
                print(f"Membrul cu ID-ul {id} nu e inregistrat aici")

        elif optiune == "exit":
            break
        else:
            print("Optiune invalida!")



if __name__ == "__main__":
    main()
