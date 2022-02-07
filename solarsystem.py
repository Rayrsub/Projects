planets = {
    "Mercury" : {
        "Length of year" : 88,
        "Planet type" : "Terrestrial",
        "Distance from sun" : 0.4
        },
    "Venus" : {
        "Length of year" :225,
        "Planet type" : "Terrestrial",
        "Distance from sun" : 0.7
        },
    "Earth" : {
        "Length of year" : 365,
        "Planet type" : "Terrestrial",
        "Distance from sun" : 1
        },
    "Mars" : {
        "Length of year" : 687,
        "Planet type" : "Terrestrial",
        "Distance from sun" : 1.5
        },
    "Jupitar" : {
        "Length of year" : 4333,
        "Planet type" : "Gas Giant",
        "Distance from sun" : 5.2
        },
    "Saturn" : {
        "Length of year" : 10759,
        "Planet type" : "Gas Giant",
        "Distance from sun" : 9.5
        },
    "Uranus" : {
        "Length of year" : 30687,
        "Planet type" : "Ice Giant",
        "Distance from sun" : 19.8
        },
    "Neptune" : {
        "Length of year" : 60190,
        "Planet type" : "Ice Giant",
        "Distance from sun" : 30
        }
    }

EARTH_DAYS = "365"

def age_on_planet(age, planet):
    new_age = (age * EARTH_DAYS) / planets[planet]
        ["length of year"]
    return round(new_age)
