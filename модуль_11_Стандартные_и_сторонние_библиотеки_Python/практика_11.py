from PIL import Image, ImageDraw, ImageFont


class PostMaker:
    def __init__(self, name_photo):
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 2, self.h // 2))

    def paste(self, name_photo):
        paste_image = Image.open(name_photo)
        paste_image = paste_image.resize((paste_image.size[0] // 4, paste_image.size[1] // 4))
        self.image.paste(paste_image, (70, 340))

    def upgrade(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('ofont.ru_Czizh.ttf', size=50)
        draw.text((140, 35), text, font=font, fill=(139, 0, 0))
        self.image.show()
        self.image.save('novay_otkritka.jpg')


image = PostMaker('ribka-3.jpg')
image.paste('chernoe.jpg')
image.upgrade('Танцуй будто никто не видит')

