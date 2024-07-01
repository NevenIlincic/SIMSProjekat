from Model.Models.Korisnik import Korisnik
from Model.Models.NeregistrovaniKorisnik import NeregistrovaniKorisnik

class RegisteredUsersRepository(NeregistrovaniKorisnik):
    def __init__(self) -> None:
        self.users = []
        self.path = "Data/RegisteredUsers.txt"
        self.load()

    def save(self):
        with open(self.path, "w") as f:
            for account in self.users:
                parameters = self.convert_to_list(account)
                row = ",".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        self.users.sort(key=lambda x: x.id)
        last_user = self.users[-1]
        return last_user.id + 1

    def add_account(self, user: Korisnik):
        self.users.append(user)
        self.save()
        self.subject.notify_observers()

    def assign_from_list(self, parameters):
        return Korisnik()
    
    def convert_to_list(self, entity: KorisnickiNalog):
        return [str(entity.id), entity.korisnicko_ime, entity.lozinka, entity.uloga]
    
    def dodaj_recenziju(self, recenzija ):
        pass

    def dodaj_ucesnik_delo(self, delo ):
        pass

    def dodaj_grupu(self, grupa):
        pass

    def promeni_jezik(self, jezik):
        pass

    def pregledaj_pocetnu_stranicu(self):
        pass

    def pregledaj_detalje_o_izvodjacima(self):
        pass

    def pregledaj_detalje_o_delima(self):
        pass
  
    def pretraga(self, upit: str):
        pass
