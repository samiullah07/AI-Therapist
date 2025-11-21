import googlemaps
from config import GOOGLE_MAPS_API_KEY

gmap = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def find_nearby_therapists_by_location(location: str) -> str:
    """
    Finds and returns a list of licensed therapists near the specified location.

    Args:
        location (str): The name of the city or area in which the user is seeking therapy support.

    Returns:
        str: A newline-separated string containing therapist names and contact info.
    """
    map_results = gmap.geocode(location)
    lat_lng = map_results[0]['geometry']['location']
    places_result = gmap.places_nearby(location=(lat_lng['lat'], lat_lng['lng']),
                                          radius=5000,
                                          keyword='psychatrist')
    output = [f"Therapists near {location}:\n"]
    therapists = places_result["results"][:5]
    for therapist in therapists:
       name = therapist.get("name", "N/A")
       address = therapist.get("vicinity", "N/A")
       details = gmap.place(therapist['place_id'], fields=['formatted_phone_number', 'website'])
       phone = details.get('result', {}).get('formatted_phone_number', 'N/A')

       output.append(f"Name: {name}\nAddress: {address}\nPhone: {phone}\n")
    return "\n".join(output)





