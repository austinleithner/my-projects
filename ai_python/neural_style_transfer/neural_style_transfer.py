# Neural Style Transfer implementation using TensorFlow and Keras
import os
import glob
import numpy as np
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Model

# GPU setup: enable memory growth and detect GPU availability
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for g in gpus:
            tf.config.experimental.set_memory_growth(g, True)
    except Exception as e:
        print(f"Could not set memory growth for GPUs: {e}")
    use_gpu = True
    print(f"GPUs found: {[g.name for g in gpus]}")
else:
    use_gpu = False
    print("No GPU found, running on CPU.")

# Attempt to enable mixed precision when a GPU is available
mixed_precision_enabled = False
if use_gpu:
    try:
        tf.keras.mixed_precision.set_global_policy('mixed_float16')
        mixed_precision_enabled = True
        print('Enabled mixed precision (float16) policy')
    except Exception as e:
        print(f'Could not enable mixed precision: {e}')


# Hard-coded parameters (edit these values as needed)

# Paths to the content and style images and output image
content_path = 'content.jpg'
style_path = 'style.jpg'
output_path = 'stylized.jpg'

# Whether to initialize the generated image with the content image or random noise.
# Using the content image can lead to faster convergence and often better results, but with a bias towards the content image,
# while random noise can produce more varied and sometimes more artistic results.
content_init = True  # If True, initialize generated image with content image; else random noise.

# Number of iterations for optimization
# More iterations can lead to better results but take longer to compute.
# Increase this if using random initialization.
# 50 iterations does take a long time on CPU; consider using a GPU for faster results.
iterations = 50

# Interval for displaying progress
display_interval = 50

# The paper used the ratio(s) of the content to style weights: content/style = 1e-3 to 1e-4 
# We can play with these values to get different results
content_weight = 1
style_weight = 1e4


# Layers to use for content and style representation
# VGG19 has 5 blocks of convolutional layers with block 1 and 2 having 2 conv layers each,
# and blocks 3, 4, and 5 having 4 conv layers each.
# Acceptable layer names are like 'block1_conv1', 'block2_conv1', ..., 'block5_conv4'.

# Using earlier layers for the content image will maintain more of the original content image structure.
# Using deeper layers will capture higher-level features but may lose some details.
# You can experiment with different layers to see how they affect the output.
# 'block4_conv2' could be a good starting point for content representation.
content_layer = ['block4_conv2']

# Using multiple layers for style representation captures style at different scales.
# Earlier layers capture low-level features like colors and textures,
# while deeper layers capture more complex patterns and structures.
# You can experiment with different combinations of layers to see how they affect the style transfer.
# A common choice is to use the first conv layer from each block.
# You can have more or fewer layers depending on the desired effect.
# Play around with these layers to see how they influence the style of the generated image.
style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']


def load_and_process_img(path, max_dim=512):
    # Use PIL to load and resize so we avoid TensorFlow shape issues
    pil_img = Image.open(path).convert("RGB")
    # Resize while keeping aspect ratio, with longest side = max_dim
    pil_img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    arr = np.array(pil_img).astype(np.float32)
    # add batch dimension
    arr = np.expand_dims(arr, axis=0)
    # preprocess for VGG19 (expects BGR with mean subtraction)
    arr = tf.keras.applications.vgg19.preprocess_input(arr)
    return tf.convert_to_tensor(arr)


def deprocess_img(processed_img):
    x = processed_img.copy()
    if len(x.shape) == 4:
        x = np.squeeze(x, 0)
    # Reverse preprocess_input for VGG19
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    x = x[:, :, ::-1]
    x = np.clip(x, 0, 255).astype("uint8")
    return x


def gram_matrix(tensor):
    # tensor shape: (batch, height, width, channels)
    x = tf.squeeze(tensor, axis=0)
    channels = int(x.shape[-1])
    x = tf.reshape(x, [-1, channels])
    n = tf.shape(x)[0]
    gram = tf.matmul(x, x, transpose_a=True)
    return gram / tf.cast(n, tf.float32)


def content_loss(content, generated):
    a_C = content_model(content)
    a_G = content_model(generated)
    loss = tf.reduce_mean(tf.square(a_C - a_G))
    return loss

def total_style_loss(style, generated):
    J_style = 0

    for style_model in style_models:
        a_S = style_model(style)
        a_G = style_model(generated)
        GS = gram_matrix(a_S)
        GG = gram_matrix(a_G)
        content_cost = tf.reduce_mean(tf.square(GS - GG))
        J_style += content_cost * weight_of_layer

    return J_style


