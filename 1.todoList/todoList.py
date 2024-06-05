todo_List = []

print("Welcome to TodoList!")

while True:
    # 顯示選項給用戶
    print("\n請選擇操作：")
    print("1. 顯示待辦事項清單")
    print("2. 新增待辦事項")
    print("3. 刪除待辦事項")
    print("4. 退出")

    choice = input("請輸入操作編號：")
    if choice == '1':
        if len(todo_List) == 0:
            print("待辦事項清單為空。")
        else:
            print("待辦事項清單：")
            for index, item in enumerate(todo_List, start=1):
                print(f"{index}, {item}")
    elif choice == '2':
        new_item = input("請輸入代辦事項：")
        todo_List.append(new_item)
        print("代辦事項已成功添加！")
    elif choice == '3':
        if len(todo_List) == 0:
            print("待辦事項清單為空，無法刪除。")
        else:
            print("待辦事項清單：")
            for index, item in enumerate(todo_List, start=1):
                print(f"{index}, {item}")
            item_to_delete = int(input("請輸入要刪除的待辦事項的編號："))
            if 1 <= item_to_delete <= len(todo_List):
                del todo_List[item_to_delete - 1]
                print("待辦事項已成功刪除！")
            else:
                print("無效的編號，請重新輸入。")
    elif choice == '4':
        print("感謝使用，再見！")
        break
    else :
        print("無效操作，請重新輸入")