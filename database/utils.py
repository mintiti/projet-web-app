

class CartItem :
    def __init__(self, id, name, quantity, unit_price, product_type):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.product_type = product_type
        self.unit_price = unit_price

    def __str__(self):
        return "CartItem :" + ": " + str(self.__dict__)
    @property
    def total_price(self):
        return self.quantity * self.unit_price

    @property
    def img_url(self):
        return 'https://via.placeholder.com/800'


class Cart:
    def __init__(self):
        self.cart = []

    @property
    def total_price(self):
        S= 0
        for cart_item in self:
            S+= cart_item.total_price
        return S

    def __contains__(self, item):
        for i in self.cart:
            if i.id == item.id:
                return True
        return False

    def __iter__(self):
        return iter(self.cart)

    def __str__(self):
        ret = "Cart : ["
        for cart_item in self.cart:
            ret += str(cart_item)+ " ,"
        return ret + "]"

    def __getitem__(self, item):
        return self.cart[item]

    def append(self, item):
        self.cart.append(item)

    def index(self, item):
        for i in range(len(self.cart)):
            if self.cart[i].id == item.id :
                return i
            
    def add(self, cart_item):
        if cart_item in self:
            index = self.index(cart_item)
            self[index].quantity += cart_item.quantity
        else :
            self.append(cart_item)




if __name__ == '__main__':
    c = CartItem(0, "test", 2, 2.5, 0)
    d = CartItem(1, "test", 2, 2.5, 0)
    print(c.total_price)
    c.quantity += 1
    print(c.total_price)
    print(c.img_url)

    cart = Cart()
    print(cart)
    cart.add(c)
    print(cart)
    cart.add(d)
    print(cart)
    cart.add(c)
    print(cart)
    cart.add(d)
    print(cart)

