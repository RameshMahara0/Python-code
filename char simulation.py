

messages = []   
bad_words = {"stupid", "idiot", "badword", "donkey"} 
user_messages = {}  
unique_users = set()  


def filter_message(msg):
    for word in bad_words:
        if word.lower() in msg.lower():
            msg = msg.replace(word, "***")  
    return msg


def send_message(user, msg):
    msg = filter_message(msg)
    messages.append(f"{user}: {msg}") 
    unique_users.add(user) 

    if user not in user_messages:
        user_messages[user] = []
    user_messages[user].append(msg)


def show_chat():
    print("\n📜 Chat History:")
    for m in messages:
        print(m)


def show_users():
    print("\n👥 Users in Chat:")
    for u in unique_users:
        print(f"- {u}")


def show_user_messages(user):
    if user in user_messages:
        print(f"\n💬 Messages by {user}:")
        for m in user_messages[user]:
            print(f"- {m}")
    else:
        print(f"❌ No messages from {user}")



while True:
    print("\n==== SIMPLE CHAT SIMULATOR ====")
    print("1. Send Message")
    print("2. Show Chat History")
    print("3. Show Users")
    print("4. Show User's Messages")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user = input("Enter username: ")
        msg = input("Enter your message: ")
        send_message(user, msg)

    elif choice == "2":
        show_chat()

    elif choice == "3":
        show_users()

    elif choice == "4":
        user = input("Enter username: ")
        show_user_messages(user)

    elif choice == "5":
        print("👋 Exiting chat. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Try again.")
