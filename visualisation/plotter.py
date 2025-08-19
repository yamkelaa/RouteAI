# visualization/plotter.py
import matplotlib.pyplot as plt

def plot_routes(locations, routes, ax=None, title="Routes"):
    if ax is None:
        fig, ax = plt.subplots(figsize=(6,6))

    xs = [loc.x for loc in locations]
    ys = [loc.y for loc in locations]
    ax.scatter(xs, ys, c="black", s=50, label="Locations")

    for loc in locations:
        ax.text(loc.x+1, loc.y+1, str(loc.id), fontsize=9)

    colors = ["blue", "green", "orange", "purple", "red"]
    for i, route in enumerate(routes):
        if not route:
            continue
        x_vals = [locations[0].x] + [locations[j].x for j in route] + [locations[0].x]
        y_vals = [locations[0].y] + [locations[j].y for j in route] + [locations[0].y]
        ax.plot(x_vals, y_vals, color=colors[i % len(colors)], linewidth=2, label=f"Vehicle {i+1}")

    ax.set_title(title)
    ax.legend()

    return ax
