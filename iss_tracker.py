import requests
import folium

# Get real-time ISS position
response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()

# Extract coordinates
latitude = float(data['iss_position']['latitude'])
longitude = float(data['iss_position']['longitude'])

# Create map centered at ISS position
iss_map = folium.Map(location=[latitude, longitude], zoom_start=2)

# Add ISS marker
folium.Marker(
    location=[latitude, longitude],
    popup="🌌 International Space Station",
    icon=folium.Icon(color='blue', icon='rocket')
).add_to(iss_map)

# Optional: Your location (LPU as example)
my_lat, my_long =  31.2536,75.7036
folium.Marker(
    location=[my_lat, my_long],
    popup="📍 My Location",
    icon=folium.Icon(color='green')
).add_to(iss_map)

# Draw line between ISS and your location
folium.PolyLine([[my_lat, my_long], [latitude, longitude]], color='red').add_to(iss_map)

# Save map
iss_map.save("iss_tracker.html")
print("✅ Map has been saved! Open 'iss_tracker.html' in your browser.")
