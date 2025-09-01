from openpyxl import Workbook
from pathlib import Path

# Output path (project root)
OUTPUT_XLSX = Path(__file__).resolve().parents[2] / "colleges.xlsx"

# 25 well-known design schools (city, country)
SCHOOLS = [
    ("Parsons School of Design", "New York", "USA"),
    ("Rhode Island School of Design", "Providence", "USA"),
    ("Pratt Institute", "Brooklyn", "USA"),
    ("School of Visual Arts", "New York", "USA"),
    ("California Institute of the Arts", "Valencia", "USA"),
    ("ArtCenter College of Design", "Pasadena", "USA"),
    ("Savannah College of Art and Design", "Savannah", "USA"),
    ("Maryland Institute College of Art", "Baltimore", "USA"),
    ("Carnegie Mellon School of Design", "Pittsburgh", "USA"),
    ("IIT Institute of Design", "Chicago", "USA"),
    ("Royal College of Art", "London", "UK"),
    ("Central Saint Martins (UAL)", "London", "UK"),
    ("Royal Danish Academy", "Copenhagen", "Denmark"),
    ("Politecnico di Milano", "Milan", "Italy"),
    ("Domus Academy", "Milan", "Italy"),
    ("Delft University of Technology", "Delft", "Netherlands"),
    ("Umeå Institute of Design", "Umeå", "Sweden"),
    ("Aalto University", "Helsinki", "Finland"),
    ("Zurich University of the Arts", "Zurich", "Switzerland"),
    ("Bauhaus-Universität Weimar", "Weimar", "Germany"),
    ("The Hong Kong Polytechnic University School of Design", "Hong Kong", "Hong Kong"),
    ("Tsinghua University – Academy of Arts & Design", "Beijing", "China"),
    ("Tongji University – College of Design & Innovation", "Shanghai", "China"),
    ("National University of Singapore", "Singapore", "Singapore"),
    ("RMIT University", "Melbourne", "Australia"),
]

# Program templates per school to reach 100 rows (4 per school × 25 = 100)
PROGRAMS = [
    ("BFA Graphic Design", "Graphic Design", "Bachelor"),
    ("BDes Product Design", "Product Design", "Bachelor"),
    ("MDes UX/UI", "UX/UI", "Master"),
    ("BA Fashion Design", "Fashion", "Bachelor"),
]

# Tuition ranges by country group (very rough placeholders for seeding)
REGION_TUITION = {
    "USA": (30000, 60000),
    "UK": (20000, 40000),
    "Denmark": (10000, 25000),
    "Italy": (15000, 30000),
    "Netherlands": (15000, 30000),
    "Sweden": (10000, 25000),
    "Finland": (10000, 20000),
    "Switzerland": (20000, 45000),
    "Germany": (10000, 20000),
    "Hong Kong": (20000, 35000),
    "China": (10000, 25000),
    "Singapore": (20000, 40000),
    "Australia": (20000, 40000),
}


def pick_tuition(country: str):
    base = REGION_TUITION.get(country, (15000, 30000))
    return base


def build_workbook():
    wb = Workbook()
    ws = wb.active
    ws.title = "colleges"

    # Required columns only (as per importer)
    headers = [
        "name",
        "location_city",
        "location_country",
        "program_name",
        "program_type",
        "degree_level",
        "tuition_min",
        "tuition_max",
    ]
    ws.append(headers)

    rows = 0
    for name, city, country in SCHOOLS:
        tmin, tmax = pick_tuition(country)
        for program_name, program_type, degree_level in PROGRAMS:
            ws.append([
                name,
                city,
                country,
                program_name,
                program_type,
                degree_level,
                tmin,
                tmax,
            ])
            rows += 1

    wb.save(OUTPUT_XLSX)
    return OUTPUT_XLSX, rows


if __name__ == "__main__":
    path, count = build_workbook()
    print(f"Wrote {count} rows to {path}") 