# 교재 dictionary 예제
subjects = {
        '국어' : '90',
        '수학' : '100',
        '영어' : '80',
 }
student = '홍길동'
subject = '수학'
# 옛날 방법
print(student, '학생의', subject, '과목성적은', subjects['수학'], '입니다')
print("%s 학생의 %s 과목성적은 %s입니다" % (student, subject, subjects[subject]))
# 모던 방법 (format 함수 활용)  0,1,2 포지셔닝 활용 가능, 숫자 굳이 안써도 순서대로 되긴함
print("{2} 학생의 {1} 과목성적은 {0} 입니다".format(student, subject, subjects[subject]))
print("{} 학생의 {} 과목성적은 {} 입니다".format(student, subject, subjects[subject]))
# 스트링 방식 활용
print(f'{student} 학생의 {subject} 과목 성적은 {subjects[subject]}입니다.')

