
def count_vowels(txt):
    vowel_count = 0
    # count the vowels in some text
    # in abc, one vowel
    for char in txt:
        if char in ["a", "e", "i", "o", "u"]:
            # increment a counter
            vowel_count += 1
    return vowel_count
print(f"number of vowels is {count_vowels("abcaa")}")