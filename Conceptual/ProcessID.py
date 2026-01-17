# program is used to get process Pid and PPID

import os

def main():
    print("PID of running process is : ",os.getpid())
    print("PPID of running process is : ",os.getppid())


if __name__ == "__main__":
    main()


# output :

# when we run the program as process using command prompt process so that's why PPID is same 

# PID of running process is :  6356
# PPID of running process is :  5885    # PPID

# PID of running process is :  6365
# PPID of running process is :  5885    # PPID

# PID of running process is :  6366
# PPID of running process is :  5885    # PPID

# PID of running process is :  6367
# PPID of running process is :  5885    # PPID
