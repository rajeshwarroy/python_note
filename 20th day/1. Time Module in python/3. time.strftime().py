import time

t = time.localtime()                                        # t এর মধ্যে লোকাল টাইম তাকে নেওয়া হয়েছে।
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)      # "%Y-%m-%d %H:%M:%S"  এটা হচ্ছে সিকুয়েন্স,  কীভাবে কীভাবে প্রিন্ট হবে।

print(formatted_time)
# Output: 2022-11-08 08:45:33
