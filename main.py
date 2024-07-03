from PIL import Image, ImageDraw, ImageFont
import requests
import math


def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height


def get_github_contributions(username):
    url = f'https://github-contributions-api.jogruber.de/v4/{username}?y=2024'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from GitHub: {response.status_code}")

    body = response.json()

    return [(contribution['date'], contribution['count']) for contribution in body['contributions']]


def draw_grid(draw, grid, cell_size, colors):
    for week in range(len(grid)):
        for day in range(len(grid[0])):
            color = colors[grid[week][day]]
            x0, y0 = week * cell_size + 40, day * cell_size + 20
            x1, y1 = x0 + cell_size, y0 + cell_size
            # Shadow
            draw.rectangle([x0 + 3, y0 + 3, x1 + 3, y1 + 3], fill=(0, 0, 0, 100))  # Semi-transparent gray shadow
            # Block
            draw.rectangle([x0, y0, x1, y1], fill=color, outline=(255, 255, 255))


def draw_legend(draw, cell_size, image_width, image_height):
    # Draw day names
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for i, day in enumerate(days):
        y = i * cell_size + 20
        draw.text((5, y), day, fill=(255, 255, 255))

    # Draw month names
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_positions = {1: 0, 2: 4, 3: 8, 4: 12, 5: 16, 6: 20, 7: 24, 8: 28, 9: 32, 10: 36, 11: 40, 12: 44}
    for month, week in month_positions.items():
        x = week * cell_size + 40
        draw.text((x, 5), months[month - 1], fill=(255, 255, 255))

    # Add black bar below months with "Credits: DEBBAWEB" aligned to the right
    legend_width = 40
    bar_height = 20
    bar_y = image_height - bar_height  # Position at the bottom of the image
    draw.rectangle([legend_width, bar_y, image_width, image_height], fill=(0, 0, 0))

    text = "Credits: DEBBAWEB"
    font = ImageFont.load_default()  # Load default font
    text_width, text_height = textsize(text, font=font)  # Calculate text size
    text_x = image_width - text_width - 5
    text_y = bar_y + (bar_height - text_height) // 2
    draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)  # Draw text with specified font


def create_tetris_gif(contributions, output_path):
    width = 53  # 53 weeks
    height = 7  # 7 days per week
    cell_size = 20
    legend_width = 40
    image_width = width * cell_size + legend_width
    image_height = height * cell_size + 40  # Increased to accommodate legend and credits bar

    colors = ['#ebedf0', '#9be9a8', '#40c463', '#30a14e', '#216e39']
    background_color = '#0e0e0e'  # Dark background color

    frames = []
    grid = [[0] * height for _ in range(width)]

    for i, (date, count) in enumerate(contributions):
        week = i // 7
        day = i % 7
        value = min(count, 4)  # Limit max count to 4 for colors

        for step in range(day + 1):
            if step % 2 == 0:  # Add frames for every second step only
                img = Image.new('RGB', (image_width, image_height), background_color)
                draw = ImageDraw.Draw(img)
                draw_legend(draw, cell_size, image_width, image_height)
                draw_grid(draw, grid, cell_size, colors)

                # Draw moving block
                x0, y0 = week * cell_size + legend_width, step * cell_size + 20
                x1, y1 = x0 + cell_size, y0 + cell_size
                draw.rectangle(
                    [x0, y0, x1, y1],
                    fill=colors[value],
                    outline=(255, 255, 255)
                )

                frames.append(img)

        grid[week][day] = value

        # Fade effect for the block when it stops
        for alpha in range(0, 256, 50):  # Larger steps to make the fade faster
            img = Image.new('RGB', (image_width, image_height), background_color)
            draw = ImageDraw.Draw(img)
            draw_legend(draw, cell_size, image_width, image_height)
            draw_grid(draw, grid, cell_size, colors)

            x0, y0 = week * cell_size + legend_width, day * cell_size + 20
            x1, y1 = x0 + cell_size, y0 + cell_size
            draw.rectangle(
                [x0, y0, x1, y1],
                fill=colors[value],
                outline=(255, 255, 255, alpha)
            )

            frames.append(img)

    # Save as animated GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], optimize=False, duration=20, loop=0)


if __name__ == "__main__":
    username = 'debba'
    try:
        contributions = get_github_contributions(username)
        create_tetris_gif(contributions, 'images/github_tetris.gif')
        print("GIF created successfully!")
    except Exception as e:
        print(e)
