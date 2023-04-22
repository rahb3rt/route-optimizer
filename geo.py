import csv
import googlemaps


class RouteOptimizer:
    def __init__(self, api_key, start_address='', csv_file_path='addresses.csv'):
        self.client = googlemaps.Client(key=api_key)
        self.start_address = start_address
        self.csv_file_path = csv_file_path

    def optimize_route(self):
        addresses = self.read_addresses_from_csv()
        result = self.client.directions(
            origin=self.start_address,
            destination=self.start_address,
            waypoints=addresses,
            optimize_waypoints=True,
            mode='driving'
        )

        if result:
            optimized_order = result[0]['waypoint_order']
            optimized_route = [addresses[i] for i in optimized_order]
            return optimized_route
        else:
            return None

    def read_addresses_from_csv(self):
        addresses = []
        with open(self.csv_file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                addresses.append(row[0])
        return addresses

    def print_optimized_route(self, optimized_route):
        if optimized_route:
            print("Optimized Route:")
            for address in optimized_route:
                print(address)
        else:
            print("Error: Unable to optimize the route.")


api_key = ''
csv_file_path = 'addresses.csv'  # Replace with your CSV file path
start_address = ''

route_optimizer = RouteOptimizer(api_key, start_address, csv_file_path)
optimized_route = route_optimizer.optimize_route()
route_optimizer.print_optimized_route(optimized_route)

