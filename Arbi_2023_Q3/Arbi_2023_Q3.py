class Vehicle:
    
    def __init__(self, listingDetails):
        self.type = listingDetails[0]    # bike or car
        self.make = listingDetails[1]
        self.model = listingDetails[2]
        self.year = listingDetails[3]

    def vehicle_details(self):
        print(f"Vehicle Type {self.type}")
        print(f"Vehicle Make {self.make}")
        print(f"Vehicle Model {self.model}")
        print(f"Vehicle Manufactur Year {self.year}")
        

class CommentSection():

    def __init__(self):
        self.comments = []

    def add_comment(self):
        name = input("Enter Name:")
        comment = input("Enter Comment:")
        self.comments.append([name, comment])

    def show_comments(self):

        for comment in self.comments:
            print(f'{comment[0]} \n {comment[1]}')

class Listing():

    postid = 0
    def __init__(self, listingDetails):
        self.listingID = Listing.postid  # Assign unique ID
        Listing.postid += 1  # Increment for the next object

        self.seller = listingDetails[0]   
        self.price = listingDetails[5]
        self.location = listingDetails[6]
        self.vehicle = Vehicle(listingDetails[1:5])
        self.commentsection = CommentSection()
        

class App():

    def __init__(self):
        # Entering dummy data
        self.listings = [
                        Listing(['Rameel', 'Car', 'Toyota', 'V8', '2023', 78000000, 'Lahore']),
                        Listing(['ABC', 'Car', 'Toyota', 'Corolla', '2020', 8000000, 'Lahore']),
                        Listing(['XYZ', 'Car', 'Toyota', 'V8', '2023', 75000000, 'Karachi']),
                        Listing(['ZYZ', 'Car', 'Honda', 'Ciciv', '2022', 10000000, 'Lahore']),
                        Listing(['ABC', 'Car', 'Toyota', 'V8', '2021', 73000000, 'Karachi']),
                        Listing(['ZYZ', 'Car', 'Lexus', '570', '2023', 85000000, 'Islamabad']),
                        ]
       

    def creat_listing(self, listingDetails):
        self.listings.append(Listing(listingDetails))

    
    @classmethod
    def show_listings(cls, listings):

        postid = 0
        while True:
            for listing in listings:
                print('---------------------------------------------------------------------')
                print(f"Seller name: {listing.seller}        Listing ID: {listing.listingID}    Post ID {postid}")
                postid += 1

            postid = int(input("Enter the post ID to veiw details or enter -1 to exit:"))
            if postid >=0 and postid < len(listings):
                listings[postid].vehicle.vehicle_details()
                listings[postid].commentsection.show_comments()
                addComment = input("Press A to add comment or any other to exit:")

                if addComment.upper() == 'A':
                    listings[postid].commentsection.add_comment()

            elif postid == -1:
                break
            else:
                print("Invalid input")

    def search_vehicles(self, args):

        result = []
        if len(args) == 1:
            # 1 argument means we are looking for one particular seller listings
            sellerName = args[0].upper()
            for listing in self.listings:
                if sellerName == listing.seller.upper():
                    result.append(listing)

        else:
            # More than 1 arguments means we are applying filters
            # type, make, model, year, minPrice, maxPrice, location
            for listing in self.listings:
                if (args[0] == listing.vehicle.type and 
                    args[1] == listing.vehicle.make and
                    args[2] == listing.vehicle.model and
                    args[3] == listing.vehicle.year and
                    args[6] == listing.location and
                    listing.price >= args[4] and listing.price <= args[5]):
                    result.append(listing)

        return result
    
    @classmethod
    def menu(cls):

        print("Menu")
        print("If you want to list your vehicle PRESS 1")
        print("If you want to search vehicle PRESS 2")
        print("If you want to exit the system PRESS 3")

    @classmethod
    def listing_form(cls):

        print("Please fill out the following details to list your vehicle")
        name = input("Enter your name:")
        type = input("Enter the vehicle type:")
        make = input("Enter the make of the vehicle:")
        model = input("Enter the model of the vehicle:")
        year = input("Enter the year of the vehicle(MM/DD/YYYY):")
        price = int(input("Enter price:"))
        location = input("Enter your location:")

        return [name, type, make, model, year, price, location]
    
    @classmethod
    def filters(cls):

        while True:
            option = 0
            print("If you want to see the listings by a single seller than PRESS 1")
            print("If you want to apply the filters than PRESS 2")
            print("If you want exit than PRESS 3")
            option = int(input("Enter your option:"))
            if option == 1:
                # If user wants to search by seller's name
                name = input("Enter seller's name:")

                return [name]
            elif option == 2:
                # If user wants to apply filters
                print("Please fill out the following filters to search your prefered vehicle")
                type = input("Enter the vehicle type:")
                make = input("Enter the make of the vehicle:")
                model = input("Enter the model of the vehicle:")
                year = input("Enter the year of the vehicle(MM/DD/YYYY):")
                minPrice = int(input("Enter min price:"))
                maxPrice = int(input("Enter max price:"))
                location = input("Enter your location:")

                return [type, make, model, year, minPrice, maxPrice, location]
            elif option == 3:
                return None
            else:
                print("Please enter a valid option")
                

        
    
    def interface(self):

        option = 0

        while True:

            App.menu()

            option = int(input("Enter Your Option:"))
            if option == 1:
                listingDetails = App.listing_form()
                self.creat_listing(listingDetails)
            elif option == 2:
                filters = App.filters()
                
                if filters != None:
                    listings = self.search_vehicles(filters)
                    if len(listings) > 0:
                        App.show_listings(listings)
                    else:
                        print('No record found, try again')
                else:
                    # User choose to exit when asked to apply filters
                    continue
                
                
            elif option == 3:
                print("Exit")
                break
            else:
                print("Invalid Option Selected")

def main():
    app = App()
    app.interface()

if __name__ == '__main__':
    main()