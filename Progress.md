A file to help me track my progress

### 2026/01/17
- Made Git repo
- Setup folder structure
- Decided on source (Kaggle Etherium Prices and r/ethfinance)


# Project Goals — eth-reddit-sentiment

## Overall Goal
Explore the relationship between Reddit social sentiment and Ethereum (ETH) price movements while learning core data science and machine learning principles.

---

## Step 1 — Data Collection
- [X] Decide subreddits to track (r/ethereum, r/ethfinance, r/cryptocurrency)
- [ ] Collect Reddit posts: timestamp, title, text, score, comment counts
- [ ] Collect ETH historical price data
- [ ] Save raw datasets in `data/raw/`

---

## Step 2 — Data Cleaning & Preprocessing
- [ ] Standardize timestamps to UTC
- [ ] Remove duplicates and irrelevant posts
- [ ] Clean text (lowercase, remove URLs/emojis/HTML artifacts)
- [ ] Aggregate posts to match ETH price intervals (hourly/daily)

---

## Step 3 — Sentiment Analysis
- [ ] Apply VADER sentiment scoring
- [ ] Optionally apply FinBERT for domain-specific sentiment
- [ ] Aggregate sentiment per time window (mean, weighted, post count)
- [ ] Explore distributions and identify outliers

---

## Step 4 — Feature Engineering
- [ ] Merge sentiment features with ETH price data
- [ ] Create derived features:
  - Price returns
  - Price direction (up/down)
  - Volatility (rolling std or high-low)
  - Lagged sentiment
- [ ] Explore correlations between sentiment and price

---

## Step 5 — Exploratory Data Analysis (EDA)
- [ ] Plot ETH price vs sentiment over time
- [ ] Visualize rolling correlations or trends
- [ ] Conduct event studies around sentiment spikes
- [ ] Check distributions and scatter plots

---

## Step 6 — Modeling
- [ ] Define predictive task (regression or classification)
- [ ] Train baseline models (Linear/Logistic Regression)
- [ ] Train tree-based models (Random Forest, XGBoost)
- [ ] Evaluate using metrics (R², MSE, accuracy, F1-score)
- [ ] Experiment with lagged features and hyperparameters

---

## Step 7 — Visualization & Reporting
- [ ] Plot predicted vs actual returns/directions
- [ ] Create heatmaps for correlations or rolling sentiment
- [ ] Save visualizations to `reports/`
- [ ] Update README.md with methodology and insights

---

## Step 8 — Optional Extensions
- [ ] Include Reddit comments in sentiment aggregation
- [ ] Compare multiple subreddits or combine with news sentiment
- [ ] Use embeddings or transformer-based models for deeper NLP
- [ ] Explore advanced time series models (LSTM/GRU)
- [ ] Run educational backtesting of sentiment-based strategies
