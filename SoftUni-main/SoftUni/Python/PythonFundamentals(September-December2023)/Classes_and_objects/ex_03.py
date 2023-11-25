class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []
    def __repr__(self):
        return_str = f"Items in the {self.name} catalogue:\n"
        return_str += "\n".join(sorted(self.products))
        return return_str
    def add_product(self, product_name: str):
        self.products.append(product_name)
    def get_by_letter(self, letter):
        l = []
        for item in self.products:
            if item.startswith(letter):
                l.append(item)
        return l

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)