### Robert Olivares - robertolivares@csu.fullerton.edu
### Dylon Gaddi    - dylongaddi@csu.fullerton.edu

This Python program is designed to find common free time slots between two groups of people who have busy schedules and working periods. It can be used to identify suitable meeting times when multiple parties need to find a convenient time to meet. The program reads input data from a text file and writes the results to an output file.

## How to Use the Program

Follow these steps to use the program to find common free time slots:

1. **Input Data File**: Prepare an input text file (e.g., `input.txt`) with the following format:

   ```
   busy_schedule1 = [(start_time1, end_time1), (start_time2, end_time2), ...]
   working_period1 = (start_time, end_time)
   busy_schedule2 = [(start_time1, end_time1), (start_time2, end_time2), ...]
   working_period2 = (start_time, end_time)
   meeting_duration = duration_in_minutes
   ```

   - `busy_schedule1` and `busy_schedule2` are lists of busy time slots for two groups of people. Each time slot is represented as a tuple `(start_time, end_time)` where `start_time` and `end_time` are in HH:MM format.

   - `working_period1` and `working_period2` define the working hours for the two groups, represented as a tuple `(start_time, end_time)` in HH:MM format.

   - `meeting_duration` is the desired duration of the meeting in minutes.

   You can have multiple sets of these parameters in the input file for different groups.

2. **Run the Program**: Execute the Python script by running the following command in your terminal:

   ```
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of the Python script containing the program.

3. **Output Data File**: The program will generate an output text file (e.g., `output.txt`) that contains the common free time slots for each group. The output will be organized as follows:

   ```
   Group 1: [(start_time1, end_time1), (start_time2, end_time2), ...]
   Group 2: [(start_time1, end_time1), (start_time2, end_time2), ...]
   ...
   ```

   Each group's common free time slots are displayed in HH:MM format.

4. **Review Results**: Open the output file to view the common free time slots for each group. These slots represent suitable times for meetings when all groups are available.

## Example Input

Here's an example of how to structure the input data file:

```python
[('09:00', '10:30'), ('12:00', '13:00'), ('16:00', '18:00')]
('08:00', '20:00')
[('10:00', '11:30'), ('12:30', '14:30'), ('14:45', '15:30')]
('09:30', '17:00')
60
```

## Example Output

The program will generate output like this:

```
Group 1: [('10:30', '12:00'), ('13:00', '16:00'), ('18:00', '20:00')]
Group 2: [('11:30', '12:30'), ('15:30', '17:00')]
```

These are the common free time slots for each group when considering their busy schedules and working hours.
