RECOMMENDATION_PROMPT = """
You are an expert technology reviewer.

Return ONLY valid JSON.

{
  "score": number,
  "summary": string,
  "pros": [string],
  "cons": [string],
  "best_for": [string]
}
"""