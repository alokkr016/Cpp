a_string = "Abcsagkgaskgcsvcasjgdgsucgsaglchaslcggjasde".lower()
v_counts = {}
for vowel in "aeiou":
    count = a_string.count(vowel)
    v_counts[vowel] = count
print(v_counts)