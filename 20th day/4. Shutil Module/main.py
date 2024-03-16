import shutil
import os
### shutil এর মাধ্যমে কপি, হার্ডকপি, মুভ করা হয়ে থাকে,


shutil.copy("main.py", "main2.py")      # এখানে main.py ফাইলকে কপি করে main২.py নাম এ কপি ফাইল করা।

shutil.copy2("main.py", "main3.py")     # পুরোপুরি কপি ফাইল তৈরি হয়, মূল ফাইল এর টাইম ডেট সহ।




# shutil.copytree("aabb", "aabbcc")                   # এখানে পুরা ফল্ডারকে কপি করা হয়।
# shutil.move("aabbcc/roni.txt", "roni.txt")          # মুভ করা হয়।
# os.remove("roni.txt")                               # ফাইল কে ডিলিট করা হয়।
