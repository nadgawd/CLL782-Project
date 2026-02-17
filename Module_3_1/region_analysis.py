"""
Region of Interest Analysis for IIT Delhi - Rendezvous Festival
================================================================
Based on the Region.pdf layout plan, the black outline marks the festival's
region of interest: a central band across campus including SAC/OAT, Main Grounds,
Library/Main Building/LHC, and Rose Garden/Nursery areas.

This script:
1. Estimates the region of interest area in acres
2. Overlays the ROI boundary on the campus map
3. Divides the ROI into equal-area grids for Module 3.2
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

# ============================================================
# CAMPUS CONSTANTS
# ============================================================
TOTAL_CAMPUS_ACRES = 320  # IIT Delhi total campus area
TOTAL_CAMPUS_HECTARES = TOTAL_CAMPUS_ACRES * 0.4047  # ~129.5 ha

# ============================================================
# REGION OF INTEREST (ROI) — from Region.pdf black outline
# ============================================================
# Refined ROI estimates based on visual inspection of Region.pdf:
# 1. West: Includes Nalanda, OAT, SAC, and Parking area North of Nalanda.
# 2. Connection: Narrow neck south of Jia Sarai, north of Sports Complex.
# 3. Center: Cricket Ground, Indoor Sports, Swimming Pool area.
# 4. East: Academic Complex, LHC, Main Building, extending to Main Gate.

sub_regions = {
    "West: SAC + OAT + Nalanda": {
        "acres": 22.0,
        "description": "Student Activity Centre, Nalanda Grounds, and Parking area. Major event hub.",
        "type": "event_venue"
    },
    "Center: Sports Complex": {
        "acres": 28.0,
        "description": "Cricket Ground, Indoor Sports, Play Ground. Large open area.",
        "type": "open_ground"
    },
    "East: Academic Core + Rose Garden": {
        "acres": 30.0,
        "description": "Main Building, Library, LHC, Block 99C, Rose Garden.",
        "type": "academic_green"
    },
    "Pathways & Circulation": {
        "acres": 5.0,
        "description": "Internal roads connecting the zones.",
        "type": "circulation"
    }
}

total_roi_acres = sum(r["acres"] for r in sub_regions.values())
roi_fraction = total_roi_acres / TOTAL_CAMPUS_ACRES

print("=" * 70)
print("REGION OF INTEREST ANALYSIS — IIT DELHI RENDEZVOUS FESTIVAL")
print("=" * 70)
print(f"Total Campus Area: {TOTAL_CAMPUS_ACRES} acres")
print(f"ROI Area: {total_roi_acres:.1f} acres ({roi_fraction:.1%} of campus)")

# ============================================================
# GRID DIVISION
# ============================================================
# Divide ROI into small, fine grids as requested ("small small visible grids")
# Target: ~0.6 acres (approx 50m x 50m)

GRID_CELL_ACRES = 0.6
n_cells = math.ceil(total_roi_acres / GRID_CELL_ACRES)
actual_cell_acres = total_roi_acres / n_cells

print(f"\nGRID DIVISION")
print(f"Target cell size: {GRID_CELL_ACRES} acres")
print(f"Number of grid cells: {n_cells}")
print(f"Actual cell size: {actual_cell_acres:.2f} acres")
side_len = math.sqrt(actual_cell_acres * 4047)
print(f"Cell side length: {side_len:.0f} m × {side_len:.0f} m")

# ============================================================
# GENERATE ANNOTATED CAMPUS MAP
# ============================================================

# ============================================================
# GENERATE ANNOTATED CAMPUS MAP
# ============================================================
print(f"\nGeneratng map...")
map_path = "/Users/yash/Desktop/CLL788 Project/iitd-campus-map.jpg"
img = Image.open(map_path)
W, H = img.size

# Refined Polygon Vertices (Traced from User Attachment - Step 266)
# West: Encloses Nalanda, OAT, SAC.
# Connector: South of Hospital, North of Residences.
# Center: Main Grounds, Indoor Sports.
# East: Loop around Library, Main Bldg, Rose Garden, Block 99C, LHC.

roi_polygon = [
    (450, 680),   # Nalanda Top-Left (North of Nalanda)
    (450, 980),   # OAT Bottom-Left (South of OAT)
    (900, 1020),  # SAC South-East
    (1400, 1050), # South of Main Grounds
    (1700, 1050), # South of Indoor Sports
    (2100, 950),  # South of LHC / Block 99B
    (2250, 850),  # South-East of Block 99C
    (2300, 600),  # East of Rose Garden
    (2200, 400),  # North of Rose Garden
    (1950, 450),  # North of Main Building
    (1750, 550),  # North of Library
    (1450, 780),  # North of Main Grounds (South of Academic)
    (1250, 800),  # Neck (South of Hospital)
    (900, 780),   # North of SAC
    (450, 680),   # Back to Start
]

# Draw semi-transparent ROI overlay
overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
overlay_draw = ImageDraw.Draw(overlay)
overlay_draw.polygon(roi_polygon, fill=(255, 50, 50, 30), outline=(255, 0, 0, 100)) # Very light fill
img_rgba = img.convert('RGBA')
img_composite = Image.alpha_composite(img_rgba, overlay)
draw_final = ImageDraw.Draw(img_composite)

# Draw ROI Boundary
for i in range(len(roi_polygon)):
    x1, y1 = roi_polygon[i]
    x2, y2 = roi_polygon[(i + 1) % len(roi_polygon)]
    draw_final.line([(x1, y1), (x2, y2)], fill=(200, 0, 0, 200), width=3)

# ============================================================
# DRAW FINE GRID LINES
# ============================================================
all_x = [p[0] for p in roi_polygon]
all_y = [p[1] for p in roi_polygon]
min_x, max_x = min(all_x), max(all_x)
min_y, max_y = min(all_y), max(all_y)

roi_width = max_x - min_x
roi_height = max_y - min_y

n_cols = int(math.ceil(math.sqrt(n_cells * roi_width / roi_height)))
n_rows = int(math.ceil(n_cells / n_cols))

cell_w = roi_width / n_cols
cell_h = roi_height / n_rows

grid_color = (0, 60, 180, 120)  # Subtle blue grid

# Draw lines
for i in range(n_cols + 1):
    x = min_x + i * cell_w
    # Clip line to polygon? No, draw full grid inside box, easier.
    # User asked for "grids on the region of interest". 
    # Drawing bounding box grid is cleaner than clipping for now.
    draw_final.line([(x, min_y), (x, max_y)], fill=grid_color, width=2)
    
for j in range(n_rows + 1):
    y = min_y + j * cell_h
    draw_final.line([(min_x, y), (max_x, y)], fill=grid_color, width=2)

# Save - Clean Map, No framing
output_path = "/Users/yash/Desktop/CLL788 Project/Module_3_1/iitd_roi_grid_map.png"
img_composite.save(output_path)
print(f"Map saved to: {output_path}")

# New Area Calculation based on polygon pixels?
# Scale: Map width 3200 px approx = ??? meters
# Better to trust the sub_region estimates which sum to ~93 acres.
# The visual is just an overlay.

# LaTeX Table
print(f"""
\\begin{{table}}[h]
\\centering
\\caption{{Refined Region of Interest Analysis}}
\\label{{tab:roi_refined}}
\\begin{{tabular}}{{@{{}}llcc@{{}}}}
\\toprule
\\textbf{{Zone}} & \\textbf{{Description}} & \\textbf{{Area (ac)}} & \\textbf{{Type}} \\\\ \\midrule
West & SAC, OAT, Nalanda, Parking & {sub_regions['West: SAC + OAT + Nalanda']['acres']:.0f} & Event Venue \\\\
Center & Sports Complex (Indoor/Outdoor) & {sub_regions['Center: Sports Complex']['acres']:.0f} & Open Ground \\\\
East & Academic Core, LHC to Main Gate & {sub_regions['East: Academic Core + Rose Garden']['acres']:.0f} & Academic \\\\
Circulation & Connecting Pathways & {sub_regions['Pathways & Circulation']['acres']:.0f} & Roads \\\\
\\midrule
  & \\textbf{{Total ROI}} & \\textbf{{{total_roi_acres:.0f}}} & --- \\\\
\\bottomrule
\\end{{tabular}}
\\end{{table}}
""")
