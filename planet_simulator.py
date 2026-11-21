import sys
from math import atan2, cos, isfinite, pi, sin, sqrt

import matplotlib

matplotlib.use("TkAgg")  # Select the interactive Windows backend

import matplotlib.pyplot as plt
from astropy import constants as const
from matplotlib.animation import FuncAnimation

# Important constants in the gravitation law: these never change
# Based off of Astropy constants (very exact)
G = float(const.G.value)  # Gravitational constant
ME = float(const.M_earth.value)  # 1 Earth mass (in kg)
MS = float(const.M_sun.value)  # 1 solar mass (in kg)
AU = 149597870700  # number of meters in 1 AU

# Time variables (increment and length)
dt = 3600  # This is in seconds: equivalent to 1 hr


def starting_page():
    """Contains some planetary ASCII art and instructions on how to proceed."""
    print("""
                                                                        ..;===+.
                                                                    .:=iiiiii=+=
                                                                .=i))=;::+)i=+,
                                                            ,=i);)I)))I):=i=;
                                                        .=i==))))ii)))I:i++
                                                        +)+))iiiiiiii))I=i+:'
                                    .,:;;++++++;:,.       )iii+:::;iii))+i='
                                .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                            ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                            ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                            ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                        ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                        ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                        ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                        =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                    +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                    =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                    .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                    :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                    :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                    .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                    =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                    +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
                +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
                =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
            +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
            :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
        .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
        ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
        +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
    .+=:))iiiiiiii)))+ii;
    .+=;))iiiiii)));ii+
    .+=i:)))))))=+ii+
    .;==i+::::=)i=;
    ,+==iiiiii+,
    `+=+++;`
    1,677

    ---------------------------------------------------------------------------------
    Welcome to Planet Simulator! Here you can experiment with the creation of
    your own planetary orbits!
    ---------------------------------------------------------------------------------
    Commands You Can Use:
    1 - Learn the Basics of How Planetary Orbits Work
    2 - Create Your Own Orbit!
    3 - Watch Your Own Orbit's Animation!
    4 - Quit
    """)


def user_select():
    """Lets the user pick an option provided on the menu."""
    choice = input("\nWhat will you do? The choice is yours! ")
    if choice == "1":
        basics()
    elif choice == "2":
        user_input()
        plot()
    elif choice == "3":
        user_input()
        orbit_ani()
    elif choice == "4":
        print("Thanks for using the planetary simulator!")
        sys.exit()
    else:
        print("You entered an invalid choice. Please try again.")
        user_select()


