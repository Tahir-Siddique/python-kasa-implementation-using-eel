import eel
import pyautogui #https://pypi.org/project/PyAutoGUI/

import asyncio
from kasa import SmartPlug, Discover
 
eel.init('views', allowed_extensions=['.js', '.html'])
    
@eel.expose
def new_window(target: str):
    eel.show(f"html/{target}")

@eel.expose
def get_data_from_python():
    return "DATA from python"



                       # Expose this function to Javascrip
  # Call a Javascript function

    


@eel.expose  
def turn_on_the_device():
    devices = asyncio.run(Discover.discover())
    print(f"Devices: {devices}")
    if devices:
        for addr, dev in devices.items():
            asyncio.run(dev.turn_on())
            return f"Device at {addr}: Turned on"
    else:
        return "NO DEVICES CONNECTED"
    
@eel.expose  
def turn_off_the_device():
    devices = asyncio.run(Discover.discover())
    print(f"Devices: {devices}")
    if devices:
        for addr, dev in devices.items():
            asyncio.run(dev.turn_off())
            return f"Device at {addr}: Turned off"
    else:
        return "NO DEVICES CONNECTED"
    
@eel.expose  
def current_state():
    devices = asyncio.run(Discover.discover())
    print(f"Devices: {devices}")
    if devices:
        for addr, dev in devices.items():
            asyncio.run(dev.update())
            state = asyncio.run(dev.is_on)
            if state:
                return f"Device at {addr}: Turned off"
            else:
                return f"Device at {addr}: Turned off"
    else:
        return "There is no Device connected to show Current State"
    
@eel.expose  
def get_system_info():
    devices = asyncio.run(Discover.discover())
    print(f"Devices: {devices}")
    if devices:
        for addr, dev in devices.items():
            sys_info = asyncio.run(dev.sys_info)
            return f"Device at {addr}: System Info - {sys_info}"
    else:
        return "There is no Device connected to show System INFO"

@eel.expose  
def get_emmeter_data():
    devices = asyncio.run(Discover.discover())
    print(f"Devices: {devices}")
    if devices:
        for addr, dev in devices.items():
            emmete_data = {}
            if dev.has_emeter:
                emeter_data = asyncio.run(dev.get_emeter_realtime())
                emeter_data[f"Device at {addr}"] = f"Voltage - {emeter_data['voltage']} , Current - {emeter_data['current']} , Power - {emeter_data['power']} , {emeter_data['total']}"
                return emmete_data      
    else:
        return "There is no Device connected to show Emmeter Data"



    # for addr in devices:
    #     print(addr)
        # if isinstance(dev, SmartPlug):
             
        #     dev.update()

        #     # Retrieve state information
        #     state =  dev.is_on
        #     return f"Device at {addr}: State - {state}"

            # # Turn the device on
            # await dev.turn_on()
            # print(f"Device at {addr}: Turned on")

            # # Turn the device off
            # await dev.turn_off()
            # print(f"Device at {addr}: Turned off")

            # # Retrieve energy consumption information
            # if dev.has_emeter:
            #     emeter_data = await dev.get_emeter_realtime()
            #     print(f"Device at {addr}: Voltage - {emeter_data['voltage']}")
            #     print(f"Device at {addr}: Current - {emeter_data['current']}")
            #     print(f"Device at {addr}: Power - {emeter_data['power']}")
            #     print(f"Device at {addr}: Total Energy - {emeter_data['total']}")

            # # Retrieve raw system information
            # sys_info = await dev.sys_info
            # print(f"Device at {addr}: System Info - {sys_info}")


eel.start(
    'templates/index.html',
    size=pyautogui.size(),
    jinja_templates='templates'
)
