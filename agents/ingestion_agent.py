import pandas as pd

class IngestionAgent:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            df = pd.read_csv(self.file_path)
            print("[IngestionAgent] Data loaded successfully")
            return df
        except Exception as e:
            print("[IngestionAgent] Error loading data:", e)
            return None
