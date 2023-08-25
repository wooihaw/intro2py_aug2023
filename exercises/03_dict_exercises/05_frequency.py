# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'The quick brown fox jumps over the lazy dog.'

# Clean and normalize the text
alist = [c.lower() for c in astring if c.isalpha()]
print(alist)

# Method 1 - Use for loop
freq1 = {}
for c in sorted(set(alist)):
    freq1[c] = alist.count(c)
print(f"{freq1 = }")

# Method 2 - Use dictionary comprehension
freq2 = {c: alist.count(c) for c in sorted(set(alist))}
print(f"{freq2 = }")

# The most frequent alphabet
alpha = [k for k in freq1]
freq = [freq1[k] for k in freq1] 
print(alpha[freq.index(max(freq))])