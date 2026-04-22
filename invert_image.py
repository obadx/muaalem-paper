from PIL import Image, ImageOps

def invert_image(input_path, output_path):
    img = Image.open(input_path)
    if img.mode == "RGBA":
        rgb_img = img.convert("RGB")
        inverted = ImageOps.invert(rgb_img)
        inverted = inverted.convert("RGBA")
    else:
        inverted = ImageOps.invert(img)
    inverted.save(output_path)

invert_image("paper-latex/figures/reciter.png", "paper-latex/figures/reciter_white.png")
invert_image("paper-latex/figures/stats.png", "paper-latex/figures/stats_white.png")
