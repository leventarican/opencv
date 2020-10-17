import setup_path # for detect airsim
import airsim
import time

# https://microsoft.github.io/AirSim/apis/
# unzip Blocks.zip
# ./Blocks/Blocks.sh

def car_state():
    car_state = client.getCarState()
    print(f"speed: {car_state.speed}; gear: {car_state.gear}")

# connect to the AirSim simulator 
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
client.reset()
car_controls = airsim.CarControls()

sleep_in_s = 1
for idx in range(60):
    time.sleep(sleep_in_s)
    car_state()
    car_controls.throttle = 100.0
    car_controls.steering = 0
    client.setCarControls(car_controls)

car_controls.brake = 1
# client.reset()
client.enableApiControl(False)
