from models.grocery_item import GroceryItem

class GroceryItemResult:
    def __init__(self, succeeded: bool, message: str, grocery_item: GroceryItem):
        self.succeeded: bool = succeeded
        self.message: str = message
        self.grocery_item: GroceryItem = grocery_item