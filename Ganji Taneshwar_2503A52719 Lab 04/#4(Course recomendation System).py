"""Prompt templates for a course recommendation system."""

# a) Zero-shot prompt: classify a learner without examples.
zero_shot_prompt = """
Classify the learner query as Beginner, Intermediate, or Advanced.
Beginner: asks about fundamentals and assumes little prior knowledge.
Intermediate: applies foundational knowledge to practical or connected topics.
Advanced: concerns specialized concepts or complex techniques.
Return only the level name. If uncertain, select the closest level.

Learner query: {query}
Level:
""".strip()

# b) One-shot prompt: use one labeled query as a pattern.
one_shot_prompt = """
Classify learner queries as Beginner, Intermediate, or Advanced. Return only
the level name.

Example:
Learner query: What is a variable in Python?
Level: Beginner

Learner query: {query}
Level:
""".strip()

# c) Few-shot prompt: use multiple labeled queries as examples.
few_shot_prompt = """
Classify learner queries as Beginner, Intermediate, or Advanced. Return only
the level name.

Examples:
Learner query: What is a variable in Python?
Level: Beginner

Learner query: How can I use a Python dictionary to count word frequencies?
Level: Intermediate

Learner query: How can I profile and optimize an asynchronous event loop under
high concurrency?
Level: Advanced

Learner query: {query}
Level:
""".strip()

# d) Multiple examples show the intended labels and distinctions between
# levels. Representative, balanced examples make classifications more
# consistent, helping match learners with appropriately challenging courses.
# Poor or unbalanced examples may skew the results.
few_shot_improvement = (
	"Few-shot prompting illustrates the expected labels and decision boundaries. "
	"With representative, balanced examples, it can classify queries more "
	"consistently and improve the fit between a learner's apparent knowledge "
	"and recommended course level."
)
