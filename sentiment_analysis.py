import os
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------
# 1. Sample reviews
# ----------------------------------

reviews = [
    "This product is amazing and I love it",
    "The service was very good",
    "I am happy with this purchase",
    "This product is terrible",
    "Very bad quality and disappointing",
    "I hate this product",
    "The product is okay",
    "It is an average experience",
    "The service was normal"
]

# ----------------------------------
# 2. Sentiment keywords
# ----------------------------------

positive_words = [
    "amazing", "love", "good", "happy", "excellent",
    "great", "awesome", "best", "wonderful", "satisfied"
]

negative_words = [
    "terrible", "bad", "disappointing", "hate",
    "poor", "worst", "awful", "broken", "useless"
]

# ----------------------------------
# 3. Sentiment analysis function
# ----------------------------------

def analyze_sentiment(review):
    words = review.lower().split()

    positive_count = sum(
        1 for word in words
        if word.strip(".,!?") in positive_words
    )

    negative_count = sum(
        1 for word in words
        if word.strip(".,!?") in negative_words
    )

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

# ----------------------------------
# 4. Analyze all reviews
# ----------------------------------

results = []

for review in reviews:
    sentiment = analyze_sentiment(review)

    results.append({
        "Review": review,
        "Sentiment": sentiment
    })

# ----------------------------------
# 5. Display results
# ----------------------------------

print("\nSENTIMENT ANALYSIS RESULTS")
print("=" * 60)

for result in results:
    print("Review:", result["Review"])
    print("Sentiment:", result["Sentiment"])
    print("-" * 60)

# ----------------------------------
# 6. Save results to CSV
# ----------------------------------

df = pd.DataFrame(results)
df.to_csv("sentiment_results.csv", index=False)

print("\nResults saved to sentiment_results.csv")

# ----------------------------------
# 7. Count sentiments
# ----------------------------------

sentiment_counts = df["Sentiment"].value_counts()

print("\nSENTIMENT SUMMARY")
print(sentiment_counts)

# ----------------------------------
# 8. Generate bar chart
# ----------------------------------

sentiment_order = ["Positive", "Negative", "Neutral"]

sentiment_counts = (
    df["Sentiment"]
    .value_counts()
    .reindex(sentiment_order, fill_value=0)
)

plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind="bar")

plt.title("Sentiment Analysis of Customer Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("sentiment_graph.png")
print("\nGraph saved to sentiment_graph.png")

# Save graph in the same folder as this Python file
folder_path = os.path.dirname(os.path.abspath(__file__))
graph_path = os.path.join(folder_path, "sentiment_graph.png")

plt.savefig(graph_path, dpi=300, bbox_inches="tight")
print("\nGraph saved at:", graph_path)

plt.show()
plt.close()