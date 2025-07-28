from typing import List

def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """
    Finds the cheapest price from src to dst with at most k stops using a Bellman-Ford like approach.

    Args:
        n (int): The number of cities.
        flights (List[List[int]]): A list of flights, where each flight is [from, to, price].
        src (int): The source city.
        dst (int): The destination city.
        k (int): The maximum number of stops allowed.

    Returns:
        int: The cheapest price, or -1 if no such route exists.
    """
    # Initialize prices array with infinity for all cities, and 0 for the source
    prices = [float('inf')] * n
    prices[src] = 0

    # We iterate k+1 times, where each iteration represents allowing one more stop.
    # k stops means k+1 edges/flights.
    # The loop runs k+1 times (from 0 to k inclusive).
    for _ in range(k + 1):
        # Create a temporary array to store prices for the current iteration.
        # This is crucial because updates must be based on prices from the *previous* stop count.
        # If we update `prices` directly, it's like allowing more than `i` stops in the current iteration.
        temp_prices = list(prices) # Make a copy of the prices from the previous iteration

        # Iterate through all flights
        for fro, to, price in flights:
            # If the 'from' city was reachable in the previous iteration (i.e., its price is not infinity)
            # and a path exists to 'to' from 'fro'
            if prices[fro] != float('inf'):
                # Update the price to 'to' if a cheaper path is found
                if prices[fro] + price < temp_prices[to]:
                    temp_prices[to] = prices[fro] + price

        # After checking all flights for the current stop count, update the main prices array
        prices = temp_prices

    # After k+1 iterations, prices[dst] will hold the cheapest price to reach 'dst'
    # with at most k stops (or k+1 edges).
    return prices[dst] if prices[dst] != float('inf') else -1