def print_badminton_players():
badminton_players = [
"张雨萌", "王宇航", "李文雅", "陈明明",
"赵佳琪", "刘伟杰", "杨欣媛", "韩军涛",
"王丽娜", "李磊", "刘青青", "赵晓阳",
"张倩倩", "王超", "杨晨", "陈婷婷",
"周宇", "李娜", "马骁", "朱欣怡"
]

badminton_players.sort()
columns = 2

players_per_column = len(badminton_players) 

for i in range(columns):
    start_index = i * players_per_column
    end_index = start_index + players_per_column
    column_players = badminton_players[start_index:end_index]

    for player in column_players:
        print(player.ljust(20), end=" ")
    print()  


