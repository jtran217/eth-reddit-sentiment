
# ETH Reddit Sentiment & Price Analysis

## Project Overview
This project investigates whether Reddit sentiment affects Ethereum (ETH) price movements. The main goal was to answer the question: **Does Reddit sentiment predict or reflect ETH price?** but also solidify my skills with pandas and matplotlib.

## Data Sources
- **ETH Price Data:** Kaggle Ethereum price dataset
- **Reddit Sentiment Data:** Kaggle Ethereum Reddit posts dataset

## Process & Methods
- Data cleaning and preprocessing
- Feature engineering (lagged sentiment)
- Exploratory data analysis (EDA) and visualization
- Correlation and lag analysis to test for leading/lagging relationships
- Event-based exploration: linking extreme sentiment days to real-world news

## Tools & Libraries
- Python
- pandas
- matplotlib
- scikit-learn

## Key Findings
- **Correlation:** There is a moderate negative correlation (-0.41) between daily Reddit sentiment and ETH closing price, meaning they tend to move in opposite directions on the same day.
- **Lag Analysis:** Shifting sentiment forward or backward in time does not increase the correlation, indicating that sentiment does not predict future price changes, nor does price predict future sentiment. There is no evidence of a leading or lagging relationship.
- **Extreme Sentiment Days:** After days with both extremely positive and extremely negative sentiment, ETH price tends to rise significantly the next day (+9.55% and +15.38% respectively). This suggests that extreme community engagement, regardless of sentiment direction, often coincides with strong price rebounds.
- **Event-Based Exploration:** On February 4, 2020 (positive sentiment), ETH was in a bullish price pattern, reflecting optimism in both the market and community. On February 26, 2022 (negative sentiment), despite pessimism due to global events (Ukraine crisis), ETH price still rose, showing that external factors can override sentiment.

## Conclusion
Reddit sentiment and ETH price are related, but not in a simple or predictive way. Extreme sentiment days often precede strong price moves, but overall, sentiment does not reliably forecast price direction. Real-world events and market dynamics play a significant role, sometimes outweighing community mood.

## What I Learned
- Deepened skills in pandas, matplotlib, and scikit-learn for data analysis and modeling.
- Gained experience in time series analysis, lag analysis, and event-based exploration.
- Learned the importance of connecting data to real-world context and market events.

## Next Steps
- Explore sentiment by topic or post type.
- Build predictive models using additional features.
- Analyze other social platforms for comparison.



