class Contact:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def displayContact(self):
        print("Nama:", self.name + ", Nomor Telepon:", self.phoneNumber)

    def updatePhoneNumber(self, newPhoneNumber):
        self.phoneNumber = newPhoneNumber
        print("Nomor telepon untuk", self.name, "berhasil diperbarui.")

    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phoneNumber

def displayMenu():
    print("======Daftar Kontak ========")
    print("1. Tambah Kontak")
    print("2. Lihat Kontak")
    print("3. Perbarui Nomor Telepon")
    print("4. Keluar")

def addContact(contacts):
    name = input("Masukkan nama kontak: ")
    phoneNumber = input("Masukkan nomor telepon: ")
    contacts.append(Contact(name, phoneNumber))
    print("Kontak berhasil ditambahkan.")

def displayContacts(contacts):
    if not contacts:
        print("Tidak ada kontak yang tersedia.")
    else:
        print("======= Daftar Kontak ========")
        for contact in contacts:
            contact.displayContact()

def updatePhoneNumber(contacts):
    name = input("Masukkan nama kontak yang akan diperbarui nomor teleponnya: ")
    found = False
    for contact in contacts:
        if contact.getName() == name:
            found = True
            newPhoneNumber = input("Masukkan nomor telepon baru: ")
            contact.updatePhoneNumber(newPhoneNumber)
            break
    if not found:
        print("Kontak tidak ditemukan.")

def main():
    contacts = []

    choice = 0
    while choice != 4:
        displayMenu()
        choice = int(input("Pilih menu: "))
        if choice == 1:
            addContact(contacts)
        elif choice == 2:
            displayContacts(contacts)
        elif choice == 3:
            updatePhoneNumber(contacts)
        elif choice == 4:
            print("Keluar dari program.")
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
