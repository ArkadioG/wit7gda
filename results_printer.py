from pyflight.results import Result


def print_results(solutions: Result):
    for i, trip in enumerate(solutions.trips):
        print(20 * "-")
        print(f"\nPropozycja nr. {i + 1}")
        print(f"Cena całkowita: {trip.total_price}")

        for k, route in enumerate(trip.routes):
            print(f"\nRoute / Slice: {k + 1}")
            print(f"Czas podróży: {route.duration} minut")

            for j, segment in enumerate(route.segments):
                print(f"\nEtap {j + 1}".ljust(8))
                print(f"Przewoźnik: {segment.flight_carrier}")

                for flight in segment.flights:
                    print(f"Lot z {flight.origin} do {flight.destination}")
                    print(f"Wylot: {flight.departure_time}")
                    print(f"Przylot: {flight.arrival_time}")
