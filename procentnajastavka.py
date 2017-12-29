P = int(input())
X = int(input())
Y = int(input())
X1 = X + X * (P / 100)
# в х1 есть копейки надо че то придумать
kopotrub = int(round(X1 % 1, 2) * 100)
Y1 = Y + Y * (P / 100)
Y2 = Y1 + kopotrub
# узнаем сколько рублей в полученных копейках
Y3 = Y2 // 100
# потом прибавим у3 к рублям
KopeikiNew = Y2 % 100
# потом прибавим
RubNew = int((int(X1) * 100) // 100) + int(Y3)
print(int(RubNew), int(KopeikiNew))
