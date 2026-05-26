import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ── Sample Movie Dataset ──────────────────────────────────────────
movies = pd.DataFrame({
    'title': [
        'The Dark Knight', 'Inception', 'Interstellar',
        'The Avengers', 'Iron Man', 'Captain America',
        'The Notebook', 'Titanic', 'A Walk to Remember',
        'The Conjuring', 'It', 'Get Out'
    ],
    'genres': [
        'action crime thriller', 'action scifi thriller', 'scifi drama adventure',
        'action scifi superhero', 'action scifi superhero', 'action superhero adventure',
        'romance drama', 'romance drama tragedy', 'romance drama',
        'horror thriller', 'horror thriller', 'horror thriller mystery'
    ],
    'description': [
        'Batman fights the Joker in Gotham City',
        'A thief enters dreams to plant an idea',
        'Astronauts travel through a wormhole to save humanity',
        'Superheroes unite to save the world from aliens',
        'Billionaire builds a suit to become a superhero',
        'A soldier becomes a superhero to fight evil',
        'Two people fall in love over one summer',
        'A love story on a sinking ship',
        'A bad boy falls for a good girl with a secret',
        'Paranormal investigators face a demonic haunting',
        'Children face an ancient evil shapeshifting clown',
        'A man uncovers a disturbing secret about his girlfriend family'
    ]
})

# ── Combine features for similarity ──────────────────────────────
movies['combined'] = movies['genres'] + ' ' + movies['description']

# ── TF-IDF Vectorizer ─────────────────────────────────────────────
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined'])

# ── Cosine Similarity ─────────────────────────────────────────────
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# ── Recommendation Function ───────────────────────────────────────
def recommend_movies(movie_title, num_recommendations=3):
    # Check if movie exists
    if movie_title not in movies['title'].values:
        print(f"\n❌ Movie '{movie_title}' not found in database!")
        print("📽️  Available movies:")
        for m in movies['title'].values:
            print(f"   - {m}")
        return

    # Get index of the movie
    idx = movies[movies['title'] == movie_title].index[0]

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort by similarity (excluding itself)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]

    # Get movie indices
    movie_indices = [i[0] for i in sim_scores]

    print(f"\n🎬 Because you liked '{movie_title}', we recommend:")
    print("=" * 45)
    for i, idx in enumerate(movie_indices, 1):
        print(f"{i}. {movies['title'][idx]}")
        print(f"   Genre : {movies['genres'][idx]}")
        print(f"   About : {movies['description'][idx]}")
        print()

# ── Collaborative Filtering (User-Based) ─────────────────────────
ratings = pd.DataFrame({
    'user':  ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Bob', 'Carol', 'Carol', 'Carol'],
    'movie': ['The Dark Knight', 'Inception', 'Interstellar',
              'The Avengers', 'Iron Man', 'The Dark Knight',
              'Titanic', 'The Notebook', 'Inception'],
    'rating': [5, 4, 5, 4, 5, 3, 5, 4, 3]
})

def collaborative_recommend(user_name):
    if user_name not in ratings['user'].values:
        print(f"\n❌ User '{user_name}' not found!")
        print(f"👥 Available users: {list(ratings['user'].unique())}")
        return

    # Movies already watched by user
    watched = ratings[ratings['user'] == user_name]['movie'].values

    # Movies watched by other users but not by this user
    other_movies = ratings[ratings['user'] != user_name]
    not_watched = other_movies[~other_movies['movie'].isin(watched)]

    # Recommend top rated unwatched movies
    recommendations = (
        not_watched.groupby('movie')['rating']
        .mean()
        .sort_values(ascending=False)
        .head(3)
    )

    print(f"\n👤 Collaborative Recommendations for {user_name}:")
    print("=" * 45)
    for movie, score in recommendations.items():
        print(f"⭐ {movie}  (avg rating: {score:.1f})")

# ── Run the System ────────────────────────────────────────────────
if __name__ == "__main__":
    print("╔══════════════════════════════════════════╗")
    print("║      🎬 MOVIE RECOMMENDATION SYSTEM      ║")
    print("╚══════════════════════════════════════════╝")

    # Content-Based
    recommend_movies("Inception")
    recommend_movies("Titanic")

    # Collaborative
    collaborative_recommend("Alice")
    collaborative_recommend("Bob")