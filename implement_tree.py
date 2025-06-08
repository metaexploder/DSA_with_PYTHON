class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_lvl(self):
        lvl = 0
        p = self.parent
        while p:
            lvl += 1
            p = p.parent

        return lvl

    def print_tree(self):
        spaces = ' ' * self.get_lvl() * 10
        prefix = spaces + "|__" if self.parent else ""
        print(prefix, self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    # child of laptop node
    for child in ["Mac", "Surface", "Thinkpad"]:
        laptop.add_child(TreeNode(child))

    cellphone = TreeNode("Cell Phone")
    for child in ["iPhone", "Google Pixel", "Vivo"]:
        cellphone.add_child(TreeNode(child))

    tv = TreeNode("TV")
    for child in ["Samsung", "LG", "REDMI"]:
        tv.add_child(TreeNode(child))

    for child in [laptop, cellphone, tv]:
        root.add_child(child)

    

    return root



if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()







