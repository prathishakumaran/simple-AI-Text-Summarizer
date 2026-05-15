def summarize(text):
    sentences = text.split('. ')
    total = len(sentences)
    
    # Take important sentences (first, middle, last)
    if total <= 3:
        return text
    
    summary = [
        sentences[0],
        sentences[total//2],
        sentences[-1]
    ]
    return '. '.join(summary)

print("=== AI Text Summarizer ===")
print("-" * 40)

while True:
    print("\nPaste your text (or type 'quit' to exit):")
    text = input()
    
    if text.lower() == 'quit':
        print("Goodbye!")
        break
    
    if len(text) < 50:
        print("Please enter longer text!")
        continue
    
    result = summarize(text)
    print("\n✅ Summary:")
    print(result)
    print("-" * 40)