#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python task.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
import logging

class Client:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname
    
    def print_info(self):
        print(f"Client: {self.name} {self.surname}")

class ClientBankEntity(Client):
    def __init__(self, client, amount_of_money):
            super().__init__(client.id, client.name, client.surname)
            self.__amount_of_money = amount_of_money
    
    def withdraw_money(self, amount_to_withdraw):
        self.__amount_of_money -= amount_to_withdraw
        print(f"Recieved: {amount_to_withdraw}")
    
    def deposit_money(self, amount_to_depsit):
        self.__amount_of_money += amount_to_depsit
        print(f"Recieved: {amount_to_depsit}")
        

class Bank:
    def __init__(self):
        self.__bankid = 1
        self.__clients_list = {}

    def add_client(self, client, amount_of_money):
        self.__clients_list[client.id] = ClientBankEntity(client, amount_of_money)

    def print_all_clients(self):
        for client in self.__clients_list.values():
            client.print_info()

    def withdraw_money(self, client_id, amount_to_withdraw):
        self.__clients_list[client_id].withdraw_money(amount_to_withdraw)

    def send_money_from_one_to_another(self, sender_id, reciever_id, amount_to_send):
        self.__clients_list[sender_id].withdraw_money(amount_to_send)
        self.__clients_list[reciever_id].deposit_money(amount_to_send)
        print("Transaction completed")
        

class BankFactory:
    pass

if __name__ == "__main__":
    bank = Bank()
    client1 = Client(1, "New", "Client")
    client2 = Client(2, "Second", "Client")
    bank.add_client(client1, 1000)
    bank.add_client(client2, 2000)
    bank.print_all_clients()
    bank.withdraw_money(1, 100)

    bank.send_money_from_one_to_another(1,2,100)
