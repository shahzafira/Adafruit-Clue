# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Zafira Shah for KCL Final Project
#
# SPDX-License-Identifier: Unlicense

import adafruit_peripherals
hardware = Facade()

curr_dt = r.datetime
curr_t = "{0}:{1}".format(curr_dt.tm_hour, curr_dt.tm_min)
temp = hardware.getTemperature
curr_moist = hardware.getMoistureLevel
hardware.motorTimer(0.5)

curr_status = "{day}, {t}, {temp}, {c_moist}\n".format(
    day = curr_dt.tm_mday, t = curr_t,
    temp = temp, c_moist = curr_moist)

print(curr_status)