def basics():
    """Tells user the basics of planetary orbits."""
    choice = input("""
------------------------------------------------------------------------
1. Orbital Geometry
2. Ellipses
3. Eccentricity
4. Solar Mass
5. Earth Mass
6. AU
7. Orbital Velocity
8. Orbital Period
9. Escape Velocity
10. Periastron
11. Apastron
12. Kepler's 1st Law
13. Kepler's 2nd Law
14. Kepler's 3rd Law
-------------------------------------------------------------------------
Which term would you like to learn more about? """)
    if choice == "1":
        print("""
        1. Orbiting bodies follow a trajectory based on 1 of the 4 conic sections (circle,
        eliipse, parabola, hyperbola). The type of shape is based on factors such as distance,
        orbital velocity, and more. To stay in orbit, the planet must have either a circular
        or elliptical orbit.

        The planets in our Solar System all follow elliptical orbits. Circular orbits are possible;
        however, they are rare as they require a near-perfect balance of fa ctors.
        """)
    elif choice == "2":
        print("""
        2. Ellipses - also known as ovals. Planets have elliptical orbits according to Kepler's
        First Law. Ellipses have a longer side and a shorter side. The longer, more stretched side
        is on an axis called the major axis, and the shorter side is on the minor axis. Also,
        ellipses have two radii. The longer one (located on the major axis) is called the semi-
        major axis. The shorter one (on the minor axis) is called the semi-minor axis. Ellipses have
        two special points within their boundary called the foci (singular: focus). These are special
        points with special properties.
        """)
    elif choice == "3":
        print("""
        3. Eccentricity - this is a number showing how stretched an ellipse is. For ellipses,
        eccentricities start at 0 (representing a perfect circle). They can go all the way up to 1
        (not including 1); as the eccentricity increases, the ellipse becomes longer and more
        elongated.
        """)
    elif choice == "4":
        print("""
        4. Solar Mass - 1 Solar Mass is equal to the mass of the Sun (about 1.989e30 kg)
        """)
    elif choice == "5":
        print("""
        5. Earth Mass - 1 Earth Mass is equal to the mass of the Earth (about 5.972e24 kg)
        """)
    elif choice == "6":
        print("""
        6. AU - 1 Astronomical Unit (AU) is about 93 million mi, which is the average distance of Earth
        of Earth from the Sun). This is a convenient unit to use on solar system scales.
        """)
    elif choice == "7":
        print("""
        7. Orbital Velocity - the speed at which a planet travels tangentially. It prevents planet from
        falling directly into the star.
        """)
    elif choice == "8":
        print("""
        8. Orbital Period - the time it takes for an orbiting body to complete 1 full revolution around
        another body
        """)
    elif choice == "9":
        print("""
        9. Escape Velocity - the required orbital speed needed for a planet to break free from its orbit
        around its star
        """)
    elif choice == "10":
        print("""
        10. Periastron - the minimum distance a planet reaches from its star during its orbit, endpoint of
        the semi-minor axis (a more general term for perihelion)
        """)
    elif choice == "11":
        print("""
        11. Apastron - the maximum distance a planet reaches from its star during its orbit, endpoint of
        the semi-major axis (a more general term for aphelion)
        """)
    elif choice == "12":
        print("""
        Kepler's 1st Law - The orbit of a planet is an ellipse. The Sun is located at one of the foci.
        Also known as the Law of Orbits.
        """)
    elif choice == "13":
        print("""
        Kepler's 2nd Law - The line connecting the planet to the sun sweeps out equal areas in equal
        amounts of time. This means that planets travel faster when closer to their star, and vice versa.
        Also known as the Law of Areas.
        """)
    elif choice == "14":
        print("""
        Kepler's 3rd Law - The square of a planet's orbital period is directly proportional to the cube
        of the semi-major axis of its orbit. This means that planets further from the Sun take longer
        to complete one full revolution. Also known as the Law of Periods.
        """)
    else:
        print("You entered something invalid. Please try again!")
        basics()


def _read_positive_float(prompt):
    """Prompt until the user enters a finite number greater than zero."""
    while True:
        try:
            value = float(input(prompt))
            if not isfinite(value) or value <= 0:
                print("Please enter a finite number greater than zero.\n")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, such as 1 or 0.5.\n")


def _read_finite_float(prompt):
    """Prompt until the user enters any finite number."""
    while True:
        try:
            value = float(input(prompt))
            if not isfinite(value):
                print("Please enter a finite number.\n")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, such as 30 or -2.5.\n")


def _read_positive_int(prompt):
    """Prompt until the user enters a whole number greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a whole number greater than zero.\n")
                continue
            return value
        except ValueError:
            print("Please enter a whole number, such as 30.\n")


def user_input():
    """Read the user's orbit settings and initialize the bodies."""
    global SMASS, PMASS, init_x, init_vy, days, planet, star

    star_mass_solar = _read_positive_float("Type your star's mass (in solar masses): ")
    planet_mass_earth = _read_positive_float(
        "Type your planet's mass (in Earth masses): "
    )
    init_x = _read_positive_float("Type the planet's initial distance (in AU): ")
    velocity_kms = _read_finite_float(
        "Type the planet's initial orbital velocity (in km/s): "
    )
    days = _read_positive_int("How many days would you like to run the simulation? ")

    SMASS = star_mass_solar * MS
    PMASS = planet_mass_earth * ME
    init_vy = velocity_kms * 1000

    # Reset the position and velocity vectors for this run
    planet = [init_x, 0, 0, init_vy]
    star = [0, 0, 0, 0]