# Training loop for neural style transfer
def training_loop(content_path, style_path, iterations=50, use_content_init=True):
    # load images (on CPU) then move to GPU if available
    content = load_and_process_img(content_path)
    style = load_and_process_img(style_path)

    if use_gpu:
        with tf.device('/GPU:0'):
            content = tf.identity(content)
            style = tf.identity(style)

    if use_content_init:
        if use_gpu:
            with tf.device('/GPU:0'):
                generated = tf.Variable(content, dtype=tf.float32)
        else:
            generated = tf.Variable(content, dtype=tf.float32)
    else:
        if use_gpu:
            with tf.device('/GPU:0'):
                generated = tf.Variable(tf.random.normal(content.shape), dtype=tf.float32)
        else:
            generated = tf.Variable(tf.random.normal(content.shape), dtype=tf.float32)

    # Create optimizer; wrap with LossScaleOptimizer when mixed precision is enabled
    base_opt = tf.keras.optimizers.Adam(learning_rate=0.7)  # Adjust learning rate as needed
    if mixed_precision_enabled:
        try:
            LossScaleOptimizer = tf.keras.mixed_precision.LossScaleOptimizer
            opt = LossScaleOptimizer(base_opt)
        except Exception:
            opt = base_opt
    else:
        opt = base_opt

    best_cost = np.inf
    best_image = None
    for i in range(iterations):
        with tf.GradientTape() as tape:
            J_content = content_loss(content, generated)
            J_style = total_style_loss(style, generated)
            J_total = content_weight * J_content + style_weight * J_style

        # If using LossScaleOptimizer, scale the loss before taking gradients and unscale grads
        if mixed_precision_enabled and hasattr(opt, 'get_scaled_loss'):
            scaled_loss = opt.get_scaled_loss(J_total)
            grads = tape.gradient(scaled_loss, generated)
            grads = opt.get_unscaled_gradients(grads)
        else:
            grads = tape.gradient(J_total, generated)

        opt.apply_gradients([(grads, generated)])

        if J_total < best_cost:
            best_cost = J_total
            best_image = generated.numpy()

        # display progress every n iterations set by display_interval (and at iteration 1)
        if (i + 1) % display_interval == 0 or i == 0:
            print(
                f"Iteration {i+1}: total loss={float(J_total):.4e}, style={float(J_style):.4e}, content={float(J_content):.4e}"
            )
            try:
                img = deprocess_img(generated.numpy())
                plt.figure(figsize=(6, 6))
                plt.imshow(img)
                plt.axis("off")
                plt.show()
            except Exception as e:
                print(f"Could not display image at iteration {i+1}: {e}")

    return best_image

if use_gpu:
    with tf.device('/GPU:0'):
        vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
        vgg.trainable = False
else:
    vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
    vgg.trainable = False

content_model = Model(inputs=vgg.input, outputs=vgg.get_layer(content_layer[0]).output)
style_models = [
    Model(inputs=vgg.input, outputs=vgg.get_layer(layer).output) for layer in style_layers
]

# Equal weight for each style layer in the total style cost
weight_of_layer = 1.0 / len(style_models)


# helper functions for fallbacks
def choose_first_image_in_dir(path):
    exts = ['*.jpg', '*.jpeg', '*.png']
    for ext in exts:
        files = glob.glob(os.path.join(path, ext))
        if files:
            return files[0]
    return None


def create_dummy_content(path, size=(512, 512)):
    # create a simple gradient content image
    gradient = np.linspace(0, 255, num=size[1], dtype=np.uint8)
    img = np.tile(gradient, (size[0], 1))
    img = np.stack([img, img, img], axis=2)
    Image.fromarray(img).save(path)
    print(f"Created dummy content image at {path}")


def create_dummy_style(path, size=(512, 512)):
    # create a colorful random style image
    img = np.random.randint(0, 256, size=(size[0], size[1], 3), dtype=np.uint8)
    Image.fromarray(img).save(path)
    print(f"Created dummy style image at {path}")


# Ensure content/style files exist (fallback to directory search or dummy images)
if os.path.isdir(content_path):
    found = choose_first_image_in_dir(content_path)
    if found:
        content_path = found
    else:
        create_dummy_content('./content.jpg')
        content_path = './content.jpg'
elif not os.path.exists(content_path):
    found = choose_first_image_in_dir('.')
    if found:
        content_path = found
        print(f"Using found content image: {content_path}")
    else:
        create_dummy_content(content_path)

if os.path.isdir(style_path):
    found = choose_first_image_in_dir(style_path)
    if found:
        style_path = found
    else:
        create_dummy_style('./style.jpg')
        style_path = './style.jpg'
elif not os.path.exists(style_path):
    found = choose_first_image_in_dir('.')
    if found and found != content_path:
        style_path = found
        print(f"Using found style image: {style_path}")
    else:
        create_dummy_style(style_path)


# Run the training loop and save the best result
best = training_loop(content_path, style_path, iterations=iterations, use_content_init=content_init)

# Save the best image to output_path
# Will overwrite if file exists so before running again, rename or move previous output.
if best is not None:
    output_img = deprocess_img(best)
    Image.fromarray(output_img).save(output_path)
    print(f"Saved stylized image to {output_path}")

