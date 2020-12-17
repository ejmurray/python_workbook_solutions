"""
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs,
until the user presses Enter. At that point, the function exits--but only
after calculating and displaying the average time that the 10 km runs took.

This version is similar to the first one, but does not use built-in functions.
"""


def run_timings():
    """
    Calculate the average time it took to run 10k given a number of
    times that have been entered by the user.
    """

    running_times = 0
    run_count = 0

    while recorded_time := input(f"Enter your 10k time: "):
        if not recorded_time:
            break
        running_times += float(recorded_time)
        run_count += 1

    return running_times / run_count


print(run_timings())
