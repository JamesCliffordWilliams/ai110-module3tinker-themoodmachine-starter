# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.
"""

from typing import List, Optional
import re

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Clean text and split into tokens.
        """

        text = text.lower().strip()

        # remove punctuation but keep emojis
        text = re.sub(r"[^\w\s😂🥲:()']", "", text)

        tokens = text.split()

        # print tokens so you can verify behavior
        print(f"Tokens: {tokens}")

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric mood score.
        """

        tokens = self.preprocess(text)
        score = 0

        # NEW: expanded negation handling
        NEGATIONS = {"not", "no", "never", "dont", "don't", "cant", "can't"}

        i = 0
        while i < len(tokens):
            token = tokens[i]

            # handle negation (UPDATED)
            if token in NEGATIONS and i + 1 < len(tokens):
                next_token = tokens[i + 1]

                if next_token in self.positive_words:
                    score -= 1
                    i += 2
                    continue
                elif next_token in self.negative_words:
                    score += 1
                    i += 2
                    continue

            # normal scoring
            if token in self.positive_words:
                score += 1
            elif token in self.negative_words:
                score -= 1

            # emoji signals
            if token in ["😂", ":)"]:
                score += 1
            elif token in ["🥲", ":("]:
                score -= 1

            i += 1

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Convert score to label.
        """

        score = self.score_text(text)

        if score >= 2:
            return "positive"
        elif score <= -2:
            return "negative"
        elif score == 1 or score == -1:
            return "mixed"
        else:
            return "neutral"

    # ---------------------------------------------------------------------
    # Explanation
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        tokens = self.preprocess(text)

        positive_hits = []
        negative_hits = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )