class AccountShow:

    def show_current(self, account):
        print("Current Balance:", account.get_balance())

    def show_final(self, account):
        print("----- Final Account Summary -----")
        print("Name:", account.name)
        print("Current Balance:", account.get_balance())
        print("Interest Rate:", account.interest, "%")
        print("Interest Amount:", account.calculate_interest())
        print("Total Balance with Interest:", account.calculate_total_balance())