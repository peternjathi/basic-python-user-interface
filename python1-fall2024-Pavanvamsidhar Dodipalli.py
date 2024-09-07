def main():
    names = []
    
    # Use a while loop to collect names
    while True:
        name = input("Enter a name or type 'done' to stop: ")
        if name.lower() == 'done':
            break
        names.append(name)
    
    # Ask the user to select a print method
    print("How would you like to print the list?")
    print("1. Lowercase")
    print("2. UPPERCASE")
    print("3. Title Case")
    choice = input("Enter the number of your choice: ")
    
    # Print the list based on the user's preference
    if choice == '1':
        formatted_names = [name.lower() for name in names]
    elif choice == '2':
        formatted_names = [name.upper() for name in names]
    elif choice == '3':
        formatted_names = [name.title() for name in names]
    else:
        print("Invalid choice. Printing in original format.")
        formatted_names = names
    
    # Print the names in the specified format
    print("\nHere is the list of names:")
    for i, name in enumerate(formatted_names, start=1):
        print(f"    {i}. {name}")
    
    # Clear the list and end
    names.clear()
    print("\nThe list has been cleared.")

if __name__ == "__main__":
    main()
