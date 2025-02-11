# Street Extractor App

Extract street names and coordinates from OpenStreetMap within defined polygon areas.

## 🇬🇧 English

### Features
- CSV & Excel input support
- Extracts city, suburban area, street data with coordinates
- Uses OpenStreetMap (OSM) via Overpass API
- Excel (.xlsx) output format
- Simple console interface

### Setup
```bash
# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install pandas geopandas osmnx openpyxl requests tqdm
```

### Usage
1. Prepare input file (CSV/Excel) with columns:
   ```
   Suburban Area | Coordinates
   Area 1       | 42.369015, 21.151678
   Area 1       | 42.364132, 21.148277
   ```
   Note: Each area needs 3+ points to form a polygon

2. Run the script:
   ```bash
   python get_streetnames_fromOSM.py
   ```

3. Follow the prompts to specify input/output paths

### Output Format
| City     | Suburban Area | Street Name | Latitude  | Longitude |
|----------|--------------|-------------|-----------|-----------|
| Pristina | Area 1      | Street A    | 42.36789  | 21.15234  |

## 🇦🇱 Shqip

### Karakteristikat
- Pranimi i të dhënave në CSV & Excel
- Nxjerrja e qytetit, zonës, rrugëve me koordinata
- Përdorimi i OpenStreetMap përmes Overpass API
- Dalje në format Excel (.xlsx)
- Ndërfaqe e thjeshtë konzole

### Instalimi
```bash
# Krijo ambient virtual (opsional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# Instalo varësitë
pip install pandas geopandas osmnx openpyxl requests tqdm
```

### Përdorimi
1. Përgatit skedarin (CSV/Excel) me kolonat:
   ```
   Zona Suburbane | Koordinatat
   Zona 1         | 42.369015, 21.151678
   Zona 1         | 42.364132, 21.148277
   ```
   Shënim: Çdo zonë kërkon 3+ pika për poligon

2. Ekzekuto skriptën:
   ```bash
   python get_streetnames_fromOSM.py
   ```

3. Ndiq udhëzimet për të specifikuar skedarët hyrës/dalës

⚠️ Kërkon lidhje interneti aktive për të marrë të dhënat nga OpenStreetMap.