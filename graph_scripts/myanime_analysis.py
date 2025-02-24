import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def generate_myanime_graphs():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="",
            password="",
            database="FINAL"
        )

        # Query 1: Data for the heatmap
        query1 = "SELECT name, score, popularity, members, favorites, anime_rank FROM myanime_data;"
        df1 = pd.read_sql(query1, connection)

        # Query 2: Data for Top 10 Most Favorited Anime
        query2 = "SELECT name, favorites FROM myanime_data;"
        df2 = pd.read_sql(query2, connection)

        if df1.empty or df2.empty:
            raise ValueError("No data found in the 'myanime_data' table.")

        # --- Heatmap Plot ---
        # Data Cleaning
        df1 = df1.dropna()
        # Create a pivot table for scores
        pivot = df1.pivot_table(values='score', index='anime_rank', columns='name', aggfunc='mean')

        # Plotting the heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(pivot, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5)
        plt.title('Heatmap of Anime Scores by Rank and Name', fontsize=16)
        plt.xlabel('Anime Name', fontsize=12)
        plt.ylabel('Anime Rank', fontsize=12)
        plt.xticks(rotation=90, fontsize=10)
        plt.tight_layout()

        # Save the heatmap to a BytesIO object
        img1 = io.BytesIO()
        plt.savefig(img1, format='png')
        img1.seek(0)
        plt.close()

        # --- Top 10 Favorites Plot ---
        # Sort data and select top 10
        top_favorites = df2[['name', 'favorites']].sort_values(by='favorites', ascending=False).head(10)

        # Plotting the bar chart
        plt.figure(figsize=(12, 6))
        plt.barh(top_favorites['name'], top_favorites['favorites'], color='lightblue')
        plt.title('Top 10 Most Favorited Anime', fontsize=16)
        plt.xlabel('Number of Favorites', fontsize=12)
        plt.ylabel('Anime Name', fontsize=12)
        plt.tight_layout()

        # Save the bar chart to a BytesIO object
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

import matplotlib.pyplot as plt
import os

def generate_specific_anime_graph(anime_name):
    # Sample data
    data = {
        "cowboy_bebop": (1926986, 84695, 8.75, 46),
        "naruto": (2935715, 81560, 8.0, 667),
        "one_piece": (2462090, 231078, 8.72, 58),
        "death_note": (4022220, 176977, 8.62, 88),
        "hunter_x_hunter": (2944582, 216113, 9.03, 9),
    }

    if anime_name not in data:
        return None

    members, favorites, score, rank = data[anime_name]

    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Subplot 1: Members vs Favorites
    bars1 = axes[0].bar(
        ["Members", "Favorites"],
        [members, favorites],
        color=["#4c72b0", "#dd8452"]
    )
    axes[0].set_title(f"{anime_name.replace('_', ' ').title()}: Members vs Favorites", fontsize=14)
    axes[0].set_ylabel("Count")
    axes[0].tick_params(axis="x", rotation=45)

    # Add counts on top of the bars
    for bar in bars1:
        height = bar.get_height()
        axes[0].text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{int(height):,}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    # Subplot 2: Rank vs Score
    bars2 = axes[1].bar(
        ["Rank", "Score"],
        [rank, score],
        color=["#55a868", "#c44e52"]
    )
    axes[1].set_title(f"{anime_name.replace('_', ' ').title()}: Rank vs Score", fontsize=14)
    axes[1].set_ylabel("Value")
    axes[1].tick_params(axis="x", rotation=45)

    # Add counts on top of the bars
    for bar, value in zip(bars2, [rank, score]):
        height = bar.get_height()
        axes[1].text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{int(value):,}" if isinstance(value, int) else f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    # Save graph to a temporary location
    img_path = f"tmp/{anime_name}_combined_graph.png"
    os.makedirs("tmp", exist_ok=True)
    plt.savefig(img_path)
    plt.close()
    return img_path
