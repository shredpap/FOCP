def convert_time(seconds):
    """
    This function converts seconds to minutes and seconds format.
    """
    minutes, seconds = divmod(seconds, 60)
    minst, secst = "minutes", "seconds"
    if minutes == 1:
        minst = "minute"
    if seconds == 1:
        secst = "second"
    return "{:02d} {} {:02d} {}".format(minutes, minst, seconds, secst)

data = {}
print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")
while True:
    val = input("> ")
    if val.upper() == "END":
        break
    try:
        runner_num, time = val.split("::")
        time = int(time)
        if runner_num in data or time < 0:
            print("Error in data stream. Ignoring. Carry on.")
        else:
            data[runner_num] = time
    except:
        print("Error in data stream. Ignoring. Carry on.")

if data:
    times = list(data.values())
    total_runners = len(times)
    average_time = convert_time(int(sum(times) / total_runners))
    fastest_time = convert_time(min(times))
    slowest_time = convert_time(max(times))
    best_time_runner = min(data, key=data.get)
    print("\nTotal Runners:  {}\nAverage Time:  {}\nFastest Time:  {}\nSlowest Time:  {}\n\nBest Time Here:  Runner #{}".format(total_runners, average_time,fastest_time, slowest_time, best_time_runner))
else:
    print("No data found. Nothing to do. What a pity.")
