import minescript

absoluteRotation = minescript.player_orientation()[0]
rel = (absoluteRotation + 180) % 360 - 180

print(f"Rel: {round(rel, 2)} Abs: {round(absoluteRotation, 2)}")

