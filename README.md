# Arduino_Printer
A simple printer using H-Bridges, an Arduino Uno, and two CD drives

Welcome to the Arduino Printer Project.

MATERIALS NEEDED:
1. Circuit (2 H-Bridge circuits)
	1. 4 2n2222 transistors
	2. 4 2n3906 transistors
	3. 8 diodes
	4. 8 10k transistors
	5. 9V battery
	6. File printer_schematic.asc (LTspice file)
2. Printer
	1. 2 CD drives (Just the motor with the gear box that connects to the lazer on a sliding rod)
	2. 1 Pen
	3. Hot Glue
	4. Wood for mounting the CD drives
3. Software
	1. Arduino Uno
	2. File Printer script.py
	3. File Arduino Printer.ino

HOW TO USE: Once you have assembled the printer, schematic, and properly connected it to your arduino, you are ready to go.
1. Giving the printer a shape to draw
	1. Run printer_script.py. A small window will appear. Using the arrow keys, draw the shape you would like your printer to draw up.
	2. Once you are done, press space. The program will close and your drawing will be saved in a cache.
2. Start up the printer. Make sure your arduino Uno is plugged into your computer. Double check that your circuit is connected to the write pins on your arduino board.
	1. Manually adjust the CD drives so the pen sits in the middle of your paper.
	2. Start up Arduino_Printer.ino and click 'Upload'.
	3. Watch your printer print out your drawing!
