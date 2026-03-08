class Product:
    __name: str
    __code: int
    __guantity: int
    __price: float

    def __init__(self, name: str, code: int, guantity: int, price:float) -> None:
        if code < 0:
            code = 0
        
        if guantity < 0:
            guantity = 0

        if price <= 0:
            price = 1.00

        self.__name = name
        self.__code = code
        self.__guantity = guantity
        self.__price = price
    
    def get_info(self) -> str:
        return f"Name: {self.__name}, Code: {self.__code}, Quantity: {self.__guantity}, Price: {self.__price}"
    
    def get_code(self) -> int:
        return self.__code
    
    def update_guantity(self, guantity: int) -> None:
        if guantity > 0:
            self.__guantity = guantity
        else:
            print("Ошибка. Значение должно быть не меньше 0")
    
    def update_price(self, price: int) -> None:
        if price > 0:
            self.__price = price
        else:
            print("Ошибка. Значение должно быть не меньше 0")


class Warehouse:
    __products: list[Product]

    def __init__(self) -> None:
        self.__products = []
    
    def get_product_by_code(self, code: int) -> Product:
        for i in range(len(self.__products)):
            if self.__products[i-1].get_code() == code:
                return self.__products[i-1]

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product_by_code(self, code: int) -> None:
        self.__products.remove(self.get_product_by_code(code))

    def print_all_products(self) -> None:
        for product in self.__products:
            print(product.get_info())