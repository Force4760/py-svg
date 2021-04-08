from ..inner import InnerShape

class Text(InnerShape):
    def __init__(self,canvas,text:str="", x:float=0, y:float=0, dx:float=0, dy:float=0):
        super().__init__("text", canvas)
        self.inner += text
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rotate = []
        self.adjust = "spacing"
        self.length = 0

    def set_text(self,text:str):
        self.inner = text

    def set_adjust(self, adjust:str):
        self.adjust = adjust
    
    def set_length(self,length:float):
        self.length = length

    def set_rotate(self,rotate:list):
        self.rotate = rotate

    def add_rotate(self, number:float):
        self.rotate.append(number)
    
    def rem_rotate(self, index:int):
        del self.rotate[index]

    def draw(self):
        info = f"<{self.tag}"
        info += f" x='{self.x}'"
        info += f" y='{self.y}'"
        info += f" dx='{self.dx}'"
        info += f" dy='{self.dy}'"

        if self.rotate:
            info += f""" rotate='{" ".join(self.rotate)}' """

        if self.length:
            info += f""" textLength='{self.length}'' """
        
        info += f""" lengthAdjust='{self.adjust}' """

        self.inner = [self.text]

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info

class TSpan(Text):
    def __init__(self, canvas, text:str='', x:float=0, y:float=0, dx:float=0, dy:float=0):
        super().__init__(canvas, text=text, x=x, y=y, dx=dx, dy=dy)
        self.tag = "tspan"

class TextPath(InnerShape):
    """https://developer.mozilla.org/en-US/docs/Web/SVG/Element/textPath"""
    def __init__(self,canvas,text:str="", href:str=""):
        super().__init__("textPath", canvas)
        self.inner += text
        self.adjust = "spacing"
        self.length = 0
        self.href = href
        self.method = "align"
        self.side = "left"
        self.spacing = "exact"
        self.offset = 0

    def set_text(self,text:str):
        self.inner = text

    def set_adjust(self, keyword:str):
        self.adjust = adjust
    
    def set_length(self,length:float):
        self.length = length

    def set_method(self,keyword:str):
        self.mathod = keyword

    def set_side(self,keyword:str):
        self.side = keyword

    def set_spacing(self,keyword:str):
        self.spacing = keyword

    def set_offset(self,length:float):
        self.offset = length


    def draw(self):
        info = f"<{self.tag}"
        info += f""" href="{self.href}" """

        if self.adjust != "spacing":
            info += f""" lengthAdjust='{self.adjust}' """

        if self.method != "align":
            info += f""" method="{self.method}" """
        
        if self.side != "left":
            info += f""" side="{self.side}" """
        
        if self.spacing != "exact":
            info += f""" spacing="{self.spacing}" """
        
        if self.offset:
            info += f""" startOffset="{self.offset}" """
        
        if self.length:
            info += f""" textLength="{self.length}" """
        

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info