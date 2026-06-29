# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
I used the rule based model and also briefly compared it with the ML model.

**Intended purpose:**  
The model is trying to classify short text messages into moods like positive, negative, neutral, or mixed.

**How it works (brief):**  
The rule based model preprocesses text by lowercasing and tokenizing, then assigns a score by adding points for positive words and subtracting for negative words. It also handles negation and simple emojis before mapping the score to a label.  
The ML model uses a bag of words approach (CountVectorizer) and learns patterns from labeled examples during training.


## 2. Data

**Dataset description:**  
There are 14 posts total in `SAMPLE_POSTS`. The original dataset had 6 posts, and I added 8 more to make the data more realistic.

**Labeling process:**  
I labeled posts based on overall tone instead of just individual words. Some posts were harder to label. For example, “I mean it could be worse I guess” could be neutral or slightly negative, but I labeled it as neutral since it doesn’t show strong emotion.

**Important characteristics of your dataset:**  
- Contains slang or emojis  
- Includes mixed feelings  
- Contains short or ambiguous messages  
- Includes informal language like “lowkey” and “highkey”  

**Possible issues with the dataset:**  
The dataset is small and somewhat subjective. Some labels could be interpreted differently by others, and there may be imbalance between categories.


## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
- Positive words add +1 to the score  
- Negative words subtract -1 from the score  
- Negation handling was added using words like “not,” “never,” “no,” and “don’t” to flip the meaning of the next word  
- Emojis like 😂 increase the score and 🥲 decrease the score  
- Score ≥ 2 → positive  
- Score ≤ -2 → negative  
- Score of ±1 → mixed  
- Score of 0 → neutral  

**Strengths of this approach:**  
The model is simple and consistent. It works well on clear sentences like “I love this” or “this is terrible.” The negation handling improves accuracy on phrases like “not happy” or “don’t love this.”

**Weaknesses of this approach:**  
The model struggles with sarcasm and subtle meaning. For example, “I just love when everything goes wrong” would likely be classified as positive because of the word “love.” It also struggles with vague phrases like “some type of way” or language that is not in the word lists.


## 4. How the ML Model Works (if used)

**Features used:**  
Bag of words using CountVectorizer.

**Training data:**  
The model was trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Because the dataset is small, the model is very sensitive to the examples and labels. Changing or adding a few posts can noticeably change predictions.

**Strengths and weaknesses:**  
The ML model can pick up patterns beyond single words and sometimes handles unfamiliar phrasing better. However, it can overfit easily and may rely too heavily on certain words instead of actual meaning.


## 5. Evaluation

**How you evaluated the model:**  
I evaluated the model by running predictions on the labeled dataset and comparing them to the true labels.

**Examples of correct predictions:**  
“I love this class so much” → positive. The word “love” correctly increases the score.  
“Today was a terrible day” → negative. The word “terrible” strongly signals negativity.  
“So excited for the weekend” → positive. The word “excited” increases the score.

**Examples of incorrect predictions:**  
“I just love when everything goes wrong” → predicted positive. The model focuses on “love” and misses sarcasm.  
“This weather got me feeling some type of way” → predicted neutral or mixed. The phrase is unclear and not in the word list.  
“I mean it could be worse I guess” → predicted neutral, but could also be interpreted as slightly negative.

If both models were compared, the ML model sometimes handled unfamiliar phrases better, but it also made mistakes when it relied too heavily on certain words.


## 6. Limitations

The dataset is small and does not cover many types of language. The model does not generalize well to longer or more complex text. It cannot reliably detect sarcasm and depends heavily on the predefined word lists.


## 7. Ethical Considerations

Misclassifying mood could be harmful in real situations, especially if someone is expressing distress. The model may also misinterpret language depending on cultural or social context. There are also privacy concerns if personal messages are analyzed without consent.


## 8. Ideas for Improvement

- Add more labeled data  
- Expand vocabulary to include more slang and expressions  
- Improve preprocessing for emojis and informal language  
- Use TF-IDF instead of CountVectorizer  
- Improve sarcasm handling  
- Add a separate test set instead of evaluating on training data  
- Explore more advanced models like neural networks or transformers  