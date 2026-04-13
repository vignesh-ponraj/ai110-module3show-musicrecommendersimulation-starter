"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


USER_PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.88,
        "danceability": 0.84,
        "tempo_bpm": 128,
        "valence": 0.82,
        "acousticness": 0.15,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.38,
        "danceability": 0.60,
        "tempo_bpm": 78,
        "valence": 0.60,
        "acousticness": 0.80,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.93,
        "danceability": 0.62,
        "tempo_bpm": 154,
        "valence": 0.46,
        "acousticness": 0.08,
    },
    "Rock + Sad Contrast": {
        "genre": "rock",
        "mood": "sad",
        "energy": 0.90,
    },
    "Chill Lofi Fast Tempo": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "tempo_bpm": 160,
    },
    "Focused Lofi Detailed": {
        "genre": "lofi",
        "mood": "focused",
        "energy": 0.41,
        "danceability": 0.61,
        "tempo_bpm": 81,
        "acousticness": 0.77,
        "valence": 0.58,
    },
}


def profile_gist(profile: dict) -> str:
    """Return a short, readable summary of a profile."""
    genre = profile.get("genre", "-")
    mood = profile.get("mood", "-")
    energy = profile.get("energy", "-")
    return f"genre={genre}, mood={mood}, energy={energy}"


def select_profile_from_terminal() -> tuple[str, dict]:
    """Show numbered profiles and return the user's selected profile."""
    profile_names = list(USER_PROFILES.keys())

    print("\nAvailable profiles:")
    for idx, name in enumerate(profile_names, start=1):
        print(f"  {idx}. {name} -> {profile_gist(USER_PROFILES[name])}")

    raw_choice = input("\nPick a profile number (press Enter for 1): ").strip()
    if not raw_choice:
        selected_index = 1
    else:
        try:
            selected_index = int(raw_choice)
        except ValueError:
            print("Invalid input. Using profile 1.")
            selected_index = 1

    if selected_index < 1 or selected_index > len(profile_names):
        print("Out-of-range choice. Using profile 1.")
        selected_index = 1

    selected_name = profile_names[selected_index - 1]
    return selected_name, USER_PROFILES[selected_name]


def main() -> None:
    songs = load_songs("data/songs.csv") 

    active_profile_name, user_prefs = select_profile_from_terminal()

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*70)
    print("🎵 TOP MUSIC RECOMMENDATIONS")
    print("="*70)
    print(f"\nProfile: {active_profile_name}")
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
