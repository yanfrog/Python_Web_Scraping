import subprocess
from urllib.parse import quote
import os, time
print('fuck')
# 設定給google小姐發音的文字
q = '菜就多練，輸不起就別玩，以前是以前，現在是現在，你要是一直拿以前當作現在，哥們你怎麼不拿剛出生的時候對比啊'
# 轉換成符合url格式的格式的文字(Encoding成%XX%XX%XX%XX...那些，瀏覽器才看得懂)
encoded = quote(q)

# 定義指令
cmd = [
    'curl',
    '-X', # 用於指定 HTTP 請求方法
    'GET', # 向指定的 URL 發送 GET 請求
    f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encoded}',
    '-o', # 指定輸出文件
    f'./{q}.mp3'] # 保存到當前目錄下

# 執行指令，回傳 Process 物件，其中的屬性 returncode == 0 代表成功
std_output = subprocess.run(cmd) # process物件
if std_output.returncode == 0:
    print(f'下載「{q}」語音檔成功')
else:
    print(f'下載失敗')

# 定義 ffmpeg 加速指令，將聲音加速
speedup = 2.0
cmd2 = [
    './ffmpeg',
    '-i', # 輸入
    f'./{q}.mp3',
    '-filter:a',
    f'atempo={speedup}',
    f'./{q}_speedUp.mp3'
]
# 執行指令，回傳 Process 物件，其中的屬性 returncode == 0 代表成功
speed_output = subprocess.run(cmd2)
if speed_output.returncode == 0:
    print(f'語音檔「{q}」加速{speedup}倍，成功')
else:
    print(f'加速失敗')


# 多句下載
# 創建 mp3 資料夾
if not os.path.exists('mp3'):
    os.makedirs('mp3')

# 設定多個給 google 小姐發音的句子
list_words = [
    '中國有句古話，叫做',
    '西西物者，維俊傑',
    '眼下的各種刑具',
    '我想，一定能撬開閣下的嘴',
    '我希望你們好蒿跟我們合作',
    '我們係不會虧待你的'
]

for index, sentence in enumerate(list_words):
    encoded = quote(sentence)
    cmd = ['curl','-X','GET',f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encoded}','-o',f'./mp3/{index}.mp3']
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'下載「{sentence}」語音檔成功')
    else:
        print(f'下載失敗')
    speedup = 3.0
    cmd2 = ['./ffmpeg',
            '-i',
            f'./mp3/{index}.mp3',
            '-filter:a',
            f'asetrate=44100*0.4,atempo={speedup}',
            f'./mp3/{index}_speedUp.mp3']
    speed_output = subprocess.run(cmd2)
    if speed_output.returncode == 0:
        print(f'語音檔「{index}」加速{speedup}倍，成功')
    else:
        print(f'加速失敗')
