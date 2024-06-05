# 定義加法函數
def add(x, y):
    return x + y

# 定義減法函數
def subtract(x, y):
    return x - y

# 定義乘法函數
def multiply(x, y):
    return x * y

# 定義除法函數
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "除數不能為零"

print("歡迎使用簡單的計算器！")
print("可用運算符：+、-、*、/")

while True:
    # 提示用戶輸入計算式
    expression = input("請輸入計算式（示例：2 + 3）或輸入 'exit' 退出：")

    # 檢查用戶是否要退出
    if expression.lower() == "exit":
        print("感謝使用，再見！")
        break

    # 將用戶輸入的計算式分割成數字和運算符
    try:
        num1, operator, num2 = expression.split()
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("輸入的格式不正確，請重新輸入！")
        continue

    # 執行計算
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        print("無效的運算符，請重新輸入！")
        continue

    # 顯示計算結果
    print("計算結果：", result)
