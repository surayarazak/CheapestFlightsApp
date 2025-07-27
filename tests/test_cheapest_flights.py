import unittest
import sys
import os

# Add the parent directory to the sys.path to allow importing find_cheapest_price
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from find_cheapest_price import find_cheapest_price

class TestCheapestFlights(unittest.TestCase):

    def test_example_1(self):
        n = 4
        flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
        src = 0
        dst = 3
        k = 1
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 700)

    def test_example_2(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 200)

    def test_example_3(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 500)

    def test_unreachable_destination(self):
        n = 3
        flights = [[0,1,100]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), -1)

    def test_no_flights(self):
        n = 5
        flights = []
        src = 0
        dst = 4
        k = 2
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), -1)

    def test_k_equal_to_n_minus_1(self):
        # A fully connected path
        n = 3
        flights = [[0,1,10],[1,2,10],[0,2,100]]
        src = 0
        dst = 2
        k = n - 1 # Max possible stops
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 20) # 0 -> 1 -> 2

    def test_larger_k_does_not_find_worse_path(self):
        # Path 0->1->2 (cost 200, 1 stop) vs 0->2 (cost 500, 0 stops)
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 2 # Allowing more stops should still pick the cheapest valid path
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 200)

    def test_multiple_paths_same_stops(self):
        n = 4
        flights = [[0,1,50],[0,2,100],[1,3,200],[2,3,50]]
        src = 0
        dst = 3
        k = 1 # 0->1->3 (250) vs 0->2->3 (150)
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 150)

    def test_zero_stops_direct_flight(self):
        n = 2
        flights = [[0,1,500]]
        src = 0
        dst = 1
        k = 0
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 500)

    def test_zero_stops_no_direct_flight(self):
        n = 3
        flights = [[0,1,100],[1,2,100]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), -1)

    def test_large_prices(self):
        n = 3
        flights = [[0,1,10000],[1,2,10000]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 20000)

    def test_complex_graph(self):
        n = 5
        flights = [
            [0,1,10],[0,2,20],[0,3,100],
            [1,2,10],[1,3,20],
            [2,4,30],
            [3,4,10]
        ]
        src = 0
        dst = 4
        k = 2 # 0->1->3->4 (10+20+10 = 40)
              # 0->2->4 (20+30 = 50)
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 40)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)