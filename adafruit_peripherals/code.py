# Recreating the code for the experiments using my library
import adafruit_peripherals

hardware = Facade()

# moisture level
MOISTURE_LEVEL = 0.5

# date time setup
r = rtc.RTC()
r.datetime = time.struct_time((2022, 1, 1, 0, 0, 0, 0, 0, 0))

# greenlight
hardware.setColourLED((0,255,0))

try:
    with open("/test.txt", a) as f:
        while True:
            curr_dt = r.datetime
            curr_t = "{0}:{1}".format(curr_dt.tm_hour, curr_dt.tm_min)
            temp = hardware.getTemperature
            bef_moist = hardware.getMoistureLevel
            is_water = False
            curr_moist = bef_moist

            if curr_moist < MOISTURE_LEVEL:
                is_water = True
                hardware.motorTimer(0.5)
                curr_moist = hardware.getMoistureLevel()
            
            after_moist = hardware.getMoistureLevel()
            curr_status = "{day}, {t}, {temp}, {b_moist}, {is_water}, {a_moist}\n".format(
                day = curr_dt.tm_mday, t = curr_t,
                temp = temp, b_moist = bef_moist,
                is_water = is_water, a_moist = after_moist)
            ex.write(curr_status)
            print(curr_status)
            ex.flush()

            # sleep for an hour
            curr_hour = curr_dt.tm_hour
            if curr_hour == 23:
                next_hour = 0
            else:
                next_hour = curr_hour + 1

            while r.datetime.tm_hour != next_hour:
                time.sleep(1)
except OSError as e:
    if e.args[0] == 28:
        t = r.datetime
        print("Storage is full {0}".format(t))
    else:
        print(e)
        