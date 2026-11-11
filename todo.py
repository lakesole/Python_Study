todos = []

def show_menu():
    print("=== TODO 앱===")
    print("1. 할 일 추가")
    print("2. 할 일 보기")
    print("3. 할 일 완료")
    print("4. 종료")
    
def add_todo(todos):
    title = input("할 일: ")
    todo = {"title": title, "done": False}
    todos.append(todo)
    print("추가 완료!")

def show_todos(todos):
    if len(todos) == 0:
        print("할일이 없어요!")
        return
    for i, todo in enumerate(todos, 1):
        if todo["done"]:
            status = "완료"
        else:
            status = "미완료"
        print(f"[{i}] {todo['title']} ({status})")
        
def complete_todo(todos):
    show_todos(todos)
    number = int(input("완료할 번호: "))
    todos[number - 1]["done"] = True
    print("완료 처리!")
     
while True:
    show_menu()
    choice = input("선택: ")
    
    if choice == "1":
        add_todo(todos)
    elif choice == "2":
        show_todos(todos)
    elif choice == "3":
        complete_todo(todos)
    elif choice == "4":
        print("종료!")
        break 