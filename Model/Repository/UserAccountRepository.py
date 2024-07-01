from Model.Models.KorisnickiNalog import KorisnickiNalog
from Model.Models.Enumerations import VrstaKorisnika
from Model.Observer.Subject import Subject

class UserAccountRepository():
    def __init__(self) -> None:
        self.accounts = []
        self.path = "Data/UserAccounts.txt"
        self.subject = Subject()
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            while True:
                row = f.readline()
                if row == None or row == "":
                    return
                row = row.strip("\n")
                parameters = row.split(",")
                account = self.assign_from_list(parameters)
                self.accounts.append(account)
    
    def assign_from_list(self, parameters):
        return KorisnickiNalog(int(parameters[0]), parameters[1], parameters[2], parameters[3])
    
    def convert_to_list(self, entity: KorisnickiNalog):
        return [str(entity.id), entity.korisnicko_ime, entity.lozinka, entity.uloga]
    
    def save(self):
        with open(self.path, "w") as f:
            for account in self.accounts:
                parameters = self.convert_to_list(account)
                row = ",".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        self.accounts.sort(key=lambda x: x.id)
        last_account = self.accounts[-1]
        return last_account.id + 1

    def add_account(self, account: KorisnickiNalog):
        self.accounts.append(account)
        self.save()
        self.subject.notify_observers()

    def delete_account(self, id: int):
        account_to_remove = None
        for account in self.accounts:
            if account.id == id:
                account_to_remove = account
                break
        if account_to_remove != None:
            self.accounts.remove(account_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_accounts(self):
        return self.accounts