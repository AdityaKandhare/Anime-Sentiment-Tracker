# Social Media Anime Popularity Dashboard

## Description
This project examines the influence of social media discussions on anime popularity across multiple platforms, including Reddit, 4chan, MyAnimeList, and political forums. The goal is to answer two key research questions:
1. How do engagement patterns across platforms correlate with anime popularity rankings over time?
2. How do sentiment analysis results and toxicity levels impact audience engagement and popularity metrics?

Data from these platforms is collected, analyzed, and visualized on an interactive dashboard. The dashboard allows users to explore trends, sentiment distributions, and other metrics related to anime popularity.

## Tech Stack
**Python**: Core programming language used for development and testing.
**Flask**: A micro web framework for building the interactive dashboard (3.1.0).
**MySQL**: Used for structured data storage.
**Matplotlib and Seaborn**: Libraries for creating graphs and visualizations.
**NLTK and TextBlob**: For sentiment and text analysis.
**MySQL-Connector-Python**: For database integration.
**Jinja2**: For rendering HTML templates dynamically.

### Dependencies
The project requires the Python libraries listed in `requirements.txt`. Key libraries include:
**Flask-Cors**: Enables cross-origin requests.
**Pandas and NumPy**: For data manipulation and analysis.
**Scikit-learn**: For data processing and feature extraction.
**TQDM**: For progress tracking during data collection and analysis.

## Data Sources
**Reddit**: Subreddit discussions are analyzed for comment volume and sentiment.
**4chan**: Analyzed for sentiment distribution and post activity.
**MyAnimeList**: Provides anime rankings, favorites, and scores.
**Politics (/pol/ on 4chan)**: Used to study discussion consistency and posting trends.

### Key APIs
**Reddit API**: Fetches subreddit data for analysis.
**4chan Scraper**: Extracts board-specific data for sentiment analysis.
**MyAnimeList API**: Retrieves anime rankings and user preferences.

## Methodology
## Data Collection
- Reddit and 4chan data are collected using respective APIs and scrapers.
- MyAnimeList data is retrieved using structured queries.
- Sentiment analysis is applied using NLTK and TextBlob to classify discussions as positive, neutral, or negative.

## Data Analysis
- Sentiment and toxicity metrics are computed to assess their impact on engagement.
- Graphical trends are generated using Matplotlib and Seaborn.

## Dashboard Features
**Interactive Visualizations**:
   - Reddit: Subreddit engagement and sentiment metrics.
   - 4chan: Anime discussion patterns and sentiment distribution.
   - MyAnimeList: Heatmap of anime scores and top favorited anime.
   - Politics: Consistency of posts over time on /pol/.

**User Interaction**:
   - Dropdown menu for selecting specific anime.
   - Date range selector for filtering temporal data.

**Dynamic Graphs**:
   - Visuals auto-update based on user inputs.

## How to Run the Project

### Prerequisites
1. Install Python 3.x and `pip`.
2. Install MySQL and configure the database credentials in relevant scripts.

### Setup
1. Clone the project repository:
   ```bash
   
   git clone <repository_url>
Navigate to the project directory:
cd implementation

Create and activate a virtual environment:

python3 -m venv myenv
source myenv/bin/activate

Install required dependencies:

pip install -r requirements.txt

Running the Dashboard
Start the Flask application:

python3 app.py

Open the dashboard in your browser at: http://127.0.0.1:8000


File Structure
graph_scripts/: Contains Python scripts for each platform's analysis.
static/icons/: Stores icons used in the dashboard.
templates/: Includes the HTML templates (dashboard.html, platform_graph.html).
tmp/: Directory for temporarily saving graph outputs.
style.css: Contains the dashboard's CSS styling.


Research Questions Addressed
Engagement Patterns and Popularity Rankings:

Demonstrates a strong correlation between engagement (e.g., comments and scores) and anime popularity.
Platforms like Reddit and MyAnimeList highlight active user participation and its impact on visibility.
Sentiment Analysis and Toxicity:

Positive sentiment correlates with higher engagement and popularity metrics.
Even polarizing or negative sentiment can drive discussions, particularly on platforms like 4chan.

Troubleshooting
Static Files Not Loading: Ensure the static/ and templates/ directories are correctly structured.
Database Errors: Verify MySQL credentials in the scripts.
Graph Issues: Check the tmp/ directory for generated images. Ensure Matplotlib and Seaborn are installed.

Contact
Anway Atkekar: aatkekar@binghamton.edu
Aditya Kandhare: akandhare@binghamton.edu
Sharwari Ambegaonkar: sambegaonkar@binghamton.edu
