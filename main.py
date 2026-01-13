from agents.ingestion_agent import IngestionAgent
from agents.preprocessing_agent import PreprocessingAgent

def main():
    ingestion_agent = IngestionAgent("data/raw_feedback.csv")
    preprocessing_agent = PreprocessingAgent()

    df = ingestion_agent.load_data()
    if df is not None:
        processed_df = preprocessing_agent.preprocess(df)
        processed_df.to_csv("data/processed_feedback.csv", index=False)
        print("[Moodlytics] Pipeline executed successfully")

if __name__ == "__main__":
    main()
