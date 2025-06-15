import math
import random
import time
from typing import List, NamedTuple

# Structure to represent geographic coordinates (latitude, longitude, altitude)
class GeoCoord(NamedTuple):
    lat: float
    lon: float
    alt: float = 0.0  # Default altitude is 0

# Structure to represent ENU planar coordinates (East, North, Up)
class Point(NamedTuple):
    x: float
    y: float
    z: float = 0.0

# Reference point near the center of Seoul
ref_point = GeoCoord(37.56, 126.92, 0.0)

# Approximate LLA to ENU conversion (valid only for short distances)
def lla_to_enu_approx(ref_lla: GeoCoord, target: GeoCoord) -> Point:
    # Latitude scale: 1 degree ≈ 111 km, longitude varies with latitude
    lat_scale = 111000.0  # Meters per degree latitude
    lon_scale = math.cos(math.radians(ref_lla.lat)) * lat_scale  # Longitude correction

    # Calculate deltas from reference point
    delta_lat = target.lat - ref_lla.lat
    delta_lon = target.lon - ref_lla.lon

    # Approximate conversion to ENU (East, North)
    x_east = delta_lon * lon_scale
    y_north = delta_lat * lat_scale
    return Point(x_east, y_north)

# Ray-casting algorithm to determine if a point is inside a 2D polygon
def point_in_polygon(verts: List[Point], p: Point) -> bool:
    inside = False
    n = len(verts)
    px, py = p.x, p.y
    xj, yj = verts[-1].x, verts[-1].y  # Start from last point

    for i in range(n):
        xi, yi = verts[i].x, verts[i].y

        # Check if edge crosses the horizontal line at p.y
        intersect = ((yi > py) != (yj > py)) and \
                    (px < (xj - xi) * (py - yi) / (yj - yi + 1e-10) + xi)
        if intersect:
            inside = not inside  # Toggle inside/outside status

        xj, yj = xi, yi  # Current point becomes previous point for next loop

    return inside

# Generate test data: a polygon and 10,000 random geographic points
def generate_test_data():
    # Define a simple pentagon near Seoul
    polygon_lla = [
        GeoCoord(37.55, 126.90),
        GeoCoord(37.55, 126.95),
        GeoCoord(37.58, 126.96),
        GeoCoord(37.60, 126.93),
        GeoCoord(37.57, 126.89)
    ]

    point_list_lla = []
    for _ in range(10000):
        # Generate 10,000 random points in a wider area
        lat = 37.57 + random.random() * 1
        lon = 126.7 + random.random() * 1
        point_list_lla.append(GeoCoord(lat, lon))

    return polygon_lla, point_list_lla

def main():
    print("1. Generating test data (LLA)...")
    polygon_lla, point_list_lla = generate_test_data()

    print("2. Converting to ENU (approximate)...")
    start_convert = time.time()

    # Convert polygon and test points to ENU coordinates
    polygon_enu = [lla_to_enu_approx(ref_point, geo) for geo in polygon_lla]
    point_list_enu = [lla_to_enu_approx(ref_point, geo) for geo in point_list_lla]

    end_convert = time.time()

    print("3. Polygon containment check...")
    start_judge = time.time()

    # Check if each point is inside the polygon
    results = [point_in_polygon(polygon_enu, pt) for pt in point_list_enu]

    end_judge = time.time()

    # Count results
    correct_inside = sum(results)
    correct_outside = len(results) - correct_inside
    total_time = (end_judge - start_judge) + (end_convert - start_convert)

    # Print results
    print(f"\nTotal points: {len(results)}")
    print("\n📊 Classification Summary:")
    print(f"- Points classified as inside: {correct_inside}")
    print(f"- Points classified as outside: {correct_outside}")

    print("\n⏱️ Timing Info:")
    print(f"- ENU conversion time: {end_convert - start_convert:.4f} sec")
    print(f"- Polygon judgment time: {end_judge - start_judge:.4f} sec")
    print(f"- Total time: {total_time:.4f} sec")
    print(f"- Average judgment time: {(end_judge - start_judge) / len(results):.6f} sec")

if __name__ == "__main__":
    main()
