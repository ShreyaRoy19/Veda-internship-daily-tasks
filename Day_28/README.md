# Duplicate Record Detection System

A Python program designed to identify exact and near-duplicate customer or transaction records using **Pandas** and **difflib**.

---

## 🚀 Features
- **Text Normalization:** Automatically cleans and normalizes text data (lowercase, whitespace stripping) before comparison[cite: 1].
- **Exact Duplicate Report:** Identifies rows with identical attributes using Pandas[cite: 1].
- **Potential Duplicate Report:** Uses fuzzy string matching (`difflib.SequenceMatcher`) to detect typos and near-duplicates based on an adjustable similarity threshold[cite: 1].
- **Cleaned Dataset:** Outputs a consolidated dataset free of exact duplicate records[cite: 1].

---

## 🛠️ Tools & Libraries Required
- Python[cite: 1]
- Pandas[cite: 1]
- `difflib` (built-in standard library)[cite: 1]

You can install the required dependency via pip:
```bash
pip install pandas
