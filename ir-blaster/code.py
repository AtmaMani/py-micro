import pulseio
import board
import adafruit_irremote
from adafruit_circuitplayground.express import cpx
# import neopixel

# led = neopixel.NeoPixel(board.NEOPIXEL, 1)

# Create a 'pulseio' input, to listen to infrared signals on the IR receiver
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
pwm = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulseout = pulseio.PulseOut(pwm)

encoder = adafruit_irremote.GenericTransmit(header=[9500, 4500], one=[550, 550],
                                            zero=[550, 1700], trail=0)

# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()

while True:
    pulses = decoder.read_pulses(pulsein)
    try:
        # Attempt to convert received pulses into numbers
        received_code = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        # print("NEC repeat!")
        continue
    except adafruit_irremote.IRDecodeException as e:
        # Something got distorted or maybe its not an NEC-type remote?
        # print("Failed to decode: ", e.args)
        continue

    print("NEC Infrared code received: ", received_code)
    if received_code == [31, 31, 31, 224]:
        print("Received NEC Vol+")
    if received_code == [255, 2, 127, 128]:
        print("Received NEC Play/Pause")
    if received_code == [31, 31, 47, 208]:
        print("Received NEC Vol-")

    if cpx.button_a:
        print("Button A pressed! \n")
        cpx.red_led = True
        encoder.transmit(pulseout, [31, 31, 31, 224])
        cpx.red_led = False
        # wait so the receiver can get the full message
    if cpx.button_b:
        print('Button B pressed! \n')
        cpx.green_led = True
        encoder.transmit(pulseout, [31,31,47,208])
        cpx.green_led = False