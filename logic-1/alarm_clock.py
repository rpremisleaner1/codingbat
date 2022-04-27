def alarm_clock(day, vacation):
    if 1 <= day <= 5 and vacation is False:
        return '10:00'
    return 'off'

print(alarm_clock(1, False))