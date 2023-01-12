# 교재 countdown 예제
# for countdown in 5, 4, 3, 2, 1, "hey!":
#     print(countdown)
# print('프로그램 종료')   컨트롤슬래시로 주석처리함

countdown_list = [5, 4, 3, 2, 1, "hey!"]
for countdown in countdown_list:
    print(countdown)
print(countdown_list[3]) # 2가 출력될 것
print(countdown_list[-1]) # hey! 출력
print('프로그램 종료')