"""Compare zero-, one-, and few-shot intent classification prompts.

Set OPENAI_API_KEY (and optionally OPENAI_MODEL) to run the evaluation.
"""

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


INTENTS = [
	"Account Issue",
	"Order Status",
	"Product Inquiry",
	"General Question",
]

# Six labeled examples used as the common test set for all three techniques.
SAMPLE_DATA = [
	{"query": "I can't log in to my account.", "intent": "Account Issue"},
	{"query": "Please reset my password.", "intent": "Account Issue"},
	{"query": "Where is my package?", "intent": "Order Status"},
	{"query": "Has my order shipped yet?", "intent": "Order Status"},
	{"query": "Does this jacket come in blue?", "intent": "Product Inquiry"},
	{"query": "What are your customer service hours?", "intent": "General Question"},
]

# Demonstrations are deliberately separate from the test queries.
DEMONSTRATIONS = [
	("I need to update my email address.", "Account Issue"),
	("Can you tell me when my parcel will arrive?", "Order Status"),
	("Is this phone available with more storage?", "Product Inquiry"),
	("Do you deliver on public holidays?", "General Question"),
]


def make_prompt(technique, query):
	"""Build an instruction prompt with zero, one, or four labeled examples."""
	prompt = (
		"Classify the customer query into exactly one of these intents: "
		f"{', '.join(INTENTS)}. Return only the exact intent name.\n"
	)
	if technique == "one-shot":
		examples = DEMONSTRATIONS[:1]
	elif technique == "few-shot":
		examples = DEMONSTRATIONS
	elif technique == "zero-shot":
		examples = []
	else:
		raise ValueError("Technique must be zero-shot, one-shot, or few-shot")

	if examples:
		prompt += "\nExamples:\n"
		for example_query, intent in examples:
			prompt += f"Query: {example_query}\nIntent: {intent}\n"
	return prompt + f"\nQuery: {query}\nIntent:"


def classify_with_openai(query, technique):
	"""Send one prompt to the OpenAI chat completions API using stdlib only."""
	api_key = os.environ.get("OPENAI_API_KEY")
	if not api_key:
		raise RuntimeError("Set OPENAI_API_KEY to run the live evaluation.")

	payload = {
		"model": os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
		"temperature": 0,
		"messages": [{"role": "user", "content": make_prompt(technique, query)}],
	}
	request = Request(
		"https://api.openai.com/v1/chat/completions",
		data=json.dumps(payload).encode("utf-8"),
		headers={
			"Authorization": f"Bearer {api_key}",
			"Content-Type": "application/json",
		},
		method="POST",
	)
	try:
		with urlopen(request, timeout=60) as response:
			result = json.loads(response.read().decode("utf-8"))
	except (HTTPError, URLError) as error:
		raise RuntimeError(f"API request failed: {error}") from error

	prediction = result["choices"][0]["message"]["content"].strip()
	# Normalize harmless punctuation/casing while preserving invalid answers.
	return next((label for label in INTENTS if prediction.lower() == label.lower()), prediction)


def evaluate():
	"""Run every prompting technique on the same six labeled test queries."""
	techniques = ("zero-shot", "one-shot", "few-shot")
	for row in SAMPLE_DATA:
		print(f"{row['query']} -> {row['intent']}")

	totals = {}
	for technique in techniques:
		correct = 0
		print(f"\n{technique.title()} results:")
		for row in SAMPLE_DATA:
			predicted = classify_with_openai(row["query"], technique)
			is_correct = predicted == row["intent"]
			correct += is_correct
			print(
				f"  Expected: {row['intent']:<18} Predicted: {predicted} "
				f"{'✓' if is_correct else '✗'}"
			)
		totals[technique] = correct
		print(f"Accuracy: {correct}/{len(SAMPLE_DATA)} ({correct / len(SAMPLE_DATA):.1%})")

	print("\nEvaluation comparison:")
	for technique in techniques:
		print(f"  {technique}: {totals[technique]}/{len(SAMPLE_DATA)} correct")
	print(
		"Differences are measured by accuracy on identical queries. "
		"Zero-shot uses instructions only; one-shot adds one example; "
		"few-shot adds four examples. Results depend on the selected model."
	)


if __name__ == "__main__":
	evaluate()