def calculate_orbital_period_days():
    """Estimate the orbital period from the initial position and velocity."""
    radius_m = init_x * AU
    gravitational_parameter = G * (SMASS + PMASS)

    # init_vy is in meters per second
    inverse_semimajor_axis = 2 / radius_m - init_vy**2 / gravitational_parameter

    # A zero or negative value means the orbit is not a closed ellipse
    if inverse_semimajor_axis <= 0:
        return None

    semimajor_axis_m = 1 / inverse_semimajor_axis
    period_seconds = 2 * pi * sqrt(semimajor_axis_m**3 / gravitational_parameter)
    return period_seconds / 86400


def dist_angle(planet, star):
    """Looks at the positions for planet and star, finds the distance and
    angle of the vector from the planet to the star."""

    stp_vec = [star[0] - planet[0], star[1] - planet[1]]
    angle = atan2(stp_vec[1], stp_vec[0])
    squared_d = stp_vec[0] ** 2 + stp_vec[1] ** 2
    d = sqrt(squared_d)
    angle = atan2(stp_vec[1], stp_vec[0])
    return [d, angle]


def accel_comps(d, angle):
    """Gets a distance and an angle. Returns the x- and y- components of both
    planet + star accelerations."""

    d2 = (d * AU) ** 2
    force = (G * PMASS * SMASS) / d2

    accel_planet = force / PMASS  # Magnitude of Earth's acceleration
    accel_planet_x = accel_planet * cos(angle)  # X-component of Earth's acceleration
    accel_planet_y = accel_planet * sin(angle)  # Y-component of Earth's acceleration

    accel_sun = force / SMASS  # Magnitude of Sun's acceleration
    accel_sun_x = accel_sun * cos(angle + pi)  # X-component of Sun's acceleration
    accel_sun_y = accel_sun * sin(angle + pi)  # Y-component of Sun's acceleration

    return [accel_planet_x, accel_planet_y, accel_sun_x, accel_sun_y]


def update(accels):
    """Gets a list of acceleration components and updates the velocities and positions
    of the planet and star using a Semi-Implicit Euler algorithm."""

    # This part is for the Earth's velocity
    planet[2] += accels[0] * dt
    planet[3] += accels[1] * dt

    # This part is for the Earth's position
    planet[0] += (planet[2] * dt) / AU
    planet[1] += (planet[3] * dt) / AU

    # This part is for the Sun's velocity
    star[2] += accels[2] * dt
    star[3] += accels[3] * dt

    # This part is for the Sun's position
    star[0] += (star[2] * dt) / AU
    star[1] += (star[3] * dt) / AU


def plot():
    """Plots planetary and stellar trajectories with orbit details."""
    px = [init_x]
    py = [0]
    sx = [0]
    sy = [0]

    # One simulation step is one hour
    for _ in range(days * 24):
        info = dist_angle(planet, star)
        accels = accel_comps(info[0], info[1])
        update(accels)

        px.append(planet[0])
        py.append(planet[1])
        sx.append(star[0])
        sy.append(star[1])

    # Calculate planet–Sun distances and find closest/farthest points
    distances = [
        ((px[i] - sx[i]) ** 2 + (py[i] - sy[i]) ** 2) ** 0.5 for i in range(len(px))
    ]
    periastron_index = distances.index(min(distances))
    apastron_index = distances.index(max(distances))
    periastron_distance = distances[periastron_index]
    apastron_distance = distances[apastron_index]

    # Estimate eccentricity from the closest and farthest distances
    if periastron_distance + apastron_distance > 0:
        eccentricity = (apastron_distance - periastron_distance) / (
            apastron_distance + periastron_distance
        )
    else:
        eccentricity = float("nan")

    # Estimate orbital period from the initial position and velocity
    radius_m = init_x * AU
    gravitational_parameter = G * (SMASS + PMASS)
    inverse_semimajor_axis = 2 / radius_m - init_vy**2 / gravitational_parameter

    if inverse_semimajor_axis > 0:
        semimajor_axis_m = 1 / inverse_semimajor_axis
        period_seconds = 2 * pi * sqrt(semimajor_axis_m**3 / gravitational_parameter)
        period_text = f"Orbital period: {period_seconds / 86400:.2f} days"
    else:
        period_text = "Orbital period: not a closed orbit"

    # Give the plot and its information separate panels
    _, (ax, info_ax) = plt.subplots(
        1,
        2,
        figsize=(12, 6),
        gridspec_kw={"width_ratios": [4, 1.6]},
    )
    info_ax.set_axis_off()

    ax.plot(px, py, color="blue", marker="o", markersize=1, label="Planet")
    ax.plot(sx, sy, color="red", marker="o", markersize=6, label="Star")

    ax.plot(
        px[periastron_index],
        py[periastron_index],
        marker="*",
        color="green",
        markersize=12,
        label="Periastron",
    )
    ax.plot(
        px[apastron_index],
        py[apastron_index],
        marker="*",
        color="purple",
        markersize=12,
        label="Apastron",
    )

    ax.set_xlabel("X Position (AU)")
    ax.set_ylabel("Y Position (AU)")
    ax.set_title("Planetary and Stellar Trajectories")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.axhline(y=0, color="black", linewidth=2)
    ax.axvline(x=0, color="black", linewidth=2)
    ax.set_aspect("equal", adjustable="box")

    # Put the legend at the top of the separate side panel
    handles, labels = ax.get_legend_handles_labels()
    info_ax.legend(handles, labels, loc="upper left", frameon=True)

    # Periastron and apastron distances
    info_ax.text(
        0.02,
        0.62,
        f"Periastron: {periastron_distance:.3f} AU\n"
        f"Apastron: {apastron_distance:.3f} AU",
        transform=info_ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
    )

    # Eccentricity in its own position
    info_ax.text(
        0.02,
        0.42,
        f"Eccentricity: {eccentricity:.4f}",
        transform=info_ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
    )

    # Orbital period beneath eccentricity
    info_ax.text(
        0.02,
        0.30,
        period_text,
        transform=info_ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
    )

    plt.show()


