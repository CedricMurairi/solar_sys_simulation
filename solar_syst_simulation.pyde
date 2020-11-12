from space_bodies import CelestialBody, Planet, NSatellite

sun_rad = map(696340, 1000, 700000, 1, 200) / 8
print('Sun radius {}'.format(sun_rad))
sun_mass = 1.989 * (10 ** 30)

earth_rad = map(6371, 1000, 70000, 10, 100)
print("Earth radius {}".format(earth_rad))
earth_mass = 5.972 * (10 ** 24)
earth_dist = map((148.08 * (10 ** 6)), 1000000, 5 * 10 ** 9, 10, 500)
print("Earth dist {}".format(earth_dist))

mars_rad = map(3389, 1000, 70000, 10, 100)
print("Mars radius {}".format(mars_rad))
mars_mass = 6.39 * (10 ** 23)
mars_dist = map(217.65 * (10 ** 6), 1000000, 5 * 10 ** 9, 10, 500)
print("Mars dist {}".format(mars_dist))

venus_rad = map(6051, 1000, 70000, 10, 100)
print("Venus radius {}".format(venus_rad))
venus_mass = 4.867 * (10 ** 24)
venus_dist = map(107.52 * (10 ** 6), 1000000, 5 * 10 ** 9, 10, 500)
print("Venus dist {}".format(venus_dist))

mercury_rad = map(2439, 1000, 70000, 10, 100)
print("Mercury radius {}".format(mercury_rad))
mercury_mass = 3.285 * (10 ** 23)
mercury_dist = map(50.012 * (10 ** 6), 1000000, 5 * 10 ** 9, 10, 500)
print("Mercury dist {}".format(mercury_dist))

jupiter_rad = map(69911, 1000, 70000, 10, 100)
print("Jupiter radius {}".format(jupiter_rad))
jupiter_mass = 1.898 * (10 ** 27)
jupiter_dist = map(765.36 * (10 ** 6), 100000, 5 * 10 ** 9, 10, 500)
print("Jupiter dist {}".format(jupiter_dist))

saturn_rad = map(58232, 1000, 70000, 10, 100)
print("Saturn radius {}".format(saturn_rad))
saturn_mass = 5.683 * (10 ** 26)
saturn_dist = map(1492.4 * (10 ** 6), 1000000, 5 * 10 ** 9, 10, 500)
print("Saturn dist {}".format(saturn_dist))

uranus_rad = map(25362, 1000, 70000, 10, 100)
print("Uranus radius {}".format(uranus_rad))
uranus_mass = 8.681 * (10 ** 25)
uranus_dist = map(2958.6 * (10 ** 6), 1000000, 5 * 10 ** 9, 10, 500)
print("Uranus dist {}".format(uranus_dist))

neptune_rad = map(24622, 1000, 70000, 10, 100)
print("Neptune radius {}".format(neptune_rad))
neptune_mass = 1.024 * (10 ** 26)
neptune_dist = map(4476.1 * (10 ** 6), 1000000, 5 * 10 ** 9, 10, 500)
print("Neptune dist {}".format(neptune_dist))

sun = CelestialBody(sun_rad, sun_mass)
earth = Planet(earth_rad, earth_mass, earth_dist)
mars = Planet(mars_rad, mars_mass, mars_dist)
mercury = Planet(mercury_rad, mercury_mass, mercury_dist)
venus = Planet(venus_rad, venus_mass, venus_dist)
jupiter = Planet(jupiter_rad, jupiter_mass, jupiter_dist)
saturn = Planet(saturn_rad, saturn_mass, saturn_dist)
uranus = Planet(uranus_rad, uranus_mass, uranus_dist)
neptune = Planet(neptune_rad, neptune_mass, neptune_dist)

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

def setup():
    size(1400, 700)
    
def draw():
    noLoop()
    background(0)
    translate(width/2, height/2)
    sun.show()
    i = 0
    for planet in planets:
        if planet.radius < 20:
            xpos = planet.distance + planet.radius + i
            ypos = planet.distance + planet.radius + i
            i += 20
        else:
            i += 10
            xpos = planet.distance + i
            ypos = planet.distance + i
        print("Planet location: {}, {}".format(xpos, ypos))
        pushMatrix()
        rotate(random(0, PI))
        translate(xpos, ypos)
        planet.show()
        planet.move()
        # planet.nsat.show()
        # planet.nsat.move()
        popMatrix()
    
