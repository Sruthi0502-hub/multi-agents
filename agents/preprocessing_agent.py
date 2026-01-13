import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

class PreprocessingAgent:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"http\S+|www\S+", "", text)   # remove URLs
        text = re.sub(r"\d+", "", text)              # remove numbers
        text = text.translate(str.maketrans("", "", string.punctuation))
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def remove_stopwords(self, text):
        tokens = text.split()
        filtered = [word for word in tokens if word not in self.stop_words]
        return " ".join(filtered)

    def preprocess(self, df, text_column="feedback_text"):
        df["cleaned_text"] = df[text_column].apply(self.clean_text)
        df["processed_text"] = df["cleaned_text"].apply(self.remove_stopwords)
        print("[PreprocessingAgent] Text preprocessing completed")
        return df
