#成绩分段
score = int(input("成绩："))
if score > 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
print('%d belongs to %s' % (score, grade))