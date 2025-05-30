import json

user = {
    "username": "vishu_01",
    "theme": "dark",
    "language": "English"
}

# Save to file
with open("settings.json", "w") as f:
    json.dump(user, f)

# Load settings back
with open("settings.json", "r") as f:
    loaded_user = json.load(f)
    print("Theme:", loaded_user["theme"])
