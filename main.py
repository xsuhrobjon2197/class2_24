#2-m
class CinemaTicket:
    def __init__(self, movie, price, is_booked):
        self.movie = movie
        self.price = price
        self.is_booked = is_booked
        
    def book(self):
        if self.movie == "Roman":
            print(f"Chipta band qilindi")
        
    def cancel(self):
        if self.price == 1000000000:
            print("Allaqachon band")
        
    
u1 = CinemaTicket("Roman", 73589347593498, "Kerak")

u1.book()
u1.cancel()
