import json
from pathlib import Path

from app.schemas.category import Category


class CategoryService:
    def __init__(self):
        self.file_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "categories.json"
        )

    def _load_categories(self) -> list[Category]:
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [Category(**item) for item in data]

    def get_categories(self) -> list[Category]:
        return self._load_categories()

    def get_category(self, category_id: str) -> Category | None:
        categories = self._load_categories()

        for category in categories:
            if category.id == category_id:
                return category

        return None