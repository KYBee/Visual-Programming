menu = {'noodle': '500원', 'ham': '200원', 'egg': '100원', 'spaghetti': '900원'}


print("안녕하세요 다음의 메뉴 중 원하는 메뉴를 선택하세요.")
target_food = input("(noodle, ham, egg, spaghetti) ")

if target_food in menu:
    print(menu[target_food])
else:
    print("그런 메뉴는 없습니다.")
