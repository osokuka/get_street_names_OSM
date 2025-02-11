# Street Extractor App 🗺️

Extract street names and coordinates from OpenStreetMap within defined polygon areas.

## 🇬🇧 English Guide

### 📌 Features
✅ Supports CSV & Excel input
✅ Extracts city, suburban area, street data with coordinates
✅ Uses OpenStreetMap (OSM) via Overpass API (no API key required)
✅ Saves output in Excel (.xlsx) format
✅ Console-based interface for easy usage

### 📥 Installation & Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install pandas geopandas osmnx openpyxl requests tqdm
```

### 📂 Input File Format
| Suburban Area | Coordinates |
|--------------|-------------|
| Suburban 1   | 42.369015, 21.151678 |
| Suburban 1   | 42.364132, 21.148277 |

💡 Each Suburban Area must have at least 3 points to form a polygon.

### 🚀 Usage Steps
1. Prepare your input file (CSV/Excel)
2. Run the script:
   ```bash
   python get_streetnames_fromOSM.py
   ```
3. Enter file paths when prompted
4. Wait for processing to complete

### 📊 Output Format
| City     | Suburban Area | Street Name | Latitude  | Longitude |
|----------|--------------|-------------|-----------|-----------|
| Pristina | Suburban 1   | Street A    | 42.36789  | 21.15234  |

### ⚠️ Important Notes
- Requires active internet connection
- Each area needs minimum 3 points
- Best for small/medium areas
- Coordinates must be in decimal format
- Results saved automatically in Excel

---

## 🇦🇱 Udhëzuesi Shqip

### 📌 Karakteristikat
✅ Pranim i të dhënave në CSV & Excel
✅ Nxjerrje e qytetit, zonës, rrugëve me koordinata
✅ Përdorim i OpenStreetMap përmes Overpass API (pa API key)
✅ Ruajtje automatike në Excel (.xlsx)
✅ Ndërfaqe e thjeshtë konzole

### 📥 Instalimi
```bash
# Krijo ambient virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# Instalo varësitë
pip install pandas geopandas osmnx openpyxl requests tqdm
```

### 📂 Formati i Hyrjes
| Zona Suburbane | Koordinatat |
|----------------|-------------|
| Zona 1         | 42.369015, 21.151678 |
| Zona 1         | 42.364132, 21.148277 |

💡 Çdo zonë kërkon minimum 3 pika për të formuar poligon.

### 🚀 Hapat e Përdorimit
1. Përgatit skedarin e hyrjes (CSV/Excel)
2. Ekzekuto skriptën:
   ```bash
   python get_streetnames_fromOSM.py
   ```
3. Vendos pozicionin e skedarëve kur kërkohet
4. Prit përfundimin e procesit

### 📊 Formati i Daljes
| Qyteti    | Zona Suburbane | Emri i Rrugës | Gjerësia | Gjatësia  |
|-----------|---------------|---------------|-----------|-----------|
| Prishtina | Zona 1       | Rruga A       | 42.36789  | 21.15234  |

### ⚠️ Shënime të Rëndësishme
- Kërkon lidhje interneti aktive
- Çdo zonë kërkon minimum 3 pika
- Ideal për zona të vogla/mesme
- Koordinatat duhet të jenë në format decimal
- Rezultatet ruhen automatikisht në Excel

---

💡 For support / Për ndihmë: [GitHub Issues](https://github.com/osokuka/get_street_names_OSM