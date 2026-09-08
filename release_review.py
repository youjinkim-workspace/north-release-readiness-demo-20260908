"""Small, executable release-review engine. This is a demonstration, not deployment approval."""
def review(item):
    if item.get("checklist") == "done" and item.get("pr_state") == "open":
        return "MISMATCH", "Checklist says done; implementation is not merged."
    if item.get("blocker") and item.get("pr_state") != "merged":
        return "BLOCKER", "Unresolved release blocker requires owner review."
    if item.get("pr_state") == "merged":
        return "MERGED", "Merged; deployment and CI require separate evidence."
    return "UNKNOWN", "Insufficient evidence; do not assume ready."

if __name__ == "__main__":
    import json
    from pathlib import Path
    for item in json.loads(Path("release/checklist.json").read_text())["items"]:
        print(item["title"], *review(item), sep=" | ")
