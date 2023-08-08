import time

CHO = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ", "ㅁ","ㅂ","ㅃ","ㅅ",
        "ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
JUNG = ["ㅏ", "ㅐ", "ㅏ", "ㅒ","ㅓ", "ㅔ", "ㅕ","ㅖ", "ㅗ",
        "ㅘ", "ㅙ", "ㅚ","ㅛ", "ㅜ", "ㅝ", "ㅞ","ㅟ","ㅠ",
        "ㅡ", "ㅢ", "ㅣ"]
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ","ㄵ","ㄶ", "ㄷ","ㄹ","ㄺ",
        "ㄻ", "ㄼ", "ㄽ", "ㄾ",
        "ㄿ", "ㅀ", "ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ",
        "ㅋ","ㅌ","ㅍ","ㅎ"]

words = ["동해물과 백두산이 마르고 닳도록",
        "하느님이 보우하사 우리 나라 만세",
        "무궁화 삼천리 화려강산",
        "대한사람 대한으로 길이 보전하세"]

colors = {
    100 : '\033[32m',
    80 : '\033[33m',
    70 : '\033[93m',
    50 : '\033[34m',
    40 : '\033[36m',
    30 : '\033[31m'
}
END = '\033[0m'

averageTime, averageScore, averageTypo = [], [], []

def average(List):
    a = 0
    for i in range(len(List)): a += List[i]
    return a / len(List)

def scoreColor(score):
    global colors

    colorKeys = list(colors.keys())
    for i in colorKeys:
        if i == 30: break
        elif score <= i and score > colorKeys[colorKeys.index(i)+1]: return colors[i]
    return colors[30]

def break_korean(string):

        word_list = list(string)
        break_word = []
        for k in word_list:
            if ord(k) >= ord("가") and ord(k) <= ord("힝"):
                char_index = ord(k) - ord('가')

                break_word.append(CHO[int((char_index/28)/21)])
                break_word.append(JUNG[int((char_index/28)%21)])
                char3 = int(char_index%28)
                if char3 > 0: break_word.append(JONG[char3])

        return break_word
input(f"타 자 연 습\n\n점수 색상 : \n{colors[100]}    Perfect{END}\n{colors[80]}    Awesome{END}\n{colors[70]}    Great{END}\n{colors[50]}    Oh..{END}\n{colors[40]}    Uh...{END}\n{colors[30]}    Good luck..?{END}\n\nStart__")

for i in words:
    startT = time.time()
    userInput = input(f"{i}\n\033[32m>>> ").strip(); print("\033[0m")
    endT = time.time() - startT
    averageTime.append(endT)

    example, answer = break_korean(i), break_korean(userInput)
    correct = 0

    for i, word in enumerate(answer):
        if i >= len(example): break
        if word == example[i]: correct += 1

    score = (correct / len(example)) * 100
    typo = ((len(example) - correct) / len(example)) * 100
    averageScore.append(score)
    averageTypo.append(typo)

    print(f"속도 : {scoreColor(int(endT))}{endT:0.2f}ms{END}, 정확도 : {scoreColor(int(score))}{int(score)}{END}, 오타율 : {scoreColor(int(typo))}{int(typo)}{END}")

averageTime, averageScore, averageTypo = average(averageTime), average(averageScore), average(averageTypo)
print(f"\n평균 속도 : {scoreColor(int(averageTime))}{averageTime:0.2f}ms{END}, 평균 정확도 : {scoreColor(int(averageScore))}{int(averageScore)}{END}, 평균 오타율 : {scoreColor(int(averageTypo))}{int(averageTypo)}{END}")