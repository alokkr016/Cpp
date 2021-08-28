a_string = "Abcsagkgaskgcsvcasjgdgsucgsaglchaslcggjasde"

v_counts = {vowel:a_string.casefold().count(vowel) for vowel in "abcdefghijklmnopqrstuvwxyz"}

print(v_counts)