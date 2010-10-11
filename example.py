#!/usr/bin/python
import viewsonicpro8100

# Create a projector object attached to the first USB Serial port.
projector = viewsonicpro8100.ViewsonicPro8100('/dev/ttyUSB0')

# Turn the projector on
projector.writeCommandFromName('Power ON')

# Select the first HDMI input
projector.writeCommandFromName('HDMI-1')

# Done watching a movie, shut it off.
projector.writeCommandFromName('Power OFF')

