# shopping list manager
# does not ignore case

shoplist=[]
while True:
    print("Menu Options", "1.Add Item", "2.Remove Item", "3.View List", "4.Sort List", "5.Quit", sep="\n")
    op = int(input("Choose MENU Option: "))

    if op==1:
        a=input("Enter item to be added: ").strip()
        if a.lower() in [x.lower() for x in shoplist]: print("Item already in list")
        else:
            shoplist.append(a)
            print("Item added!")

    elif op==2:
        r=input("Enter item to be removed: ")
        for x in shoplist:
            if x.lower() == r.lower():
                shoplist.remove(r)
                print("Item removed!")
            else: print("Item not in list")

    elif op==3:
        print("Shopping List:")
        for number, item in enumerate(shoplist, start=1):
                print(f"{number}. {item}")

    elif op==4:
        print("Shopping List:")
        sortlist=sorted(shoplist)
        for number, item in enumerate(sortlist, start=1):
            print(f"{number}. {item}")

    elif op==5:
        print("Exiting Menu")
        break

    else: print("Invalid option, please choose 1-5")




