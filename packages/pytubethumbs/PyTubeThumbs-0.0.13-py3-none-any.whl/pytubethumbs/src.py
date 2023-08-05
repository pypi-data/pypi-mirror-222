
from typing import Literal
from PIL import Image, ImageDraw, ImageFont


class PyTubeThumbs:
    def __init__(self, title : str, out_path : str, background : str = 'white') -> None:
        self.height = 720
        self.width = 1280
        self.title = title
        self.out_path = out_path
        
        # create a new image
        self.image = Image.new(
            mode = 'RGB',
            size = (self.width, self.height),
            color = background
        )
        
        self.thumb = ImageDraw.Draw(self.image)
        
    
        
    def add_text(self, text: str, size: int, color, font_path: str,
                 pos: tuple = (20, 20),
                 align: Literal['left', 'center', 'right'] = "left"):
        
        # draw text on thumb
        self.thumb.text(
            pos,
            text, 
            font = ImageFont.truetype(font_path, size),
            align = align,
            fill = color,
        )
        
    
    def add_image(self, image_path : str, pos : tuple, size : tuple = (50, 50)):
        img = Image.open(image_path).resize((size[0], size[1]))
        self.image.convert("RGBA")
        img.convert("RGBA")
        self.image.paste(img, pos, img)
        
    def template_text_2imgs(self,text: str,font_path : str,img1_path: str,img2_path: str,count: int = 1):
        self.add_text(
            pos=(80, 50),
            text = text, 
            size = 70,
            color = 'black',
            font_path=font_path,
        )

        self.add_image(img1_path, pos = (100, 250), size = (140, 140))
        self.add_image(img2_path, pos = (280, 250), size = (140, 140))
        
    
        
    def show_thumb(self):
        self.image.show()
    
    def save_thumb(self):
        self.image.save(f'{self.out_path}/{self.title}.jpg')
        
