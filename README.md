# CodeAlpha Sentiment Analysis

## Project Overview
This project performs sentiment analysis on customer reviews using Python. It classifies each review into three categories: Positive, Negative, or Neutral, based on predefined positive and negative keywords.

## Objectives
- Analyze customer reviews.
- Identify positive, negative, and neutral sentiments.
- Display sentiment analysis results in the terminal.
- Save the results in a CSV file.
- Generate a bar chart to visualize sentiment distribution.

## Technologies Used
- **Python** – Main programming language
- **Pandas** – Data handling and CSV file creation
- **Matplotlib** – Data visualization and graph generation
- **VS Code** – Development environment

## Project Features
1. Sentiment classification of customer reviews.
2. Keyword-based sentiment detection.
3. Display of review-wise results.
4. Export of results to `sentiment_results.csv`.
5. Generation of `sentiment_graph.png`.
6. Summary of positive, negative, and neutral reviews.

## Project Structure

```text
CodeAlpha_SentimentAnalysis/
│
├── sentiment_analysis.py
├── sentiment_results.csv
├── sentiment_graph.png
└── README.md
```

## Installation and Setup

### 1. Clone the Repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd CodeAlpha_SentimentAnalysis
```

### 2. Create a Virtual Environment
```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment
For macOS and Linux:
```bash
source .venv/bin/activate
```

### 4. Install Required Libraries
```bash
python -m pip install pandas matplotlib
```

### 5. Run the Project
```bash
python sentiment_analysis.py
```

## Output Files

- **sentiment_results.csv:** Contains customer reviews and their predicted sentiment labels.
- **sentiment_graph.png:** Displays a bar chart showing the number of positive, negative, and neutral reviews.

## Methodology
The program converts each review to lowercase and checks it against predefined positive and negative keywords. It counts matching keywords and assigns a sentiment label based on the comparison. If neither category has a higher count, the review is classified as Neutral.

## Limitations
This project uses a simple keyword-based approach. It may not correctly understand sarcasm, context, or negation. It is a beginner-level implementation and does not use a trained machine learning model.

## Future Improvements
- Use a machine learning model for sentiment classification.
- Analyze reviews from larger datasets.
- Add a graphical user interface.
- Support multiple languages.
- Create an interactive sentiment analysis dashboard.

## Conclusion
This project demonstrates the basic concepts of text processing, sentiment classification, CSV data handling, and data visualization using Python.

## Author
Anshul Tiwari

## Internship
CodeAlpha Internship Project
