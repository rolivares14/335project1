from datetime import datetime

# Helper function to convert HH:MM to minutes past midnight
def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

# Main function
def find_common_free_time(busy_schedule1, busy_schedule2, working_period1, working_period2, meeting_duration):
    common_free_time = [] # List to store common free time slots

    # Convert busy schedules to minutes and sort them
    busy1_minutes = [(time_to_minutes(start), time_to_minutes(end)) for start, end in busy_schedule1]
    busy2_minutes = [(time_to_minutes(start), time_to_minutes(end)) for start, end in busy_schedule2]

    # Merge the busy schedules into one list and sort it
    merged_busy = busy1_minutes + busy2_minutes
    merged_busy.sort()

    # Find the intersection of the working periods
    free_from = max(time_to_minutes(working_period1[0]), time_to_minutes(working_period2[0]))
    free_to = min(time_to_minutes(working_period1[1]), time_to_minutes(working_period2[1]))

    # Loop through the merged busy schedule to find free slots
    for start, end in merged_busy:
        if start > free_from:
            if start - free_from >= meeting_duration:
                common_free_time.append((free_from, start))
        free_from = max(free_from, end)

    # Check for a free slot at the end of the day
    if free_to - free_from >= meeting_duration:
        common_free_time.append((free_from, free_to))

    # Convert the free slots back to HH:MM format
    converted_free_time = []
    for start, end in common_free_time:
        start_str = f'{start // 60}:{start % 60:02d}'
        end_str = f'{end // 60}:{end % 60:02d}'
        converted_free_time.append((start_str, end_str))
    return converted_free_time

with open('input.txt', 'r') as f:
    lines = f.readlines()

with open('output.txt', 'w') as f:
    for i in range(0, len(lines), 5):
        busy_schedule1 = eval(lines[i].strip())
        working_period1 = eval(lines[i + 1].strip())
        busy_schedule2 = eval(lines[i + 2].strip())
        working_period2 = eval(lines[i + 3].strip())
        meeting_duration = int(lines[i + 4].strip())

        result = find_common_free_time(busy_schedule1, busy_schedule2, working_period1, working_period2, meeting_duration)
        f.write(f'Group {(i // 5) + 1}: {result}\n')
