# 最初にまとめて質問する
q1 = int(input('おやつにいくら使える？(Y／N)＞'))
q2 = input('甘いものがいい？(Y／N)＞')
q3 = input('カロリーを気にしてる？(Y／N)＞')

# 300円以上で甘いものもカロリーも「Y」の場合
if (q1 >= 300 and
    q2 == 'Y' and
    q3 == 'Y'):
    print('ライ麦ケーキを買う')
# 300円以上で甘いものだけが「Y」の場合
elif (q1 >= 300 and
      q2 == 'Y'):
    print('キャラメルチーズタルトを買う')
# 300円以上で甘いものもカロリーも「Y」ではない場合
elif q1 >= 300:
    print('ウーロン茶とポテチを買う')
# どの条件も成立しない（使えるお金が300円以上ではない）場合
else:
    print('チョコドーナツを買う')
