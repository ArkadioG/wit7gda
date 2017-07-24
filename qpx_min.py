import pyflight
from secrets import API_KEY

pyflight.set_api_key(API_KEY)

my_trip = pyflight.Request()
my_trip.adult_count = 1

stage1 = pyflight.Slice("CPH", "NYC", "2017-11-24")
my_trip.add_slice(stage1)

solutions = my_trip.send_sync()
