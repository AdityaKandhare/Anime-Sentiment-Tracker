import mysql.connector
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import io

# Utility function to clean HTML content
def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()

def generate_politics_graph_by_date(start_date, end_date):
    try:
        # Establish connection to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="",
            password="",
            database="FINAL"
        )

        # Query to fetch content and timestamps within the date range
        query = f"""
        SELECT created_at, reply_content
        FROM chan_comments
        WHERE board = 'pol' AND DATE(created_at) BETWEEN '{start_date}' AND '{end_date}'
        """
        
        # Load the data into a pandas DataFrame
        df = pd.read_sql(query, connection)

        if df.empty:
            return None  # Return None if no data is found

        # Clean the HTML content and process the data
        df['cleaned_reply_content'] = df['reply_content'].apply(clean_html)
        df['created_at'] = pd.to_datetime(df['created_at'])
        df['date'] = df['created_at'].dt.date

        # Count the number of posts per day
        posts_per_day = df.groupby('date').size()

        # Plot the graph
        plt.figure(figsize=(10, 6))
        posts_per_day.plot(kind='bar', color='skyblue')
        plt.title('Number of Posts to /pol/ Board per Day')
        plt.xlabel('Date')
        plt.ylabel('Number of Posts')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()

        return img  # Return the BytesIO object

    except Exception as e:
        print(f"Error generating graph: {e}")
        return None
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()


import matplotlib.pyplot as plt

def generate_specific_anime_graph(anime_name):
    data = {
        "Cowboy Bebop": (1926986, 84695),
        "Naruto": (2935715, 81560),
        "One Piece": (2462090, 231078),
    }
    members, favorites = data.get(anime_name, (0, 0))
    
    plt.figure()
    plt.bar(["Members", "Favorites"], [members, favorites])
    plt.title(f"{anime_name}: Members vs Favorites")
    img_path = f"/tmp/{anime_name}_graph.png"
    plt.savefig(img_path)
    return img_path
