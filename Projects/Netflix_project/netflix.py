import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"D:\Kushagra\Data-science\Matplotlib\Netflix_project\netflix_titles.csv"
)

print(df.columns)

df = df.dropna(subset=['type', 'title', 'director', 'cast', 'country', 'date_added','release_year', 'rating', 'duration', 'listed_in', 'description'])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index , type_counts.values , color = ['skyblue','green'])
plt.title("No. of movies VS TV shows on Netflix")
plt.xlabel("Type")
plt.ylabel('count')
plt.tight_layout()
plt.savefig("movies_vs_tvShows.png", dpi = 300, bbox_inches = "tight")
plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels = rating_counts.index, autopct= '%1.1f%%', startangle=90)
plt.title("Rating comparison")
plt.tight_layout()
plt.savefig("ratings.png", dpi = 300, bbox_inches = "tight")
plt.show()

movie_df = df[df['type']== 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins = 30, color = "purple", edgecolor = "black")
plt.title("Movie duration")
plt.xlabel("Duration (in mins)")
plt.ylabel('No. of movies')
plt.tight_layout()
plt.savefig("movies_duration.png", dpi = 300, bbox_inches = "tight")
plt.show()

release_counts = df["release_year"].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index , release_counts.values, color = "red")
plt.title("Release year VS no. of shows")
plt.xlabel("Release Year")
plt.ylabel('No. of shows')
plt.tight_layout()
plt.savefig("release_year_VS_no_of_shows.png", dpi = 300, bbox_inches = "tight")
plt.show()

country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color = "magenta")
plt.title("Top 10 countries by by number of shows")
plt.xlabel("Number of shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("country_counts.png", dpi = 300, bbox_inches = "tight")
plt.show()

content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2,figsize = (12,5))
ax[0].plot(content_by_year.index , content_by_year['Movie'], color = 'red')
ax[0].set_title('Movie content')
ax[0].set_xlabel('Release Year')
ax[0].set_ylabel('No. of Movies')

ax[1].plot(content_by_year.index , content_by_year['TV Show'], color = 'green')
ax[1].set_title('Shows content')
ax[1].set_xlabel("Release year")
ax[1].set_ylabel("No. of shows")

fig.suptitle("Comparison of movies and TV shows released over year")
plt.tight_layout()
plt.savefig("Comparison_TVshows_Movies.png", dpi = 300, bbox_inches = "tight")

plt.show()