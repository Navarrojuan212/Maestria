```python
class MyClass:
    def __init__(self.value):
        self.value = value

    def method1(self):
        #logica del metodo
        return f"Method 1 executed with value: {self.value}"

    def method2(self):
        #logica del metodo
        return f"Method 2 executed with value: {self.value}"

    def __call__(self, new_value):
        #logica del metodo
        self.value = new_value
        return f"Object updated with new_value: {self.value}"

```