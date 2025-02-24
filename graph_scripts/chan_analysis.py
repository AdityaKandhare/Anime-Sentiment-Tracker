import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import io

def generate_4chan_graphs():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="",
            password="",
            database="FINAL"
        )

        # Query to get the comments and anime names from the 'chan_anime_comments' table for board 'a'
        query = "SELECT anime_name, reply_content FROM chan_anime_comments WHERE board = 'a';"
        df = pd.read_sql(query, connection)

        if df.empty:
            raise ValueError("No data found for board 'a' in the 'chan_anime_comments' table.")

        # Function to classify the sentiment of each comment
        def get_sentiment(text):
            blob = TextBlob(text)
            sentiment_score = blob.sentiment.polarity
            if sentiment_score > 0:
                return 'Positive'
            elif sentiment_score < 0:
                return 'Negative'
            else:
                return 'Neutral'

        # Apply sentiment analysis to each comment
        df['sentiment'] = df['reply_content'].apply(get_sentiment)

        # --- Sentiment Distribution Plot ---
        sentiment_by_anime = df.groupby(['anime_name', 'sentiment']).size().unstack(fill_value=0)

        plt.figure(figsize=(12, 6))
        sentiment_by_anime.plot(kind='bar', stacked=True, color=['green', 'red', 'gray'])
        plt.title('Sentiment Distribution by Anime (Board A)', fontsize=16)
        plt.xlabel('Anime Name', fontsize=12)
        plt.ylabel('Number of Comments', fontsize=12)
        plt.xticks(rotation=90, fontsize=10)
        plt.tight_layout()

        img1 = io.BytesIO()
        plt.savefig(img1, format='png')
        img1.seek(0)
        plt.close()

        # --- Comment Count Plot ---
        comment_count_by_anime = df['anime_name'].value_counts()

        plt.figure(figsize=(12, 6))
        comment_count_by_anime.plot(kind='bar', color='skyblue')
        plt.title('Number of Comments per Anime (Board A)', fontsize=16)
        plt.xlabel('Anime Name', fontsize=12)
        plt.ylabel('Number of Comments', fontsize=12)
        plt.xticks(rotation=90, fontsize=10)
        plt.tight_layout()

        img2 = io.BytesIO()
        plt.savefig(img2, format='png')
        img2.seek(0)
        plt.close()

        return img1, img2

    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()


