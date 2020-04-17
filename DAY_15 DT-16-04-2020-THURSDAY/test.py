from PIL import Image,ImageFilter

img = Image.open("./4.5 pikachu.jpg.jpg")
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png","png")
print(filtered_img)
#Image._show()
box = (100,200,200,300)
region = filtered_img.crop(box)
region.save("crop.png","png")

img = Image.open("./6.1 astro.jpg.jpg")
#print(img.size)
new_img = img.resize((200,300))
new_img.save('thumb')
