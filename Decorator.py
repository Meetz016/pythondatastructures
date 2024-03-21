class A:
    def demo(self):
        return "demo check"

    def display(self):
        print(self.demo())


class B(A):
    def check(self):
        return "B Check"


A().display()
B().display()
