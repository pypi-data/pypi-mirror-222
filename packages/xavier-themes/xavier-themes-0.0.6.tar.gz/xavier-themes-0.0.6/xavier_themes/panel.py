import os,re
from xavier_themes.emoji import Emoji
data = []
emoticon=[]

def Panel(text,width=None,style=None):
	return "\n".join(str(text) for text in printer(text,width,style))

def printer(text,width,style):
	texti = cek_hex(text.replace("[","").replace("]",""))
	text = replace_hex(text)
	if len(emoji(text))>0:
		if "\n" in text:
			data.append(coloring(style) +"╭"+"─" *int(screen_size(width)-2)+"╮")
			for txt in texti.split("\n"):
				if cek_emoji(txt):
					minus = cek_emoji(txt)
					data.append(coloring(style) +"│"+ txt +" " *int(screen_size(width)-2-len(replace_ansi(txt))-len(minus)) + coloring(style) +"│")
				else:
					data.append(coloring(style) +"│"+ txt +" " *int(screen_size(width)-2-len(replace_ansi(txt))) + coloring(style) +"│")
			data.append(coloring(style) +"╰"+"─" *int(screen_size(width)-2)+"╯")
		else:
			data.append(coloring(style) +"╭"+"─" *int(screen_size(width)-2)+"╮")
			data.append(coloring(style) +"│"+ texti +" " *int(screen_size(width)-2-len(text)-len(emoji(text))) + coloring(style) +"│")
			data.append(coloring(style) +"╰"+"─" *int(screen_size(width)-2)+"╯")
	else:
		if "\n" in texti:
			data.append(coloring(style) +"╭"+"─" *int(screen_size(width)-2)+"╮")
			for txt in texti.split("\n"):
				data.append(coloring(style) +"│"+ txt +" " *int(screen_size(width)-2-len(replace_ansi(txt))) + coloring(style) +"│")
			data.append(coloring(style) +"╰"+"─" *int(screen_size(width)-2)+"╯")
		else:
			data.append(coloring(style) +"╭"+"─" *int(screen_size(width)-2)+"╮")
			data.append(coloring(style) +"│"+ texti +" " *int(screen_size(width)-2-len(text)) + coloring(style) +"│")
			data.append(coloring(style) +"╰"+"─" *int(screen_size(width)-2)+"╯")
	return data
	
def screen_size(width):
	if width == None:
		width = os.get_terminal_size().columns
	else:
		width = width
	return int(width)
		
def cek_emoji(text):
	emo = [c for c in text if c in emoticon]
	return emo
	
def emoji(text):
	data = sorted((v, k) for k, v in Emoji.items())
	for emoji, kode in data:
		emoticon.append(emoji)
	em = [c for c in text if c in emoticon]
	return em
	
def coloring(color):
	color_data = {"RED": "\x1b[91m","GREEN": "\x1b[92m","YELLOW": "\x1b[93m","BLUE": "\x1b[94m","ORANGE": "\x1b[95m","CYAN": "\x1b[96m","WHITE": "\x1b[97m","BLACK": "\x1b[30m","DEFAULT": "\x1b[39m","BOLD": "\x1b[1m"}
	if color == None:
		return color_data.get("DEFAULT")
	else:
		if "BOLD" in color:
			return color_data.get("BOLD")+color_data.get(color.split(" ")[1])
		else:
			return color_data.get(color)

def replace_hex(text):
	regex = re.findall(r"#[a-fA-F0-9]{6}", text)
	if regex:
		z = 0
		for gex in regex:
			text = text.replace(f"[{gex}]", "")
			z += 1
		return text
	else:
		return text
		
def replace_ansi(text):
	regex = re.findall(r"\x1b\[38;2;\d{1,3};\d{1,3};\d{1,3}m",text)
	if regex:
		z = 0
		for gex in regex:
			text = text.replace(f"{gex}", "")
			z += 1
		return text
	else:
		return text
	
def cek_hex(text):
	regex = re.findall(r"#[a-fA-F0-9]{6}", text)
	if regex:
		z = 0
		for hex_color in regex:
			r, g, b = hex_to_rgb(hex_color.replace("#", ""))
			ansi_color = rgb_to_ansi(r, g, b)
			text = text.replace(regex[z], ansi_color)
			z += 1
		return text
	else:
		return text
	
def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16)  for i in (0, 2, 4))

def rgb_to_ansi(r,g,b):
    return f"\x1b[38;2;{r};{g};{b}m"
    
