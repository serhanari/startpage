import pywal

wallpaper_path = "../../../public/images/wallpaper/"
css_source_path = "../../css/colors/"
json_source_path = "../../data/json/colors/"

wallpaper_name = "a_snowy_landscape_with_trees_and_a_light_on_it.jpg"

color_generation = pywal.colors.get(wallpaper_path + wallpaper_name)

special_colors = color_generation["special"]
main_colors = color_generation["colors"]

special_scss = ""
main_scss = ""

with open(css_source_path + "_special_colors.scss", "w") as file:
    for color in special_colors:
        special_scss += f"\t--{color}: {special_colors[color].upper()};\n"

    new_css = f""":root {{
{special_scss}}}"""
    print(new_css)
    file.write(new_css)

with open(css_source_path + "_main_colors.scss", "w") as file:
    for color in main_colors:
        main_scss += f"\t--{color}: {main_colors[color].upper()};\n"

    new_css = f""":root {{
{main_scss}}}"""
    print(new_css)
    file.write(new_css)



