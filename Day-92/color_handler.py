from colorthief import ColorThief


def extract_dominant_colors(image_path_local, num_colors_local=5):
    color_thief = ColorThief(image_path_local)
    dominant_colors_local = color_thief.get_palette(color_count=num_colors_local)

    # Convert RGB to hex
    hex_colors = [rgb_to_hex(col) for col in dominant_colors_local]

    return hex_colors


def rgb_to_hex(col):
    return "#{:02X}{:02X}{:02X}".format(col[0], col[1], col[2])


