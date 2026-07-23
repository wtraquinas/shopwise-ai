# shopwise-ai
Shopping Advisor

<br>

---

Sprint 1 - Architecture
Frontend (React)

↓

API

↓

Business Logic

↓

Providers

↓

External APIs

The React app never knows whether products came from mock data, SerpAPI, Rainforest, or another provider.

Backend Structure

This is the structure I recommend from day one.

backend/

app/

│
├── api/
│     categories.py
│     products.py
│     recommendations.py
│
├── services/
│     category_service.py
│     product_service.py
│
├── providers/
│     shopping/
│          base.py
│          mock_provider.py
│          serpapi_provider.py
│
├── schemas/
│     category.py
│     product.py
│
├── data/
│     categories.json
│
├── config.py
│
└── main.py

Notice we already have providers/.

Even though SerpAPI won't be implemented immediately, the architecture already supports it.

Providers

This is probably the most important design decision.

Instead of

Products API

↓

SerpAPI

we'll have

Products API

↓

Product Service

↓

Shopping Provider

↓

Mock Provider

or

SerpAPI

or

Rainforest

This lets us switch providers without changing the API.

<br>

---

Category Flow
GET /api/categories

↓

CategoryService

↓

categories.json

Very simple.

Product Flow
GET /api/products?category=tablets

↓

ProductService

↓

ShoppingProvider

↓

MockProvider

↓

Products

Later

MockProvider

becomes

SerpAPIProvider

No frontend changes.

Schemas

Instead of returning random dictionaries, every endpoint returns a typed model.

Category
Category

id

title

description

icon

search
Product
Product

id

title

brand

category

price

currency

rating

review_count

image

store

url

Everything in the application uses this model.

Why this matters

Imagine later using Rainforest.

Rainforest returns

{
    "product_title": "...",
    "stars": 4.8,
    "current_price": ...
}

SerpAPI returns

{
    "title": "...",
    "rating": 4.8,
    "price": ...
}

We normalize both into

Product(...)

React never notices.

Product Cards

Every card always receives

Product

Nothing else.

That keeps the frontend very clean.

Recommendation Flow (Sprint 2)
Products

↓

OpenAI

↓

Recommendation

↓

Frontend

Notice GPT never calls SerpAPI.

GPT only receives

Product

objects.

Prompt Example

Instead of giving GPT raw JSON from SerpAPI,

we'll provide a normalized list:

Available products:

Samsung Galaxy Tab S10
Price: €499
Rating: 4.8
Reviews: 2134

Apple iPad Air
Price: €699
Rating: 4.9
Reviews: 6245

Lenovo Tab M11
Price: €249
Rating: 4.5
Reviews: 874

Prompt

Recommend the best product for a general consumer.

Mention:

Best Overall
Best Budget
Best Premium
Explain your reasoning.

Much cleaner.

Configuration

Eventually

.env

will contain

OPENAI_API_KEY=

SERPAPI_API_KEY=

SHOPPING_PROVIDER=mock

OPENAI_MODEL=gpt-5.5

Changing

SHOPPING_PROVIDER=mock

to

SHOPPING_PROVIDER=serpapi

switches providers.

No code changes.

Development Roadmap
Sprint 1

✅ Categories

✅ Mock products

✅ React pages

Sprint 2

Live shopping API

Sprint 3

OpenAI recommendations

Sprint 4

AI summaries

Sprint 5

Comparison page

Sprint 6

Shopping Assistant