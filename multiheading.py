# multithreading =  Used to perform multiple tasks concurrently(multitasking)
#                   Good for input/output bound tasks like reading files or fetching data from APIs
#                   threading.thread(target = my_function)


# What is a thread?

# A thread is like hiring another worker.

# Without threads:

# You
#  ├─ Walk dog
#  ├─ Take out trash
#  └─ Get mail

# One person does everything.

# With threads:

# You
#  ├─ Worker 1 → Walk dog
#  ├─ Worker 2 → Take out trash
#  └─ Worker 3 → Get mail

# Now multiple workers can work simultaneously.


import threading
import time

def walk_dog(first_name, last_name):
    time.sleep(8)
    print(f"You Finished Walking {first_name}-{last_name}")

def take_out_trash():
    time.sleep(2)
    print("You Take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# walk_dog()
# take_out_trash()
# get_mail()
chore1 = threading.Thread(target = walk_dog, args = ('scooby', 'Doo' ))
chore1.start()

chore2 = threading.Thread(target = take_out_trash)
chore2.start()


chore3 = threading.Thread(target = get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()


print("ALL chores complete")

# 1. Define thread (nothing runs yet)
# 2. start() → thread begins running
# 3. function executes in background
# 4. join() → wait for it to finish

# What happens over time?

# After 2 seconds:

# You Take out the trash

# Worker 2 is done.
# -----------------------------

# After 4 seconds:

# You get the mail

# Worker 3 is done.
# ------------------------------
# After 8 seconds:

# You Finished Walking scooby-Doo

# Worker 1 is done.
# ----------------------------
# Total runtime?

# Not:

# 14 seconds

# but approximately:

# 8 seconds

# Because all tasks were happening at the same time.

# The slowest task determines the total time.