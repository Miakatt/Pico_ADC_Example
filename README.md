# Pico_ADC_Example
An example of transferring data from the Raspberry Pico ADC to a host PC for a random stranger on the internet! :) 
Uses the ADC0 on GPIO26 

Upload pico_ADC.py to your Pico device using Thonney
Open host_ADC.py and set the COM port as required (line 24). 
Run pico_ADC.py via Thonney. You should see a stream of numbers in the Shell window. 
Close Thonney (to free up the serial port)
Run host_ADC.py (I use PyCharm but any standard IDE should work - Not Thonney though. That's for Micropython)
You should see a plot of live ADC data. To test, connect a wire from GPIO26 to ground (pin 31) and ground (Pin 38) or Vcc (Pin40)
