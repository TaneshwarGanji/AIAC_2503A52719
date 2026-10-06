"""Social media post moderation prompt examples."""

# a) Zero-shot prompt: instructions without labeled examples.
zero_shot_prompt = """
Classify the post as exactly one of these labels: Acceptable, Offensive, or Spam.
Acceptable means ordinary content that is not abusive or unsolicited promotion.
Offensive means abusive, hateful, threatening, or harassing content.
Spam means unsolicited repetitive advertising, scams, or irrelevant promotion.
Return only a JSON object with keys "label" and "reason".

Post: {post}
""".strip()

# b) One-shot prompt: instructions with one labeled example.
one_shot_prompt = """
Classify a post as Acceptable, Offensive, or Spam. Offensive is abusive,
hateful, threatening, or harassing content. Spam is unsolicited advertising,
scams, or repetitive promotional content. Return only JSON with "label" and
"reason" keys.

Example:
Post: You are worthless and nobody wants you here.
Label: Offensive
Reason: It directly insults and harasses someone.

Classify this post:
Post: {post}
""".strip()

# c) Few-shot prompt: examples illustrate each of the three categories.
few_shot_prompt = """
Choose exactly one label: Acceptable, Offensive, or Spam. Offensive includes
abuse, hate, threats, and harassment. Spam includes unsolicited promotions,
scams, and repetitive advertising. Return only JSON with "label" and
"reason" keys.

Post: I enjoyed the park today; the flowers were lovely.
Label: Acceptable
Reason: This is a harmless personal update.

Post: People like you should be attacked and driven out.
Label: Offensive
Reason: It threatens and targets a group.

Post: Click my link now to claim a guaranteed cash prize!
Label: Spam
Reason: This is an unsolicited promotional message making a suspicious offer.

Post: {post}
""".strip()

# d) Challenges of zero-shot prompting in content moderation.
zero_shot_challenges = [
	"Instructions alone may not make category boundaries clear or consistent.",
	"Sarcasm, slang, reclaimed language, and cultural context can be misread.",
	"A post may fit multiple labels, while the task requires just one.",
	"Ambiguity can cause false positives or allow harmful content to pass.",
	"Language and community standards evolve, requiring updated guidance.",
	"Model judgments can be biased; uncertain cases may need human review.",
]

if __name__ == "__main__":
	print("Zero-shot prompt:\n" + zero_shot_prompt)
	print("\nOne-shot prompt:\n" + one_shot_prompt)
	print("\nFew-shot prompt:\n" + few_shot_prompt)
	print("\nChallenges:")
	for challenge in zero_shot_challenges:
		print("- " + challenge)
