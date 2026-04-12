"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*70)
    print("🎵 TOP MUSIC RECOMMENDATIONS")
    print("="*70)
    print(f"\nUser Profile: {user_prefs}\n")
    
    for idx, rec in enumerate(recommendations, 1):
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        
        # Format reasons as individual bullet points
        reasons = explanation.split(" | ")
        
        print(f"{idx}. {song['title']}")
        print(f"   Artist: {song['artist']} | Genre: {song['genre']} | Mood: {song['mood']}")
        print(f"   📊 Score: {score:.2f}")
        print("   Why recommended:")
        for reason in reasons:
            print(f"      • {reason}")
        print()
    
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
