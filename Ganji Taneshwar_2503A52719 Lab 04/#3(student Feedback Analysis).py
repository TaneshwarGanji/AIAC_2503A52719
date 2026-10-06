"""Prompts for classifying student feedback sentiment."""

# a) Zero-shot: classify without examples.
zero_shot_prompt = """Classify the student feedback as exactly Positive, Negative,
or Neutral. Return only the label.

Feedback: {feedback}
Sentiment:"""

# b) One-shot: provide one labeled example.
one_shot_prompt = """Classify the student feedback as Positive, Negative, or
Neutral. Return only the label.

Feedback: "The instructor explains ideas clearly, and I enjoy the course."
Sentiment: Positive

Feedback: {feedback}
Sentiment:"""

# c) Few-shot: provide examples for all three labels.
few_shot_prompt = """Classify the student feedback as Positive, Negative, or
Neutral. Return only the label.

Feedback: "The instructor explains ideas clearly, and I enjoy the course."
Sentiment: Positive

Feedback: "The lectures are confusing, and the assignments are unreasonable."
Sentiment: Negative

Feedback: "The course meets twice a week and uses a required textbook."
Sentiment: Neutral

Feedback: {feedback}
Sentiment:"""

# d) Labeled examples clarify category boundaries and expected output.
accuracy_explanation = (
	"Examples show how praise, criticism, and factual comments map to the labels. "
	"Several varied examples make these distinctions clearer, reducing ambiguity "
	"and helping the model classify feedback more consistently."
)

if __name__ == "__main__":
	print("A) Zero-shot prompt:\n" + zero_shot_prompt)
	print("\nB) One-shot prompt:\n" + one_shot_prompt)
	print("\nC) Few-shot prompt:\n" + few_shot_prompt)
	print("\nD) How examples improve accuracy:\n" + accuracy_explanation)
