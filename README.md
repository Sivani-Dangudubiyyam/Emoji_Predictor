# 🤖 Emoji Prediction Game 🎮

A simple and fun Machine Learning game built with Python, where the AI predicts the most appropriate emoji for your input sentence.

---

## ✨ Features

- Predicts emojis like 😊, 😢, 😡, ❤️, 🎉 based on sentence meaning
- Trained on small custom dataset using NLP techniques
- Command-line interactive game
- Uses Naive Bayes and Bag-of-Words for text classification

---

## 📂 Project Structure

```

emoji_predictor.py      # Main script to run the game

````

---

## 🔧 Installation

1. Clone this repository or copy the code.
2. Install dependencies:

```bash
pip install scikit-learn
````

3. Run the game:

```bash
python emoji_predictor.py
```

---

## 🧠 How It Works

* Text inputs are vectorized using `CountVectorizer`
* A Naive Bayes classifier (`MultinomialNB`) is trained on a small dataset
* The model predicts the most likely emoji based on learned patterns

---

## 🎯 Example

```
You: I am so happy
🤖 Emoji: 😊

You: I love you
🤖 Emoji: ❤️

You: I’m crying
🤖 Emoji: 😢
```




