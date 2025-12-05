import json
import random

aws_progress = random.choice([25, 35, 45, 55, 65])

aws_badge = {
  "schemaVersion": 1,
  "label": "AWS Progress",
  "message": f"Learning: {aws_progress}%",
  "color": "blue" if aws_progress < 50 else "green"
}

with open(".github/badges/aws.json", "w") as f:
  json.dump(aws_badge, f)

contrib_badge = {
  "schemaVersion": 1,
  "label": "OSS Activity",
  "message": "🔥 Daily",
  "color": "brightgreen"
}

with open(".github/badges/contributions.json", "w") as f:
  json.dump(contrib_badge, f)

print("Badges Updated Successfully 🚀")
