
class GameMachine:
    def __init__(self, answer):
        self.answer = answer
        self.forbidden_numbers = {1, 2, 3}
        
        
    def start(self):
        history = []
        count = 0
        while True:
            try:
                number = int(input("숫자를 입력하세요: "))
                if number in self.forbidden_numbers:
                    print("금지된 숫자입니다!")
                    continue
                
                count = count + 1           
                history.append(number)
                
                if self.answer > number:
                    print("up!")
                elif self.answer < number:
                    print("down!")
                else:
                    print("정답!")
                    print(f"{count}번 만에 맞히셨네요!")
                    print(f"입력한 숫자: {history}")
                    with open("result.txt", "w")as f:
                        f.write(f"이번 게임 시도 횟수: {count}회")
                    break
            except ValueError:
                print("숫자를 입력하세요!")
            
my_game = GameMachine(15)
my_game.start()