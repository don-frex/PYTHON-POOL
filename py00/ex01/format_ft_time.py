import time
from datetime import datetime

current_time = time.time()
formatted_date = datetime.now().strftime("%b %d %Y")

print(
    f"Seconds since January 1, 1970: {current_time:,.4f} "
    f"or {current_time:.2e} in scientific notation"
)
print(formatted_date)
