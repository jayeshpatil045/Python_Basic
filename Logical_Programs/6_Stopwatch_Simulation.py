'''
@Author: Jayesh Patil


@Date: 2024-13-08 


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-13-08 01:28 PM


@Title :  Simulate Stopwatch Program
'''
import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()  # Capture the start time

    input("Press Enter to stop the stopwatch...")
    end_time = time.time()  # Capture the end time

    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    stopwatch()
