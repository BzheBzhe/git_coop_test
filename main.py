import unit
import new_module.module as newmod
import sys

from utils.statuses import Status


status: Status = Status.ON  # Example status, can be set to Status.OFF or Status.UNKNOWN

if status == Status.ON:
    newmod.new_mod()
elif status == Status.OFF:
    unit.room(5)
elif status == Status.UNKNOWN:
    unit.hello()
else:
    print("Invalid status, please provide a valid status.", status, Status.ON, Status.OFF, Status.UNKNOWN)