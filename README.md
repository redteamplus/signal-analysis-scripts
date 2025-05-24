# RF Signal Analysis Tools 🔍📡

Python scripts to analyze RF (Radio Frequency) signals and determine whether they use **Static Codes** or **Rolling Codes** — useful for reverse engineering remotes, fobs, and wireless systems.

---

## 🛠 Features

- Detects similarity between two RF signals using:
  - Byte-by-byte comparison with alignment
  - Sliding Window techniques
- Auto-classifies signal pairs as:
  - 🟢 Static Code
  - 🔴 Rolling Code
- Exports comparison results to Excel
- Supports cleaning URH signal logs from `[Pause: ...]` metadata

---

## 📂 Scripts Included

| Script Name                | Description |
|---------------------------|-------------|
| `Clean SIgnal Data.py`              | Cleans signal files from URH pauses and joins hex data |
| `Signal Analysis.py`      | Compares signals using sliding window byte match |


---

## 🧪 Example

### Compare static1.txt vs static2.txt

```bash
python sliding_matcher.py static1.txt static2.txt
```

### Output:

```
Similarity: 91.86%
Conclusion: 🟢 Static Code
```

---

## 🔗 Downloads & Tools Used

- [URH (Universal Radio Hacker)](https://github.com/jopohl/urh/releases)
- [SDR++](https://www.sdrpp.org/)
- [Flipper Zero](https://flipperzero.one/)
- [TinySA Analyzer](https://tinysa.org/)
- [GNU Radio](https://www.gnuradio.org/)
- [RTL-SDR Blog](https://www.rtl-sdr.com/)

---

## 📬 Contact & Community

- Website: [www.redteamplus.net](https://www.redteamplus.net)
- Telegram: [@redteamplus](https://t.me/redteamplus)
- YouTube: [@RedTeamPlus](https://youtube.com/@RedTeamPlus)
