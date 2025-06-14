from django.core.management.base import BaseCommand
from product.models import Category  
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Creates the category hierarchy for the website'

    def handle(self, *args, **options):
        data = """
#Bathroom Furniture
Back
Combination Vanity Units
Freestanding Vanity Units
Wall Hung Vanity Units
Cloakroom Vanity Units
Toilet Units
Bathroom Cabinets & Storage
Illuminated Bathroom Mirrors
Bathroom Mirror Cabinets
#Toilets
Close Coupled Toilets
Traditional Toilets
Comfort Height Toilets
Back To Wall Toilets
Wall Hung Toilets
WC Units
Toilet Seats
Concealed Cisterns
Urinals
#Basins
Full Pedestal Basins
Semi Recessed Basins
Cloakroom Basins
Counter Top Basins
Vanity Units
Basin Wastes & Traps
#Taps
Basin Taps
Basin Mixer Taps
Bath Taps
Bath Filler Taps
Bath Shower Mixer Taps
Accessories
#Baths
Straight Baths
Single Ended Baths
Double Ended Baths
Curved Baths
Bow Front Baths
Corner Baths
J Shaped Baths
Round Baths
Shower Baths
L Shaped Shower Baths
P Shaped Shower Baths
Single Ended Shower Baths
Shower Bath Screens
Shower Bath Panels
Freestanding Baths
Contemporary Freestanding Baths
Traditional Freestanding Baths
Whirlpool Baths
Single Ended Whirlpool Baths
Double Ended Whirlpool Baths
Whirlpool Shower Baths
Whirlpool Corner Baths
Walk In Baths
Bath Screens
Bath Panels
Bath Wastes
#Shower Trays
Square Shower Trays
Rectangular Shower Trays
Quadrant Shower Trays
Offset Quadrant Shower Trays
Shower Wastes
Riser Kits
#Shower Enclosures
Square Shower Enclosures
Quadrant Shower Enclosures
Offset Quadrant Shower Enclosures
Bifold Shower Enclosures
Hinged & Pivot Shower Enclosures
Sliding Shower Enclosures
Corner Entry Shower Enclosures
Shower Doors
Bifold Shower Doors
Hinged & Pivot Shower Doors
Sliding Shower Doors
Shower Door Side Panels
Wet Rooms
Wet Room Panels
Wet Room Systems
#Showers
Shower Sets
Shower Valves
Shower Heads & Arms
Slider Rail Kits
#Flooring
Stone Effect Vinyl Flooring
Wood Effect Vinyl Flooring
#Heating
Designer Towel Radiators
Designer Vertical Radiators
Designer Horizontal Radiators
Towel Rails
Radiator Valves
Electric Elements
Underfloor Heating
#Wall Panelling
Laminate Wall Panels
Slatted Wall Panels
PVC Wall Panels
Trims
#Brands
Kstone Shower Trays
Cambrian
Bathe Easy
Cosytoes Underfloor Heating
Cramer Cleaning & Repair Kits
Hudson Reed
Hydro Step Luxury Vinyl Floor Tiles
MX Group
MX Elements Shower Trays
Oasis Freestanding Baths
Reflections Illuminated Mirrors
Coral 6mm Showers
Trojan Baths
Trojancast Reinforced Baths
Trojan Whirlpool Baths
Trojan Single Ended Baths
Trojan Double Ended Baths
Trojan Freestanding Baths
Trojan Shower Baths
Trojan Corner Baths
Trojan Bow Fronted Baths
Trojan J Shaped Baths
Trojan Bath Panels
Coral 8mm Showers
Lapis Wetroom Glass Panels
Clearance
"""

        current_parent = None
        created_count = 0
        
        for line in data.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('#'):
                # This is a parent category
                name = line[1:].strip()
                slug = slugify(name)
                current_parent, created = Category.objects.get_or_create(
                    name=name,
                    defaults={'slug': slug}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created parent category: {name}'))
                    created_count += 1
            else:
                # This is a child category
                if current_parent is None:
                    self.stdout.write(self.style.WARNING(f'Skipping "{line}" - no parent category'))
                    continue
                    
                name = line.strip()
                slug = slugify(name)
                _, created = Category.objects.get_or_create(
                    name=name,
                    parent=current_parent,
                    defaults={'slug': slug}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created child category: {name} under {current_parent.name}'))
                    created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} categories'))