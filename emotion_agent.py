# emotion_agent.py
import pandas as pd
from textblob import TextBlob

class EmotionAgent:
    def __init__(self, input_csv, output_csv):
        self.input_csv = input_csv
        self.output_csv = output_csv
        self.emotions = ["Joy", "Anger", "Frustration", "Trust", "Disappointment"]

    def detect_emotion(self, text):
        """Basic rule + keyword-based emotion detection"""
        text_lower = text.lower()
        emotion_scores = {emotion:0 for emotion in self.emotions}

        # Keywords for simple detection
        keywords = {
            "Joy": ["happy", "love", "great", "awesome", "fantastic"],
            "Anger": ["angry", "hate", "annoyed", "furious", "mad"],
            "Frustration": ["frustrated", "confused", "stuck", "disappointed"],
            "Trust": ["trust", "reliable", "safe", "dependable"],
            "Disappointment": ["disappointed", "sad", "unhappy", "regret"]
        }

        for emotion, words in keywords.items():
            for word in words:
                if word in text_lower:
                    emotion_scores[emotion] += 1

        # Pick the emotion with the highest score
        detected_emotion = max(emotion_scores, key=emotion_scores.get)
        confidence = emotion_scores[detected_emotion] / (sum(emotion_scores.values()) + 1e-5)
        if sum(emotion_scores.values()) == 0:
            detected_emotion = "Neutral"
            confidence = 1.0

        return detected_emotion, round(confidence, 2)

    def run(self):
        df = pd.read_csv(self.input_csv)
        emotions = []
        confidences = []

        for text in df['processed_text']:
            emotion, conf = self.detect_emotion(str(text))
            emotions.append(emotion)
            confidences.append(conf)

        df['emotion'] = emotions
        df['emotion_confidence'] = confidences
        df.to_csv(self.output_csv, index=False)
        print(f"[EmotionAgent] Emotion detection completed and saved to {self.output_csv}")
