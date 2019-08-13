import pygame
from PIL import Image

def load_tiles(tilemap_file, tilesize):
	tilemap = Image.open(tilemap_file)
	map_width, map_height = tilemap.size
	tiles = []
	for y in range(0, map_height, tilesize):
		for x in range(0, map_width, tilesize):
			tiles.append(tilemap.crop((x, y, x+tilesize, y+tilesize)))

	return tiles

def main():
	tiles = load_tiles('dirtmap.png', 32)
	for tile in tiles:
		tile.show()

if __name__ == '__main__':
	main()