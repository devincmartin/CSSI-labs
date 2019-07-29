#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
    pass

    def __str__(self):
        return "The name of my bank account is " + self.label + "and my balance is " + str(self.balance)

    # def withdraw(self, label, balance):
    #     if balance <= self.balance:
    #         self.balance -= amount
    #     return True

    def deposit(self, depositAmount):
        if depositAmount < 0:
            return
        self.balance += depositAmount
        print("\n Amount Deposited:", depositAmount)

    def withdraw(self, balance):
        if balance < 0:
            return
        if self.balance >= balance:
            self.balance -= balance
            print("\n You Withdrew:", balance)
        else:
            print("\n Insufficient balance  ")

    def rename (self, newName):
        if newName == "":
            print("invalid")
        else:
            self.label = newName

myBankAccount = BankAccount("FlagstarBank", 1000)
myBankAccount.deposit(100)

print(myBankAccount)




# myPokemon = Pokemon("Pikachu", "electric", "Male")
