import pandas as pd
import geopandas as gpd
import osmnx as ox
import requests
import os
from shapely.geometry import Polygon, Point
from tqdm import tqdm

# Function to read input file (CSV or Excel)
def read_input_file(file_path):
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext == ".csv":
        df = pd.read_csv(file_path)
    elif file_ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")

    # Ensure proper column names
    if "Suburban Area" not in df.columns or "Coordinates" not in df.columns:
        raise ValueError("File must have 'Suburban Area' and 'Coordinates' columns.")

    # Split 'Coordinates' into 'Latitude' and 'Longitude'
    df[['Latitude', 'Longitude']] = df['Coordinates'].str.split(',', expand=True).astype(float)
    
    return df

# Function to create polygons from coordinates
def create_polygons(df):
    polygons = {}
    
    for area, group in df.groupby("Suburban Area"):
        coords = list(zip(group["Longitude"], group["Latitude"]))  # (lon, lat) for OSM format
        if len(coords) < 3:
            print(f"Skipping {area}: Not enough points to form a polygon.")
            continue
        polygons[area] = Polygon(coords)
    
    return polygons

# Function to query OpenStreetMap using Overpass API
def get_streets_within_polygon(polygon):
    query = f"""
    [out:json];
    way["highway"](poly:"{' '.join(f'{lat} {lon}' for lon, lat in polygon.exterior.coords)}");
    out center;
    """
    
    response = requests.get("http://overpass-api.de/api/interpreter", params={"data": query})
    
    if response.status_code != 200:
        print("Error fetching data from Overpass API.")
        return []
    
    data = response.json()
    streets = []
    
    for element in data.get("elements", []):
        if "tags" in element and "name" in element["tags"]:
            name = element["tags"]["name"]
            center = element.get("center", {})
            midpoint = (center.get("lat", None), center.get("lon", None))
            if None not in midpoint:
                streets.append((name, midpoint))
    
    return streets

# Function to get city name from a coordinate
def get_city_name(lat, lon):
    try:
        location = ox.geocode((lat, lon))
        return location.get("address", {}).get("city", "Unknown")
    except:
        return "Unknown"

# Main function to process the file and export results
def process_file(input_path, output_path=None):
    print("\n🔄 Reading input file...")
    df = read_input_file(input_path)
    
    print("📍 Creating polygons from coordinates...")
    polygons = create_polygons(df)

    results = []
    
    print("🌍 Querying OpenStreetMap for street data...")
    for suburban_area, polygon in tqdm(polygons.items(), desc="Processing Suburban Areas"):
        streets = get_streets_within_polygon(polygon)
        
        for street_name, (lat, lon) in streets:
            city = get_city_name(lat, lon)
            results.append([city, suburban_area, street_name, lat, lon])

    # Convert to DataFrame
    result_df = pd.DataFrame(results, columns=["City", "Suburban Area", "Street Name", "Latitude", "Longitude"])
    
    # Determine output path
    if not output_path:
        output_path = os.path.splitext(input_path)[0] + "_output.xlsx"

    print(f"💾 Saving results to {output_path} ...")
    result_df.to_excel(output_path, index=False)
    print("✅ Done! Output file created.")

# Console interface
if __name__ == "__main__":
    print("\n📌 Welcome to the Street Extractor App! 🚀")
    file_path = input("📂 Enter the path of your CSV/Excel file: ").strip()
    
    if not os.path.exists(file_path):
        print("❌ Error: File not found. Please check the path and try again.")
    else:
        output_path = input("💾 Enter output file path (or press Enter to save in the same folder): ").strip()
        output_path = output_path if output_path else None
        process_file(file_path, output_path)
