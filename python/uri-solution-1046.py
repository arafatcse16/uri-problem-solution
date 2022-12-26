start_time, end_time = map(int, input().split())
game_duration=0
if start_time==end_time:
    game_duration=24
elif start_time>end_time:
    game_duration=(24 - start_time)+end_time
else:
    game_duration=end_time - start_time

print("O JOGO DUROU {} HORA(S)".format(game_duration))
