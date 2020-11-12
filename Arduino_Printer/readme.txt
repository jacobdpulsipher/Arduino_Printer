Welcome to the Arduino Printer Project.

MATERIALS NEEDED:
    >Circuit (2 H-Bridge circuits)
	.4 2n2222 transistors
	.4 2n3906 transistors
	.8 diodes
	.8 10k transistors
	.9V battery
	.File printer_schematic.asc (LTspice file)
    >Printer
	.2 CD drives (Just the motor with the gear box that connects to the lazer on a sliding rod)
	.1 Pen
	.Hot Glue
	.Wood for mounting the CD drives
    >Software
	.Arduino Uno
	.File Printer script.py
	.File Arduino Printer.ino

HOW TO USE:
Once you have assembled the printer, schematic, and properly connected it to your arduino, you are ready to go.
1. Giving the printer a shape to draw
	.Run printer_script.py. A small window will appear. Using the arrow keys, draw the shape you would like your printer to draw up.
	.Once you are done, press space. The program will close and your drawing will be saved in a cache.
2. Start up the printer
	.Make sure your arduino Uno is plugged into your computer. Double check that your circuit is connected to the write pins on your arduino board.
	.Manually adjust the CD drives so the pen sits in the middle of your paper.
	.Start up Arduino_Printer.ino and click 'Upload'.
	.Watch your printer print out your drawing. 
