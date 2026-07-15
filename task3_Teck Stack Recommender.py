import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("raw_skills.csv")

df = df.dropna(subset=["raw_skills"])

career_profiles = {
    "Data Scientist":
        "python pandas numpy statistics machine learning sql data visualization",

    "Data Analyst":
        "sql excel power bi tableau python statistics",

    "Machine Learning Engineer":
        "python tensorflow pytorch deep learning machine learning nlp",

    "AI Engineer":
        "python tensorflow pytorch computer vision deep learning nlp",

    "Backend Developer":
        "python java django flask sql api git",

    "Frontend Developer":
        "html css javascript react angular bootstrap",

    "Full Stack Developer":
        "html css javascript react nodejs python sql",

    "DevOps Engineer":
        "docker kubernetes aws linux git jenkins ci cd automation",

    "Cloud Engineer":
        "aws azure docker kubernetes linux terraform",

    "Cloud Architect":
        "aws azure cloud docker kubernetes networking",

    "System Administrator":
        "linux windows bash networking virtualization",

    "Cybersecurity Analyst":
        "network security linux wireshark penetration testing firewall",

    "Network Engineer":
        "networking cisco routing switching linux tcp ip",

    "Database Administrator":
        "sql mysql oracle postgresql database",

    "Software Engineer":
        "python java c++ git algorithms data structures",

    "Mobile App Developer":
        "android kotlin java flutter dart",

    "QA Engineer":
        "testing selenium automation junit",

    "Site Reliability Engineer":
        "linux docker kubernetes aws monitoring",

    "Big Data Engineer":
        "spark hadoop hive python kafka sql",

    "Business Intelligence Developer":
        "power bi tableau sql excel data warehouse"
}

dataset_skills = " ".join(df["raw_skills"].astype(str).tolist())

documents = [dataset_skills] + list(career_profiles.values())

vectorizer = TfidfVectorizer(stop_words="english")

tfidf_matrix = vectorizer.fit_transform(documents)

career_vectors = tfidf_matrix[1:]

while True:

    user_input = input(
        "Enter exactly 3 skills separated by commas:\n"
    )

    skills = [skill.strip().lower() for skill in user_input.split(",") if skill.strip()]

    if len(skills) == 3:
        break

    print("\nPlease enter exactly 3 skills.\n")

user_text = " ".join(skills)

user_vector = vectorizer.transform([user_text])

similarity = cosine_similarity(user_vector, career_vectors)

scores = similarity.flatten()

top_indices = scores.argsort()[-3:][::-1]

career_names = list(career_profiles.keys())
print("\n")
print("=" * 50)
print("TOP 3 CAREER RECOMMENDATIONS:")
print("=" * 50)

for rank, index in enumerate(top_indices, start=1):
  print(f"\n{rank}. {career_names[index]}")
  print(f"Similarity Score : {scores[index]*100:.2f}%")

print("\nThank you for using the Tech Stack Recommender!")