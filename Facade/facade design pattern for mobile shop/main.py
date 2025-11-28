from shop_keeper import ShopKeeper

def main():
    shop_keeper = ShopKeeper()

    while True:
        print("------- Mobile Shop -------")
        print("1. Iphone.")
        print("2. Samsung.")
        print("3. Blackberry.")
        print("4. Exit.")
        choice = int(input("Enter your choice: "))
        
        if choice == 4:
            break
        
        shop_keeper.get_function(choice)
    
if __name__ == "__main__":
    main()