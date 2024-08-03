from diary import monthly
from diary import daily

birth_angelo = monthly.monthly_note(2024,9,'Month of my birthday',True)
monthly.modify_monthly_description(birth_angelo,'Month of my 39 birthday')
print(monthly.convert_monthly_to_string(birth_angelo))