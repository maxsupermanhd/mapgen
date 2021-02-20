# Map generator for [DandyBot](https://github.com/true-grue/DandyBot)


Run gen.py


Working:
 - Map layout generation
 - Start/end position (possible)
 - Map rooms difficulty progression
 - Placeholders for tile-rooms
 - Layout scaling


TODO:
 - Hire someone to make tiles
 - Do actual tile matching algorithm

Customize:
 - Layout size, generation steps and offsets can be changed in arguments to `GenerateLayout` function
 - Stripping of layout is optional, however it will consume more space+time
 - Placeholder-rooms are completly optional, size can be changed in `RealizeLayout` function
