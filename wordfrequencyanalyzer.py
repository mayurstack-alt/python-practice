from string import punctuation

def analyze_text(text):
    for p in punctuation:
        text = text.replace(p, "")
    text = text.lower()
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:10]

print("Enter text (Press Enter twice to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
text = " ".join(lines)
result = analyze_text(text)
print(result)