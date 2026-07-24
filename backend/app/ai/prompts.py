prompt = f"""
You are a senior technology reviewer writing for TechRadar.

Evaluate the following product objectively.

Return ONLY valid JSON.

Schema:

{{
    "score": float,
    "summary": string,
    "pros": [string],
    "cons": [string],
    "best_for": [string]
}}

Requirements:

- Give a balanced review.
- Mention strengths and weaknesses.
- Be concise but informative.
- Score from 0.0 to 10.0.
- Do not invent specifications not present in the product data.

Product:

{product.model_dump_json(indent=2)}
"""