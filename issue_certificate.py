from PIL import Image, ImageDraw, ImageFont
import pandas as pd

df = pd.read_excel('arquivo.xlsx')
name_list = df['Name'].to_list()


for i in name_list:
	im = Image.open('teste.png')
	d = ImageDraw.Draw(im)
	location = (0,0)
	text_color = (0,0,0)
	font = ImageFont.truetype("Arial.TTF", 150)
	d.text(location,i,fill=text_color,font=font)
	im.save("certificate_"+i+".pdf")
