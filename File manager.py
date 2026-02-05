import os

def show_files():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        for file in files:
            print(file)

def create_file():
    name = input("Enter file name: ")
    with open(name, "w") as f:
        print("File created successfully")

def delete_file():
    name = input("Enter file name to delete: ")
    if os.path.exists(name):
        os.remove(name)
        print("File deleted")
    else:
        print("File not found")

def rename_file():
    old = input("Enter old file name: ")
    new = input("Enter new file name: ")
    if os.path.exists(old):
        os.rename(old, new)
        print("File renamed")
    else:
        print("File not found")

while True:
    print("\n--- FILE MANAGER ---")
    print("1. Show files")
    print("2. Create file")
    print("3. Delete file")
    print("4. Rename file")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_files()
    elif choice == "2":
        create_file()
    elif choice == "3":
        delete_file()
    elif choice == "4":
        rename_file()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
