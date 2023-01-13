# 챕터 4
a=[]
print(bool(a))
a.append(5)   #추가
print(bool(a))
print(bool(set()))
print(bool(dict()))
print(bool("aa"))

vowels = 'aeiou'
letter ='x'
if letter not in vowels:   # in 키워드 되게 유용
    print("안 들어감")

limits = 20
tweets = "pass" * 6
diff = limits - len(tweets)
if diff >= 0:
# if diff := limits - len(tweets) >= 0:
    print(tweets)
else:
    print(f'제한 글자 수 {abs(diff)} 초과')
