# Phone 인스턴스들을 담기 위한 PhoneBook Class 선언
class PhoneBook:
    #PhoneBook 클래스는 선언되면서 phone_list라는 Phone 인스턴스들을 담기위한 배열을 속성으로 가짐
    def __init__ (self):
        self.phone_list = []

    # 인자를 phone_list에 추가하기 위한 add 메소드
    def add(self, person):
        self.phone_list.append(person)

    # PhoneBook 내부의 인스턴스 수를 반환하는 getter
    def getBookCount(self):
        return len(self.phone_list)

    # PhoneBook에서 i번째 인스턴스를 전달하는 getter
    def getBook(self, i):
        return self.phone_list[i]

# Phone 객체 정의
class Phone:
    # Phone 클래스는 선언되면서 name과 number을 인자로 받아 각각 name, number 속성에 할당
    def __init__(self, name, number):
        self.name = name
        self.number = number

    # 객체가 불렸을 때 돌려주는 내용으로 "이름 전화번호"의 format임
    def __str__(self):
        return self.name + " " + self.number



# 예시 코드
myPhoneBook = PhoneBook()
oneperson = Phone("홍길동", "010-5555-2222")
myPhoneBook.add(oneperson)                   
oneperson = Phone("강감찬", "010-2222-3333")      
myPhoneBook.add(oneperson)                    
oneperson = Phone("심청", "010-3333-2222")       
myPhoneBook.add(oneperson)                            

for i in range(myPhoneBook.getBookCount()) :        
    print(myPhoneBook.getBook(i))                         