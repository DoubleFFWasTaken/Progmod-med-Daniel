from PIL import Image
import glob
 
# Create the frames
frames = []
n = 1
while n < 100:
    imgs = glob.glob(f"nbody_{n}.png")

    n += 1


    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
 
    # Save into a GIF file that loops forever
    frames[0].save('nbody_GIF.gif', format='GIF', append_images=frames[1:], save_all=True, duration=300, loop=0)
