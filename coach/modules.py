import yaml
from pathlib import Path


def load_modules():
    current_file = Path(__file__)
    coach_folder = current_file.parent
    repo_root = coach_folder.parent
    metadata_file = repo_root / "metadata" / "modules.yml"

    with open(metadata_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    modules = data["modules"]
    return modules


def recommend_modules(user_text):
    modules = load_modules()
    text = user_text.lower()
    results = []

    for module in modules:
        score = 0
        matched_keywords = []

        for keyword in module["keywords"]:
            if keyword.lower() in text:
                score += 1
                matched_keywords.append(keyword)

        if score > 0:
            results.append({
                **module,
                "score": score,
                "matched_keywords": matched_keywords
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results