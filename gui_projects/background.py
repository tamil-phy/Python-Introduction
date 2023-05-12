from guizero import App, Text, Picture 
app = App("Display", layout="grid")
text = Text(app,"Wanted!")
text.text_size = 25
dog = Picture(app, image="image.jpg", grid=[1,1,1] )
app.bg = "white"
app.display()