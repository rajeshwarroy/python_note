# time.time()


import time

def usingWhile():                           # ইউজ হোয়াইল লুপ
    i = 0
    while i<100:
        i = i + 1
        print(i)
def usingFor():                             # ইউজ ফর লুপ
    for i in range(100):
        print(i)

timeuse = time.time()       #   "timeuse" এটা নিজের মতো যেকুনো নাম দেওয়া যাবে।
                # time() ->  floating point number.      Return the current time in seconds since the Epoch. Fractions present id the system clock provides them.

usingWhile()
print(time.time() - timeuse)                # কত সময় লাগে তা বের করা  যায়।
t1 = time.time() - timeuse                  # কত সময় লাগে তা বের করা  যায় ,,,, তা 't1' এর মধ্যে রেখে দিয়েছি।

print('\n')
somoy = time.time()                         #   "somoy" এটা নিজের মতো যেকুনো নাম দেওয়া যাবে।
usingFor()
print(time.time() - somoy)                  # কত সময় লাগে তা বের করা  যায়।
print(t1)                                   # 't1' এর মধ্যে রেখে দেওয়া ম্যান প্রিন্ট করি।
