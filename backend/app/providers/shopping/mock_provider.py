from app.schemas.product import Product


class MockShoppingProvider:

    def search_products(self, category: str) -> list[Product]:

        if category == "tablets":

            return [

                Product(
                    id="1",
                    title="Samsung Galaxy Tab S10",
                    brand="Samsung",
                    category="tablets",
                    price=499,
                    currency="EUR",
                    rating=4.8,
                    review_count=2541,
                    image="https://placehold.co/300x300",
                    store="Amazon",
                    url="#"
                ),

                Product(
                    id="2",
                    title="Apple iPad Air",
                    brand="Apple",
                    category="tablets",
                    price=699,
                    currency="EUR",
                    rating=4.9,
                    review_count=4102,
                    image="https://placehold.co/300x300",
                    store="Amazon",
                    url="#"
                ),

                Product(
                    id="3",
                    title="Lenovo Tab M11",
                    brand="Lenovo",
                    category="tablets",
                    price=249,
                    currency="EUR",
                    rating=4.5,
                    review_count=865,
                    image="https://placehold.co/300x300",
                    store="Amazon",
                    url="#"
                )

            ]

        return []