import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def generate_reddit_graphs():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="",
            password="",
            database="FINAL"
        )

        # --- Total Comments by Subreddit ---
        query_comments = """
        SELECT subreddit, SUM(comments) AS total_comments
        FROM subreddit_data
        WHERE subreddit IN ('AttackonTitan', 'Naruto', 'Deathnote', 'Uzumaki', 'DemonSlayer', 'Pokemon')
        GROUP BY subreddit
        ORDER BY total_comments DESC
        """
        df_comments = pd.read_sql(query_comments, connection)

        # Plot Comments Graph
        plt.figure(figsize=(10, 6))
        bars = plt.bar(df_comments['subreddit'], df_comments['total_comments'], color='skyblue', edgecolor='black')
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                     f"{int(bar.get_height())}", ha="center", va="bottom", fontsize=10, color="black")
        plt.title("Total Comments by Subreddit", fontsize=14)
        plt.xlabel("Subreddit", fontsize=12)
        plt.ylabel("Total Comments", fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        plt.tight_layout()

        # Save Comments Graph to a BytesIO object
        img1 = io.BytesIO()
        plt.savefig(img1, format='png')
        img1.seek(0)
        plt.close()

        # --- Total Score by Subreddit ---
        query_score = """
        SELECT subreddit, SUM(score) AS total_score
        FROM subreddit_data
        WHERE subreddit IN ('AttackonTitan', 'Naruto', 'Deathnote', 'Uzumaki', 'DemonSlayer', 'Pokemon')
        GROUP BY subreddit
        """
        df_score = pd.read_sql(query_score, connection)

        # Plot Score Graph
        plt.figure(figsize=(10, 6))
        sns.barplot(x='subreddit', y='total_score', data=df_score, palette='viridis')
        for index, row in df_score.iterrows():
            plt.text(index, row['total_score'] + 10000, f"{int(row['total_score']):,}",
                     ha="center", va="bottom", fontsize=10, color="black")
        plt.title("Total Score by Subreddit", fontsize=14)
        plt.xlabel("Subreddit", fontsize=12)
        plt.ylabel("Total Score", fontsize=12)
        plt.tight_layout()

        # Save Score Graph to a BytesIO object
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
