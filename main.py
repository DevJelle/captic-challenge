import cv2
import json


def create_image_metadata(image_path):
    image = cv2.imread(image_path)

    if image is not None:
        height, width, channels = image.shape
        image_size = image.size
        image_dtype = str(image.dtype)
        mean_color = cv2.mean(image)[:3]
        mean_color_int = [int(value) for value in mean_color]

        dominant_color = calculate_dominant_color(image)

        image_metadata = {
            "file_name": image_path,
            "width(px)": width,
            "height(px)": height,
            "number_of_channels": channels,
            "image_size": image_size,
            "data_type": image_dtype,
            "mean_color(bgr)": {
                "blue": mean_color_int[0],
                "green": mean_color_int[1],
                "red": mean_color_int[2]
            },
            "dominant_color(bgr)": {
                "blue": str(dominant_color[0]),
                "green": str(dominant_color[1]),
                "red": str(dominant_color[2])
            },
        }

        json_data = json.dumps(image_metadata, indent=4)
        with open("metadata.json", 'w') as json_file:
            json_file.write(json_data)
    else:
        print("Failed to load the image.")


def calculate_dominant_color(image) -> tuple:
    pixels = image.reshape(-1, 3)
    pixels = [tuple(pixel) for pixel in pixels]

    color_counts = {}
    for pixel in pixels:
        if pixel in color_counts:
            color_counts[pixel] += 1
        else:
            color_counts[pixel] = 1

    dominant_color = max(color_counts, key=color_counts.get)
    return dominant_color


if __name__ == "__main__":
    image_path = 'image.jpeg'
    create_image_metadata(image_path)
