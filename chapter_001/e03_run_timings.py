"""
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs,
until the user presses Enter. At that point, the function exits--but only
after calculating and displaying the average time that the 10 km runs took.
"""


def run_timings():
    """
    Calculate the average time it took to run 10k given a number of
    times that have been entered by the user.
    """

    running_times = []

    while recorded_time := input(f"Enter your 10k time: "):
        if not recorded_time:
            break
        running_times.append(float(recorded_time))
    average_pace = sum(running_times) / len(running_times)
    return average_pace


run_timings()
