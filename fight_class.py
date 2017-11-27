import tkinter
import random

class FightManager:
    # コンストラクタ
    def __init__(self):
        self.dialog = tkinter.Frame(width=820, height=434)
        self.dialog.place(x=10, y=10)
        canvas = tkinter.Canvas(self.dialog, width=820, height=434)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0, 0, 620, 434, fill="black")
        # ボタン作成
        winbutton = tkinter.Button(self.dialog, text="勝った")
        winbutton.place(x=180, y=340)
        winbutton["command"] = self.fight_win
        losebutton = tkinter.Button(self.dialog, text="負けた")
        losebutton.place(x=360, y=340)
        losebutton["command"] = self.fight_lose
        # 非表示
        self.dialog.place_forget()
    # 戦闘開始
    def fight_start(self, map_data, x, y):
        self.dialog.place(x=10, y=10)
        self.map_data = map_data
        self.brave_x = x
        self.brave_y = y
    # 勝利
    def fight_win(self):
        self.map_data[self.brave_y][self.brave_x] = 0
        self.dialog.place_forget()
    # 敗北
    def fight_lose(self):
        canvas = tkinter.Canvas(self.dialog, width=820, height=434)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0, 0, 620, 434, fill="red")
        canvas.create_text(300, 200,
        fill="white", font=("MS ゴシック", 15),
        text="""勇者は負けてしまった…。
        最初からやり直してくれたまえ。""")

# キャラクターの親クラス
class Character:
    # コンストラクタ
    def __new__(cls):
        obj = super().__new__(cls)
        obj.rsv = 1
        return obj
    # 力をためる
    def reserve(self):
        self.rsv = self.rsv + 1
    # 攻撃力を求める
    def get_atk(self):
        r = self.rsv
        self.rsv = 1
        return random.randint(1, self.atk * r)
    # 防御力を求める
    def get_dfs(self):
        return random.randint(0, self.dfs)
    # 体力計算
    def culc_hp(self, atk, dfs):
        dmg = atk - dfs
        # ダメージ無し
        if dmg < 1:
            return self.hp
        # 体力を減らす
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

# 勇者クラス
class Brave(Character):
    def __init__(self):
        self.name = "勇者ハル"
        self.hp = 30
        self.atk = 15
        self.dfs = 10
# モンスター1
class Monster1(Character):
    def __init__(self):
        self.name = "マコデビル"
        self.hp = 20
        self.atk = 15
        self.dfs = 10
# モンスター2
class Monster2(Character):
    def __init__(self):
        self.name = "リリースネーク"
        self.hp = 10
        self.atk = 8
        self.dfs = 5
