# Route Optimizer

This Route Optimizer uses the Google Maps API to find the most efficient route between a list of addresses. The program reads a list of addresses from a CSV file and takes a starting address, then returns the optimized route.

## Dependencies

- `googlemaps` - To install, run `pip install -U googlemaps`.
- `csv` - Included in Python's standard library.

## Usage

1. Set your Google Maps API key:

```
python
api_key = 'YOUR_API_KEY'
```

2. Provide the path to a CSV file containing the addresses one per line

```
csv_file_path = 'addresses.csv'  # Replace with your CSV file path
```

3. Provide a starting address

```
start_address = '7 Corporate Dr, North Haven, CT'
```

4. REad the addresses from the CSV file:

```
addresses = read_addresses_from_csv(csv_file_path)
```

5. Create an instance of the `RouteOptimizer` class and call the `optimize_route` method:

```
route_optimizer = RouteOptimizer(api_key)
optimized_route = route_optimizer.optimize_route(addresses, start_address)
```

6. Print the optimized route:

```
if optimized_route:
    print("Optimized Route:")
    for address in optimized_route:
        print(address)
else:
    print("Error: Unable to optimize the route.")
```

## Code Overview

### RouteOptimizer Class

The `RouteOptimizer` class handles the optimization of the route by utilizing the Google Maps API. It has the following methods:

#### `__init__(self, api_key)`
Initializes the class with the given Google Maps API key.

#### `optimize_route(self, addresses, start_address)`
Takes a list of addresses and a starting address, and returns an optimized route based on the Google Maps API directions.

The `optimize_route` method sends a request to the Google Maps API with the given list of addresses, the starting address, and the request to optimize waypoints. If the API returns a valid response, the method creates an optimized route by reordering the list of addresses based on the optimized order provided by the API. If the API does not return a valid response, the method returns `None`.

### read_addresses_from_csv(file_path)

This function reads a list of addresses from a CSV file and returns them as a list. The file should have one address per line.

