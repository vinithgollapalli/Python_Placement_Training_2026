#wap to read a program on ticket booking system
class TicketBookingSystem:
    tickets = {}

    def login_method(self, username="admin", password="123456", phonenumber="1234567890"):
        phone = input("enter your phone number: ").strip()
        if len(phone) == 10 and phone.isdigit():
            print("successfull login")
            print("Available methods after login: 4) Ticket booking  5) Payment  6) Cancel  7) Exit")
            return True
        else:
            print("invalid phonenumber")
            return False
    
    def ticket_booking(self, phonenumber="1234567890", name="Rohith", password="123456", seats_list="1,2,3,4"):
        name = input("enter your name: ").strip()
        password = input("enter your password: ").strip()
        if name == "admin" and password == "123456":
            print("you are ready to book the ticket")
        else:
            print("Invalid credentials")
        print(name)

    def __init__(self, seats=10, price=120):
        self.seats = set(range(1, seats+1))
        self.price = price
        self.next_id = 1
        self.bookings = {}

    def show(self):
        return sorted(self.seats)

    def book(self, seats):
        if any(s not in self.seats for s in seats):
            return None, "Not available"
        for s in seats: self.seats.remove(s)
        tid = self.next_id; self.next_id += 1
        amt = self.price * len(seats)
        self.bookings[tid] = {"seats": seats, "amt": amt}
        TicketBookingSystem.tickets[tid] = {"seats": seats, "amt": amt}
        return tid, amt

if __name__=="__main__":
    sys = TicketBookingSystem()

    def amount(payment_method="Cash", payment_method1="UPI", payment_method2="card", card_number="1234567890"):
        payment_method = input("enter your payment method: ").strip()
        if payment_method == "Cash":
            price_ticket = 100
            GST = 0.18
            total_amount = price_ticket * GST
            print("The total amount to be paid is:", total_amount)

        elif payment_method == "UPI":
            price_ticket = 100
            GST = 0.18 + 0.05
            total_amount = price_ticket * GST
            print("The total amount to be paid is:", total_amount)

        elif payment_method == "card":
            card_number = input("enter your card number: ").strip()
            if len(card_number) <= 12:
                print("enter card number")
            else:
                price_ticket = 100
                GST = 0.18 + 0.10
                total_amount = price_ticket * GST
                print("The total amount to be paid is:", total_amount)
        print(payment_method)

    def ticket_cancellation():
        n=int(input("enter your ticket number: "))
        if n in TicketBookingSystem.tickets:
            del TicketBookingSystem.tickets[n]
            print("Ticket cancelled successfully")
        else:
            print("Invalid ticket number")
        print(n)

    while True:
        print("\n1) Show seats  2) Book  3) Login  4) Ticket booking  5) Payment  6) Cancel  7) Exit")
        c = input("Choose: ")
        if c=="1":
            print("Seats:", sys.show())
        elif c=="2":
            print("Seats:", sys.show())
            try: s=[int(x) for x in input("Seats: ").split(",")]
            except: print("Bad input"); continue
            tid,r=sys.book(s)
            print("Fail:",r) if tid is None else print(f"Ticket {tid}, Amt {r}")
        elif c=="3":
            sys.login_method()
        elif c=="4":
            sys.ticket_booking()
        elif c=="5":
            amount()
        elif c=="6":
            ticket_cancellation()
        elif c=="7":
            break