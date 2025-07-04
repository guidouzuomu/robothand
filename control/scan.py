from MyHand import MyGripper_H100
PORT = "/dev/ttyUSB0"
for guess in range(1, 31):
    try:
        g = MyGripper_H100(PORT, 115200, id=guess)
        real = g.get_gripper_Id()       # ここで応答があれば正解
        print(f"🎯  ID {guess} がヒット（本体は {real} と返答）")
        break
    except TimeoutError:
        pass    # 無応答なら次へ
else:
    print("どの ID にも応答しませんでした。配線・電源・Baudrate を再確認！")
