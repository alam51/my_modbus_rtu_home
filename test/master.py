"""
Initialization:
1. Load Configs: Bay name, SS Name, Alarm limits etc in variable / array
2. Load System : Get system param settings like ct, pt ratio etc and store in variable / array

Thread 1 :
    Loop: read values from Modbus, store in a DF (10 devices, 1/2 time as appropriate); Async Push values to DB
            Avoid bottleneck

Thread 2 :
    Loop: Get values from the latest DF (not DB) and update GUI (refresh rate 300ms)

In all cases error handling and logging is to be done
"""
