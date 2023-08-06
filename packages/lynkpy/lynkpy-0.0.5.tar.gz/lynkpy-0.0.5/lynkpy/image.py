from PIL import Image
import os

class DPIChanger:
    def __init__(self, file=None, folder=None, dpi=None, name=None, ext=None, new_location=None):
        self.file = file
        self.name = name if name else file
        self.ext = ext if ext else 'png'
        self.dpi = dpi
        self.new_location = new_location
        self.folder = folder
        
    def _check(self):
        if (self.file is None) and (self.folder is None):
            raise ValueError("both file and folder cannot be empty")

        if self.dpi is None:
            raise ValueError("Value of dpi cannot be empty")
        
        if type(self.dpi) != tuple:
            raise ValueError("Value of dpi should be in tuple e.g. (500, 500)")
        
    def _get_name(self):
        name, _ = os.path.splitext(self.name)
        return name
    
    def _file(self):
        image = Image.open(self.file)
        name = self._get_name()
        image.save(f"{name}.{self.ext}", dpi=self.dpi)
        
    def _folder(self):
        for img in os.listdir(self.folder):
            name, _ = os.path.splitext(img)
            image = Image.open(f"{self.folder}/{img}")
            if self.new_location is not None:
                os.makedirs(self.new_location, exist_ok=True)
                image.save(f"{self.new_location}/{name}.{self.ext}", dpi=self.dpi)
            else:
                os.makedirs(f"{self.folder}_dpi_changed", exist_ok=True)
                image.save(f"{self.folder}_dpi_changed/{name}.{self.ext}", dpi=self.dpi)
    
    def process(self):
        self._check()
        if self.file is not None:
            self._file()
        if self.folder is not None:
            self._folder()