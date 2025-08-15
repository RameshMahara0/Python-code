contacts = []
email_domain = set()

# Adding contacts
def add_contact(name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})
    domain = email.split("@")[-1]
    email_domain.add(domain)
    print(f"✅ Contact {name} added successfully.")

# Searching existing contacts
def search_contact(keyword):
    results = [c for c in contacts if keyword.lower() in c['name'].lower() or keyword in c['phone']]
    if results:
        print("\n🔎 Searching Results...")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("🚫 Not Found")

# Display all contacts
def display_contacts():
    if not contacts:
        print("Sorry! Contact list is EMPTY")
    else:
        print("\n All Contacts:")
        print("----------------------")
        for num, c in enumerate(contacts, start=1):
            print(f"{num}. {c['name']} || {c['phone']} || {c['email']}")

# Unique email domains
def show_unique_domains():
    print("\n🌐 Unique Email Domains:")
    for domain in email_domain:
        print(f"- {domain}")
# Option for user
while True:
    print("\n==== CONTACT BOOK MANAGER ====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Show Unique Email Domains")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        add_contact(name, phone, email)

    elif choice == "2":
        keyword = input("Enter Name or Phone to Search: ")
        search_contact(keyword)

    elif choice == "3":
        display_contacts()

    elif choice == "4":
        show_unique_domains()

    elif choice == "5":
        print("👋 Exiting Contact Book. Goodbye!")
        break
# Defult result
    else:
        print("❌ Invalid choice! Please try again.")
