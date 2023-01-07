from PIL import Image, ImageFilter

# 获取图片基础信息
image1 = Image.open('guido.jpg')
# print(image.format, image.size, image.mode)
# image.show()

# 裁剪图像
rect = 80, 20, 310, 360
# image1.crop(rect).show()

# 生成缩略图
# size = 128, 128
# image.thumbnail(size)
# image.show()

# 缩放和粘贴图像
# image2 = Image.open('test.jpg')
# guido_head = image2.crop(rect)
# width, height = guido_head.size
# image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
# image1.show()

# 旋转和翻转
# image1.rotate(180).show()
# image1.transpose(Image.FLIP_LEFT_RIGHT).show()

# 操作像素
# for x in range(80, 310):
#     for y in range(20, 360):
#         image1.putpixel((x, y), (128, 128, 128))
# image1.show()

# 滤镜效果
# image1.filter(ImageFilter.CONTOUR).show()