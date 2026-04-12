import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric values to appropriate types."""
    songs: List[Dict] = []

    with open(csv_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a single song using genre/mood matching and numeric closeness to return score and explanations."""
    score = 0.0
    reasons = []
    
    # Genre match: +2.0 points
    if "genre" in user_prefs:
        if song["genre"].lower() == user_prefs["genre"].lower():
            score += 2.0
            reasons.append(f"genre match: {song['genre']} (+2.0)")
    
    # Mood match: +1.0 point
    if "mood" in user_prefs:
        if song["mood"].lower() == user_prefs["mood"].lower():
            score += 1.0
            reasons.append(f"mood match: {song['mood']} (+1.0)")
    
    # Energy closeness: 2.0 * (1 - |song_energy - user_energy|)
    if "energy" in user_prefs:
        energy_distance = abs(song["energy"] - user_prefs["energy"])
        energy_score = 2.0 * (1 - energy_distance)
        score += energy_score
        reasons.append(f"energy closeness: {song['energy']:.2f} vs {user_prefs['energy']:.2f} ({energy_score:.2f})")
    
    # Danceability closeness: 1.0 * (1 - distance)
    if "danceability" in user_prefs:
        danceability_distance = abs(song["danceability"] - user_prefs["danceability"])
        danceability_score = 1.0 * (1 - danceability_distance)
        score += danceability_score
        reasons.append(f"danceability: {song['danceability']:.2f} vs {user_prefs['danceability']:.2f} ({danceability_score:.2f})")
    
    # Tempo closeness: 0.5 * (1 - |tempo_distance| / 100)
    if "tempo_bpm" in user_prefs:
        tempo_distance = abs(song["tempo_bpm"] - user_prefs["tempo_bpm"])
        tempo_score = 0.5 * max(0, 1 - tempo_distance / 100)
        score += tempo_score
        reasons.append(f"tempo: {song['tempo_bpm']:.0f} vs {user_prefs['tempo_bpm']:.0f} BPM ({tempo_score:.2f})")
    
    # Acousticness closeness: 0.5 * (1 - distance)
    if "acousticness" in user_prefs:
        acousticness_distance = abs(song["acousticness"] - user_prefs["acousticness"])
        acousticness_score = 0.5 * (1 - acousticness_distance)
        score += acousticness_score
        reasons.append(f"acousticness: {song['acousticness']:.2f} vs {user_prefs['acousticness']:.2f} ({acousticness_score:.2f})")
    
    # Valence closeness: 0.5 * (1 - distance)
    if "valence" in user_prefs:
        valence_distance = abs(song["valence"] - user_prefs["valence"])
        valence_score = 0.5 * (1 - valence_distance)
        score += valence_score
        reasons.append(f"valence: {song['valence']:.2f} vs {user_prefs['valence']:.2f} ({valence_score:.2f})")
    
    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return top k recommendations sorted by score in descending order."""
    # Score each song and prepare recommendations with explanations
    recommendations = [
        (song, score, " | ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    
    # Sort by score (descending) and return top k results
    return sorted(recommendations, key=lambda x: x[1], reverse=True)[:k]
