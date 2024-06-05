import tkinter as tk
import random

# 創建一個空的單字字典
word_dict = {}

# 添加單字函數
def add_word():
    # 獲取使用者在英文單字輸入框中輸入的內容
    english_word = english_entry.get()
    # 獲取使用者在中文翻譯輸入框中輸入的內容
    chinese_translation = chinese_entry.get()
    # 如果使用者同時輸入了英文單字和中文翻譯
    if english_word and chinese_translation:
        # 將英文單字和中文翻譯添加到單字字典中
        word_dict[english_word] = chinese_translation
        # 清空英文單字輸入框中的內容
        english_entry.delete(0, tk.END)
        # 清空中文翻譯輸入框中的內容
        chinese_entry.delete(0, tk.END)

# 測試單字函數
def test_word():
    # 如果單字字典中有單字
    if word_dict:
        # 從單字字典中隨機選擇一個英文單字和對應的中文翻譯
        english_word, chinese_translation = random.choice(list(word_dict.items()))
        # 在界面上顯示隨機選擇的英文單字
        english_label.config(text=english_word)
        # 清空反饋標籤的內容
        feedback_label.config(text="")
        # 定義檢查翻譯函數
        def check_translation():
            # 獲取使用者在猜測翻譯輸入框中輸入的內容
            user_translation = translation_entry.get()
            # 如果使用者輸入的翻譯與正確的中文翻譯相匹配
            if user_translation == chinese_translation:
                # 在反饋標籤中顯示“正確”字樣，字體顏色為綠色
                feedback_label.config(text="Correct!", fg="green")
            else:
                # 在反饋標籤中顯示“錯誤”字樣，同時顯示正確的中文翻譯，字體顏色為紅色
                feedback_label.config(text=f"Wrong. Correct translation is: {chinese_translation}", fg="red")
            # 清空猜測翻譯輸入框中的內容
            translation_entry.delete(0, tk.END)
        # 將提交按鈕的命令設置為檢查翻譯函數
        submit_button.config(command=check_translation)

# 創建主窗口
root = tk.Tk()
# 設置主窗口標題
root.title("單字記憶小工具")

# 創建控件

# 創建用於顯示英文單字的標籤
english_label = tk.Label(root, text="", font=("Helvetica", 18))
english_label.pack(pady=10)

# 創建用於輸入猜測翻譯的輸入框
translation_entry = tk.Entry(root, font=("Helvetica", 14))
translation_entry.pack(pady=5)

# 創建提交按鈕
submit_button = tk.Button(root, text="提交")
submit_button.pack(pady=5)

# 創建用於顯示反饋信息的標籤
feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
feedback_label.pack(pady=5)

# 創建用於輸入英文單字的輸入框
english_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
english_entry.pack(pady=5)

# 創建用於輸入中文翻譯的輸入框
chinese_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
chinese_entry.pack(pady=5)

# 創建添加單字按鈕
add_button = tk.Button(root, text="添加單字", command=add_word)
add_button.pack(pady=5)

# 創建測試按鈕
test_button = tk.Button(root, text="測試", command=test_word)
test_button.pack(pady=5)

# 運行主迴圈
root.mainloop()
