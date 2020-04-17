from PIL import Image,ImageFilter

img = Image.open("./6.1 astro.jpg.jpg")
#print(img.size)
new_img = img.resize((200,300))
new_img.save('thumb')
