import random

otp = "".join([str(random.randint(0, 9)) for _ in range(6)])
print("Your OTP:", otp)

otp = "".join([str(random.randint(0, 9)) for _ in range(4)])
print("Your OTP:", otp)