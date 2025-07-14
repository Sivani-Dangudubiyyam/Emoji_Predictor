import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# training data
data = {
    "text": [
        "I am so happy", "This is wonderful", "I love you", "I am sad",
        "This is the worst", "I hate everything", "You are amazing",
        "I'm angry", "Feeling joyful", "Life is tough", "You make me laugh",
        "I’m heartbroken", "Let's party", "I am crying", "Such fun!"
    ],
    "emoji": [
        "😊", "😊", "❤️", "😢", "😠", "😡", "😍", "😡", "😁", "😢", "😂", "💔", "🎉", "😭", "🎉"
    ]
}

df = pd.DataFrame(data)

# ML pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(df['text'], df['emoji'])

# Game loop
print("🎮 Emoji Prediction Game!")
print("Type a sentence and the AI will predict the emoji.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    prediction = model.predict([user_input])[0]
    print(f"🤖 Emoji: {prediction}\n")
