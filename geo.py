import googlemaps

class RouteOptimizer:
    def __init__(self, api_key):
        self.client = googlemaps.Client(key=api_key)

    def optimize_route(self, addresses, start_address):
        result = self.client.directions(
            origin=start_address,
            destination=start_address,
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

api_key = ''
addresses = []

start_address = ''

route_optimizer = RouteOptimizer(api_key)
optimized_route = route_optimizer.optimize_route(addresses, start_address)

if optimized_route:
    print("Optimized Route:", optimized_route)
else:
    print("Error: Unable to optimize the route.")

