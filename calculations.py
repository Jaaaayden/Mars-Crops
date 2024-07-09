import math

"""
eto is a calculated value based on the martian environment measured in mm/day of water;
placeholder can be 3mm/day
Kc is the crop coefficient (depends on the plant, as well as the stage)
the durations are days that the crop will be in that stage
area is the area of the crop in square meters FROM USER INPUT
time is the time period over which the water will be consumed FROM USER INPUT
"""

def waterConsumed(eto, kc_ini, kc_mid, kc_late, iniDuration, midDuration, lateDuration, area, time):
  cycleDuration = iniDuration + midDuration + lateDuration
  total_consumption = 0
  etc_ini = eto * kc_ini
  etc_mid = eto*kc_mid
  etc_late = eto*kc_late
  ini_consumption = etc_ini * iniDuration
  mid_consumption = etc_mid * midDuration
  late_consumption = etc_late * lateDuration
  total_consumption += (time//cycleDuration)*area*(ini_consumption + mid_consumption + late_consumption)
  daysLeft = time%cycleDuration
  if(daysLeft == 0):
    return (total_consumption)
  elif(daysLeft < iniDuration):
    return (total_consumption + area*etc_ini*daysLeft)
  elif(daysLeft < iniDuration+midDuration):
    return (total_consumption + area*(etc_ini*iniDuration + etc_mid*(daysLeft-iniDuration)))
  else:
    return (total_consumption + area*(etc_ini*iniDuration + etc_mid*midDuration + etc_late*(daysLeft-iniDuration-midDuration)))