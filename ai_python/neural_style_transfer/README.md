The neural_style_transfer.py file implements neural style transfer introduced in the paper A Neural Algorithm of Artistic Style by Gatys et al. https://arxiv.org/pdf/1508.06576.
You can download and run the code yourself provided that you have the Python libraries used in the program.
You also need a content and style image and you need to add their file path to the content_path and style_path variables.
You can also edit the output_path variable as well if you want to change the name or location of the generated image.

The images included in this folder are what I used to test and run my program. The eiffel_picasso_transfer.jpg was generated over 50 iterations using a 1e-3 content/style weighting ratio and using the content image as the generated image's initial starting point. The process took ~10 minutes to complete.

The eiffel_picasso_transfer_300.jpg image was generated over 300 iterations using a 1e-4 content/style weighting ratio and using the content image as the generated image's initial starting point. This took ~40 minutes to finish.

The eiffel_picasso_transfer_random_300.jpg image was generated over 300 iterations using a 1e-3 content/style weighting ratio and used random initialization for the generated image. This took ~40 minutes.

I found this project really interesting and fun to play around with after completing the code. 
I would have liked to generate a better image using random initialization by increasing the number of iterations as I believe it would give more style to the final image but, I may run out of patience before it would finish. 
There may be more optimizations that could be added to this code but, I believe this was a good proof of concept for me and I am happy how it turned out.

All other documentation can be found in my code in the neural_style_transfer.py file.