def orbit_ani():
    """Creates an animation for the planetary and stellar paths."""
    # Calculate the trajectory using the existing simulation
    px = [init_x]
    py = [0]
    sx = [0]
    sy = [0]

    for _ in range(days * 24):
        info = dist_angle(planet, star)
        accels = accel_comps(info[0], info[1])
        update(accels)

        px.append(planet[0])
        py.append(planet[1])
        sx.append(star[0])
        sy.append(star[1])

    # Find the closest and farthest planet–Sun distances
    distances = [
        ((px[i] - sx[i]) ** 2 + (py[i] - sy[i]) ** 2) ** 0.5 for i in range(len(px))
    ]
    periastron_index = distances.index(min(distances))
    apastron_index = distances.index(max(distances))
    periastron_distance = distances[periastron_index]
    apastron_distance = distances[apastron_index]

    # Estimate eccentricity from the closest and farthest distances
    distance_sum = periastron_distance + apastron_distance
    eccentricity = (
        (apastron_distance - periastron_distance) / distance_sum
        if distance_sum > 0
        else float("nan")
    )

    # Estimate orbital period from the initial position and velocity
    radius_m = init_x * AU
    gravitational_parameter = G * (SMASS + PMASS)
    inverse_semimajor_axis = 2 / radius_m - init_vy**2 / gravitational_parameter

    if inverse_semimajor_axis > 0:
        semimajor_axis_m = 1 / inverse_semimajor_axis
        period_seconds = 2 * pi * sqrt(semimajor_axis_m**3 / gravitational_parameter)
        period_label = f"Orbital period: {period_seconds / 86400:.2f} days"
    else:
        period_label = "Orbital period: not a closed orbit"

    step = 20
    displayed_frames = range(0, len(px), step)
    periastron_frame = next(
        (frame for frame in displayed_frames if frame >= periastron_index),
        None,
    )
    apastron_frame = next(
        (frame for frame in range(0, len(px), step) if frame >= apastron_index),
        None,
    )

    # Give the plot and its information separate panels
    fig, (ax, info_ax) = plt.subplots(
        1,
        2,
        figsize=(12, 6),
        gridspec_kw={"width_ratios": [4, 1.8]},
    )
    info_ax.set_axis_off()

    # Animated trails and markers for both bodies
    (planet_trail,) = ax.plot([], [], color="blue", linewidth=1, label="Planet path")
    (star_trail,) = ax.plot([], [], color="red", linewidth=1, label="Sun path")
    (planet_marker,) = ax.plot([], [], "bo", markersize=5, label="Planet")
    (star_marker,) = ax.plot([], [], "ro", markersize=8, label="Sun")

    # Markers for closest and farthest points
    (periastron_marker,) = ax.plot(
        [], [], marker="*", color="green", markersize=12, label="Periastron"
    )
    (apastron_marker,) = ax.plot(
        [], [], marker="*", color="purple", markersize=12, label="Apastron"
    )

    ax.set_xlabel("X Position (AU)")
    ax.set_ylabel("Y Position (AU)")
    ax.set_title("Planetary and Stellar Trajectories")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.axhline(y=0, color="black", linewidth=1)
    ax.axvline(x=0, color="black", linewidth=1)

    # Legend at the top of the separate side panel
    handles, labels = ax.get_legend_handles_labels()
    info_ax.legend(handles, labels, loc="upper left", frameon=True)

    # Information readouts below the legend
    distance_text = info_ax.text(
        0.02,
        0.62,
        "Planet–Sun distance: calculating...",
        transform=info_ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
    )
    extrema_text = info_ax.text(
        0.02,
        0.50,
        f"Periastron: {periastron_distance:.3f} AU\n"
        f"Apastron: {apastron_distance:.3f} AU",
        transform=info_ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
    )
    eccentricity_text = info_ax.text(
        0.02,
        0.40,
        f"Eccentricity: {eccentricity:.4f}",
        transform=info_ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
    )
    period_text = info_ax.text(
        0.02,
        0.32,
        period_label,
        transform=info_ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
    )
    days_text = info_ax.text(
        0.02,
        0.22,
        "Elapsed time: 0.00 days",
        transform=info_ax.transAxes,
        ha="left",
        va="top",
        fontsize=11,
    )

    # Fit the full trajectories of both bodies in the view
    all_x = px + sx
    all_y = py + sy
    center_x = (min(all_x) + max(all_x)) / 2
    center_y = (min(all_y) + max(all_y)) / 2
    half_range = max(
        (max(all_x) - min(all_x)) / 2,
        (max(all_y) - min(all_y)) / 2,
    )
    pad = max(half_range * 0.05, 0.1)
    half_range += pad

    ax.set_xlim(center_x - half_range, center_x + half_range)
    ax.set_ylim(center_y - half_range, center_y + half_range)
    ax.set_aspect("equal", adjustable="box")

    def init():
        planet_trail.set_data([], [])
        star_trail.set_data([], [])
        planet_marker.set_data([], [])
        star_marker.set_data([], [])
        periastron_marker.set_data([], [])
        apastron_marker.set_data([], [])
        days_text.set_text("Elapsed time: 0.00 days")

        return (
            planet_trail,
            star_trail,
            planet_marker,
            star_marker,
            periastron_marker,
            apastron_marker,
            distance_text,
            extrema_text,
            eccentricity_text,
            period_text,
            days_text,
        )

    def animate(frame):
        planet_trail.set_data(px[: frame + 1], py[: frame + 1])
        star_trail.set_data(sx[: frame + 1], sy[: frame + 1])
        planet_marker.set_data([px[frame]], [py[frame]])
        star_marker.set_data([sx[frame]], [sy[frame]])

        distance_text.set_text(f"Planet–Sun distance: {distances[frame]:.3f} AU")

        # Each simulation position represents one hour
        elapsed_days = frame / 24
        days_text.set_text(f"Elapsed time: {elapsed_days:.2f} days")

        if periastron_frame is not None and frame >= periastron_frame:
            periastron_marker.set_data([px[periastron_index]], [py[periastron_index]])

        if apastron_frame is not None and frame >= apastron_frame:
            apastron_marker.set_data([px[apastron_index]], [py[apastron_index]])

        return (
            planet_trail,
            star_trail,
            planet_marker,
            star_marker,
            periastron_marker,
            apastron_marker,
            distance_text,
            extrema_text,
            eccentricity_text,
            period_text,
            days_text,
        )

    ani = FuncAnimation(  # noqa: F841
        fig,
        animate,
        frames=displayed_frames,
        init_func=init,
        interval=10,
        blit=False,
        repeat=False,
    )

    plt.show()


def main():
    starting_page()
    while True:
        user_select()


if __name__ == "__main__":
    main()
