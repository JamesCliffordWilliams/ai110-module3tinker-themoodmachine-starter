"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",

    # --- New posts ---
    "lowkey had a rough day but we move",
    "this weather got me feeling some type of way",
    "I mean it could be worse I guess",
    "lol that was actually kinda fun 😂",
    "not gonna lie I’m over it already",
    "why does everything feel off today 🥲",
    "just finished and I don’t even know how to feel",
    "highkey tired but still gotta get this done",
]

TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"

    # --- Labels for new posts ---
    "mixed",     # "lowkey had a rough day but we move"
    "mixed",     # "this weather got me feeling some type of way"
    "neutral",   # "I mean it could be worse I guess"
    "positive",  # "lol that was actually kinda fun 😂"
    "negative",  # "not gonna lie I’m over it already"
    "negative",  # "why does everything feel off today 🥲"
    "mixed",     # "just finished and I don’t even know how to feel"
    "mixed",     # "highkey tired but still gotta get this done"
]

# sanity check (optional but helpful)
assert len(SAMPLE_POSTS) == len(TRUE_LABELS)