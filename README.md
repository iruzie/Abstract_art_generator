

# 🎨 Art Generator

This project is an **Image-based Abstract Art Generator** that takes an input image, applies various transformations, and generates an abstract art piece. The tool pixelates the image, reduces its colors, and adds random shapes to create a unique, artistic output. 🖼️✨

## 🚀 Features

- **Pixelation**: The input image is pixelated by resizing and enlarging to create a blocky, abstract effect. 🔲
- **Color Quantization**: Reduces the number of colors in the image to create a visually simplified, abstract palette. 🎨
- **Random Shapes**: Adds randomly placed circles and rectangles using a color palette extracted from the input image. 🔵🟢🟠
- **Output Image**: The final abstract art is saved as an image (e.g., PNG or JPEG). 📸

## 🛠️ Technologies Used

- **Python**: The primary programming language. 🐍
- **PIL (Pillow)**: Used for image manipulation and drawing shapes on the image. 🖌️
- **Numpy**: For handling and processing pixel data efficiently. 🔢
- **Random**: For generating random positions and shapes on the image. 🎲

## 📦 Requirements

To run this project, you'll need the following Python libraries:

- **Pillow**: For image processing.
- **Numpy**: For numerical operations.

You can install these libraries using `pip`:

```bash
pip install pillow numpy
```

## 📝 How to Use

1. **Clone or Download the Repository**:
   Clone or download the repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/art-generator.git
   ```

2. **Place Your Input Image**:
   - Make sure you have an image to process.
   - Edit the `input_image_path` in the script to point to your image file.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the folder containing the script and execute the following command:

   ```bash
   python art_generator.py
   ```

   The script will process your image and save the generated abstract art in the specified `output_image_path`. 💻🎨

4. **Customize the Output**:
   - You can modify the number of shapes (`num_shapes`) or the size of the pixelation (`pixel_size`) to tweak the output's appearance. 🎨✨
   - Adjust the number of colors (`num_colors`) to create different levels of abstraction. 🎨🔮

## 📂 File Structure

Your project folder should look like this:

```
/art-generator
  |-- art_generator.py
  |-- input_image.jpg (or any image you want to use)
  |-- output_image.png (generated abstract art)
  |-- README.md (this file)
```

## 🖼️ Example of Customization

- **Pixelation Size**: Change the `pixel_size` parameter in the `pixelate()` function to make the pixelation effect stronger or weaker. 🔲
- **Number of Colors**: Adjust the `num_colors` parameter in the `color_quantization()` function to have more or fewer colors in the final art. 🌈
- **Number of Shapes**: Modify `num_shapes` in the `add_random_shapes()` function to change the amount of random shapes added to the image. 🟡🔶

## 🎨 Output Example

After running the script, you will receive an abstract version of your image that might look something like this:

![Abstract Art Example](example_output.png)

## 📜 License

This project is licensed under the MIT License. 📝

## 📬 Contact

Feel free to reach out if you have any questions or suggestions! 💌

- Email: roseiruzie.com
- GitHub: [github.com/yourusername/art-generator](https://github.com/yourusername/art-generator)

---
