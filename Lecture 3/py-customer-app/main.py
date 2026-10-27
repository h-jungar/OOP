from services.customer_service import CustomerService

def main():
    customer_service = CustomerService()

    first_name = input("Ange förnamn: ")
    last_name = input("Ange efternamn: ")
    email = input("Ange email: ")

    customer = customer_service.add_customer(first_name, last_name, email)

    print(f"Kund med id '{customer.id}' skapades.")
    #print("Kund med id" + str(customer.id) + " skapades")

if __name__ == "__main__":
    main()
