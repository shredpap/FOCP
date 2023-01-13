print("Park Run Timer")
print("~~~~~~~~~~~~~~")
print("Let's go!")

players = []
time = []

while True:
    line = input("> ")
    players.append(line)

    if line.upper() == "END":
        break
    if players[0].upper() == "END":
        print("No data found. Nothing to do. What a pity. ")
        break
    elif '::' not in line or len(line.split('::')) < 2 or line.split('::')[0] == '' or line.split('::')[1] == '':
        print("Error in data stream. Ignoring. Carry on.")
        players.pop(-1)

for t in players:
    p = t.split("::")
    time.append(p)
    runners = {int(t[0]): int(t[1])
    for t in time[:-1]}


def get_key(num):
    for key, value in runners.items():
        if num == value:
            return key


if len(runners) > 0:
    print(f"\nTotal runners: {len(runners)}")
    print(f"Average time: {(int(sum(runners.values())/len(runners)))//60}minute, {(int(sum(runners.values())/len(runners)))%60}seconds")
    print(f"Fastest Time: {max(runners.values())// 60} minute, {max(runners.values())%60} seconds")
    print(f"Slowest Time: {min(runners.values())//60}minute, {min(runners.values())%60}seconds")
    print(f"\nBest Time Here: Runner #{get_key(min(runners.values()))}")
