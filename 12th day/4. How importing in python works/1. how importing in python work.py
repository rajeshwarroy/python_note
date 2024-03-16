from math import sqrt, pi
from math import pi, sqrt as s          # "sqrt" kea "s" dhorea niyeachi.
import math as math_builtin_python

result = sqrt(9)
print(result)                     # Output: 3.0

result = s(9) * pi                # 3*3.1416 = 9.4248; import ar somoy 'sqrt' kea 's' dhorea nichi, tai 's' used korchi.
print(result)

result = math_builtin_python.sqrt(9) * math_builtin_python.pi
print(result)




import math

from rajeshwar import welcome, roni     # import korchi "welcome" and roni "kea", "rajeshwar.py" name a file thakea.
# from rajeshwar import *                 # rajeshwar ak file achea, takea pura import kora hochea, and use kora jay jeakuno vabea.
#       uporer jea kuno akta use korlea hobea.


#   nichear tar moto korea use kora jay,
import rajeshwar as rr                  # import korchi "Rajeshwar.py" file kea, and oy file kea short name dichi "rr".


print(dir(math))                        # "math" ar sob function and ar vitorea ki ki achea sob print kora jay ay vabea. "dir( )" function ar madhomea.
print(math.nan, type(math.nan))         # A float value, nan (Not a Number),
                                        # The math.nan constant returns a floating-point nan (Not a Number) value. This value is not a legal number.
                                        # The nan constant is equivalent to float('nan').
welcome()                               #  "welcome" name a akta function kea print korchi.
print(roni)                             # "roni" name a akta Variable achea ta print korchi.

print('\n')
print(rr.roni)
rr.welcome()
