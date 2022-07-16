import colorgram


class RandomColor:
    """
      help extract colours from an image and use the colors to paint our hirst
    """
    def choose_color(self):
        colors = colorgram.extract("image.jpg", 30)
        color_list = []
        for color in colors:
            r = color.rgb[0]
            g = color.rgb[1]
            b = color.rgb[2]
            new_color = (r, g, b)
            color_list.append(new_color)

        return color_list

