import json
import pandas as pd

with open("ecommerce_faq.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]

df = pd.DataFrame(questions)

df.to_csv("ecommerce_faq.csv", index=False)

print("JSON converted to CSV successfully!")


