from agents.ingestion_agent import IngestionAgent
from agents.preprocessing_agent import PreprocessingAgent
from agents.sentiment_agent import SentimentAgent

def main():
    # Agents
    ingestion_agent = IngestionAgent("data/raw_feedback.csv")
    preprocessing_agent = PreprocessingAgent()
    sentiment_agent = SentimentAgent()

    # Load and preprocess
    df = ingestion_agent.load_data()
    if df is not None:
        df = preprocessing_agent.preprocess(df)
        df = sentiment_agent.process_dataframe(df)
        df.to_csv("data/sentiment_results.csv", index=False)
        print("[Moodlytics] Sentiment analysis completed and saved")

if __name__ == "__main__":
    main()
from emotion_agent import EmotionAgent

# Run Emotion Detection
emotion_agent = EmotionAgent(
    input_csv="data/sentiment_results.csv",
    output_csv="data/emotion_results.csv"
)
emotion_agent.run()
