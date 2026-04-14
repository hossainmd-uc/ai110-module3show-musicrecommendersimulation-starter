"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    # Fallback for direct execution: python src/main.py
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
        "acousticness": 0.20,  # or use "likes_acoustic": False
        "tempo_bpm": 120.0,  # optional
        "danceability": 0.78,  # optional
        "valence": 0.82,  # optional
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations\n")
    for idx, rec in enumerate(recommendations, start=1):
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        reasons = [part.strip() for part in explanation.split("|") if part.strip()]

        print(f"{idx}. {song['title']}")
        print(f"   Final Score: {score:.3f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"   - {reason}")
        print("-" * 60)


if __name__ == "__main__":
    main()
