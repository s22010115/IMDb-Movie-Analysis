import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and set the first column as index
movies = pd.read_csv('imdb_movie_dataset.csv', index_col=0)

# Display first 5 rows
print(movies.head())

# Display number of rows and columns
print(movies.shape)

# Display column names
print(movies.columns)

#Convert Rating to numeric
# Invalid entries (text, N/A) will become NaN
movies['Rating'] = pd.to_numeric(movies['Rating'], errors='coerce')

#Remove rows without Rating
movies = movies.dropna(subset=['Rating'])

#Remove duplicate rows
movies = movies.drop_duplicates()

# Check the new shape after cleaning
print(movies.shape)

#Check missing ratings
print("Movies Missing Rating:", movies['Rating'].isnull().sum())

# Calculate average movie rating
print("Average Rating:", movies['Rating'].mean())


# VISUALIZATION

#Top 10 Movie Genres (Bar Chart)
movies['Genre'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Movie Genres')
plt.xlabel('Genres')
plt.ylabel('Number of Movies')
plt.show()

#Rating Distribution (Histogram)
movies['Rating'].plot(kind='hist', bins=10)
plt.title('Movie Rating Distribution')
plt.xlabel('Rating')
plt.show()

#Rating vs Votes (Scatter Plot)
plt.scatter(movies['Votes'], movies['Rating'])
plt.title('Rating vs Votes')
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.show()