import pandas as pd
from itertools import combinations

# Re-define the file paths after environment reset
files = {

    "Static1.txt": "static1.txt",
    "Static2.txt": "static2.txt"
}

# Load and clean the files
def load_data(path):
    with open(path, 'r') as f:
        return ''.join(f.read().split())

# Compare strings using long common subsequence window method
def sliding_similarity(sig1, sig2, window=20): 
    matches = 0
    total = max(len(sig1), len(sig2))
    for i in range(0, len(sig1) - window + 1, window):
        chunk = sig1[i:i + window]
        if chunk in sig2:
            matches += len(chunk)
    return 100 * matches / total if total > 0 else 0

# Perform comparison
results = []
labels = list(files.keys())
data = {name: load_data(path) for name, path in files.items()}

for a, b in combinations(labels, 2):
    sig1 = data[a]
    sig2 = data[b]
    similarity = round(sliding_similarity(sig1, sig2, window=20), 2)
    total_len = max(len(sig1), len(sig2))
    byte_diff = abs(len(sig1) - len(sig2)) + sum(1 for x, y in zip(sig1, sig2) if x != y)
    conclusion = "🟢 Static Code" if similarity >= 50 else "🔴 Rolling Code"
    results.append({
        "File A": a,
        "File B": b,
        "Similarity (%)": similarity,
        "Byte Differences": byte_diff,
        "Total Length": total_len,
        "Conclusion": conclusion
    })

# Output to Excel
df = pd.DataFrame(results)
output_path = "Signal_Code_Analysis.xlsx"
df.to_excel(output_path, index=False)
output_path
