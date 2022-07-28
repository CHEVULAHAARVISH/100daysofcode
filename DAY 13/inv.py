class inventory:
    def __init__(self):
        self.inventory =dict()
        self.item_name=""
        self.quantity=0
    def store(self,n):
      
        if 1<=n<=100:
            for i in range(n):
                item_name,item_quantity=input().split()
                if 1<=int(item_quantity)<=100:
                    self.inventory[item_name.upper()]=int(item_quantity)
                    self.item_name=item_name
                    self.quantity=int(item_quantity)

    def display_inventory(self):
        #print(self.inventory)
        print("Total Items in Inventory: {}".format(sum(self.inventory.values())))

    def add_item(self,item_name,quantity):
        existing_inventory=self.inventory.keys()
        if item_name.upper() in existing_inventory:
            self.inventory.update({item_name.upper():int(quantity)})
            print("UPDATED Item {}".format(self.item_name))
        else:
            self.inventory[item_name.upper()]=int(quantity)
            print("ADDED Item {}".format(item_name))

    def delete_item(self, item_name,quantity):
        existing_inventory=self.inventory.keys()
        self.item_name=item_name
        for k,v in self.inventory.items():
               if item_name.upper()==k:
                   existing_quantity=v
        if item_name.upper() in existing_inventory:
            if existing_quantity<int(quantity):
                print ("Item {} could not be DELETED".format(self.item_name))
            else:
                quant=int(quantity)
                existing_quantity-=quant
                self.inventory.update({item_name.upper():existing_quantity})
                print("DELETED Item {}".format(self.item_name))
        else:
            print("{} does not exist".format(self.item_name))



if __name__=='__main__':
    try :

        mart= inventory()
        test_case=int(input())
        test_caselist=[]
        operations_list=[]
        if 1<=test_case<26:
            for i in range(test_case):
                initial_addition=int(input())
                if 1<=initial_addition<101:
                    mart.store(initial_addition)
                    minimum_operation=int(input())
                    if 1<=minimum_operation<101:
                        for i in range(minimum_operation):
                            operation,item_name,quantity=input().split()

                            operations_list.append([operation,item_name,quantity])
                        test_caselist.append(operations_list)
                        #print(test_caselist)
                    for i in range(len(test_caselist)):
                        operation,item_name,quantity=test_caselist[i][i][0],operations_list[i][1],operations_list[i][2]
                        #print(operation)
                        if operation.upper()=='ADD':
                            mart.add_item(item_name,quantity)
                        elif operation.upper()=='DELETE':
                            mart.delete_item(item_name,quantity)

                mart.display_inventory()
    except EOFError as e:
        pass

    
