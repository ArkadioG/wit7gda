import pyflight
import pickle
from results_printer import print_results
from secrets import API_KEY

# seting our QPX api key - from Google APIs console
pyflight.set_api_key(API_KEY)
# pyflight.set_queries_per_day(50)

# define our trip
# slice is a one way route - from where - to where you want to fly
stage1 = pyflight.Slice("GDN", "NYC", "2017-11-24")
stage2 = pyflight.Slice("NYC", "GDN", "2017-12-12")

# you can change properties of slice
# stage1.latest_departure_time = "2017-11-26"

# preparing request to QPX
my_trip = pyflight.Request()

# adding slices/routes to trip
my_trip.add_slice(stage1)
my_trip.add_slice(stage2)

# adding details
my_trip.adult_count = 2
my_trip.children_count = 0

# sale country - prices in currency of this country
my_trip.sale_country = "PL"

# number of returned solutions
my_trip.solution_count = 10

# send request to QPX
print("Sending request...")
solutions = my_trip.send_sync()

print("Dumping data")
with open("results_3.pckl", "wb") as file:
    pickle.dump(solutions, file)

print("Done.")

# print formatted output
print_results(solutions)
