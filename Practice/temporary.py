print("Welcome to the Shop!\n\n")
output=""
cost=0
item={"apple":35,"banana":18,"orange":26,"chocolate bar":50,"juice":40,"soda":50,"cake":80}
name=list(item.keys())
price=list(item.values())  
print("Currently in stock: ",end='')
for i,j in (item.items()[:-1]):
    print(f"{i}(Rs.{j}), ",end='')
print("\nPick an Item, or Enter to Checkout.")
while True:
    user=input("Choice--> ")
    if user!="":
        if (user.lower() in item):
            print("Item added.\n")
            output+=user +"-"
            for x in name:
                if user==x:
                    num=name.index(x)
                    cost+=price[num]
        else:
            print("No such item. Try again.")
    else:
        break

print(f"Thank you. You have purchased {output[:-1]} at a cost of Rs.{cost}.")