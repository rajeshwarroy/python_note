# ডেকোরেটর হয় ওই ফাংশন জেএ ফাংশন অন্য ফাংশন এর ডাটা চেঞ্জ কোরিয়া রিটান  করে থাকে। মামে ফাংশন আপগ্রেড কোরিয়া রিটান  কোরিয়া থাকে ।


def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx


@greet   # "@greet" hochea decorator,
def hello():
    print("hello world")

hello()

# greet(hello)()

print('\n\n')








def greet(fx):
  def mfx(*args, **kwargs):                 # ""*args"" jotogulo Argument achea sobgulokea neaoyar niyom as a topol, "**kwargs" a hochea Dictionary sob argulent neaoyar key value  ar upoor
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")



# def add(a, b):
#   print(a+b)
# hello()
# greet(add)(1, 2)
# # #or 2 tai akoy kaj
@greet
def add(a, b):
  print(a+b)
hello()
add(1, 2)
