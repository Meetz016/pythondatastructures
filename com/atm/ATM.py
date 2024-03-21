class ATM:
    def __init__(self):
        self.balance=10000
        self.arr=["-------"]*5
        self.index=0
    #1.withdraw
    def withdraw(self,amount):
        if(self.balance<=0 or amount>self.balance):
            print("Insufficient Funds")
        elif amount%100==0:
            if amount>10000:
                otp=int(input("Enter 4 digit otp:"))
                if len(str(otp))==4:
                    print("Transaction Successful")
                    self.arr[self.index%5]=f"{amount} withdrawn from the account."
                    self.index+=1
                else:
                    print("Enter Valid 4 digit OTP")
            else:
                print("Transaction Successful")
                self.balance-=amount
                #mini statement remaining
                self.arr[self.index%5]=f"{amount} withdrawn from the account."
                self.index+=1
                print("Available Balance:",self.balance)

    def deposit(self,amount):
        curr=int(input("Which Denomination You are Using (100,200,500):"))
        if curr==100 or curr==200 or curr==500:
            notes=(amount/curr)
            if notes>200:
                print("Maximum notes allowed is 200 at time")
            else:
                print("Amount Deposited Successfully")
                self.balance+=amount
                self.arr[self.index%5]=f"{amount} Deposited to the account."
                self.index+=1
                print("Available Balance is:",self.balance)
    def miniStatement(self):
        print("last 5 transactions are:")
        if(self.index==5):
            for i in range(0,5):
                self.arr[i]=self.arr[i+1]
        for string in self.arr:
            print(string)
        print(f"Available Balance is {self.balance}")

if __name__=="__main__":
    cus=ATM()
    while 1:
        print("1.Withdraw\n2.Deposit\n3.Mini-Statement\n4.Exit")
        num=int(input())
        if num==1:
            print("How Much You Want to Withdraw(In Multiples of 100s Only):")
            cus.withdraw(int(input()))
        elif num==2:
            print("How much you Want to deposit:")
            cus.deposit(int(input()))
        elif num==3:
            print("Mini-Statement:")
            cus.miniStatement()
        elif num==4:
            print("Exiting the program.")
            break
        print("-----------------------------------------")

