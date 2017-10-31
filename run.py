#!/usr/bin/env python3

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import sys, time
from pycalima.Calima import Calima

# Here you can specify your Calimas MAC address and pincode
# Address you can find by using cmdline.poy script and -l parameter
# Pincode is found on the backside of the manual or on one of the 
# feet of the motor plug component
fan = Calima("58:2b:db:00:7b:a2", "03155106")


try:
#  print(fan.getAlias())
#  print(fan.getState())


  # If Clock is not set then there has been a power failure, 
  # so just in case we will write the settings to Calima and set time
  if fan.getIsClockSet() == "02":
    print("Clock is not set, setting current time and other parameters")
    # Lets preconfigure Calima by setting these values
  
    # Start off by setting time and then wait 2 seconds for it to settle before polling for time
    print(fan.setTimeToNow())
    time.sleep(2)
    #fan.getTime()
  
    # Setting Fan speed, I am not using light sensor therefore same value in fields 2 and 3
    fan.setFanSpeedSettings(2250,975,975)

    # Sets humidity sensivitity and light sensitivity. If set to 0 then sensor triggering will be off
    print(fan.setSensorsSensitivity(2,0))
    #fan.getSensorsSensitivity()
  
    # Set Light sensor delay and running times. Just setting these even if I do not use light sensor for now.
    print(fan.setLightSensorSettings(0,5))
    #fan.getLightSensorSettings()
  
    # Set automatic purge cycles which is max speed for X minutes every 12 hours, 0=disabled, 1=30min, 2=60min, 3=90min
    # Disable it for now as I want to control it from other Smart Home systems
    print(fan.setAutomaticCycles(0))
    #fan.getAutomaticCycles()
  
    # Setting Silent hours
    print(fan.setSilentHours(1,22,0,6,0))
    #fan.getSilentHours()
  
    # Set trickle days
    print(fan.setTrickleDays(1,1))
    #fan.getTrickleDays()

  print(fan.getStateShort())

except Exception as e:
  print(e)
  fan.disconnect()
