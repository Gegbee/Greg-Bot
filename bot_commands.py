import serial, discord, time, sys

port = "COM5"
baudrate = 9600
arduino = serial.Serial(port, baudrate)

async def c_log(message):
    message_array = message.content.split('-')
    requested_text = message_array[1]
    response = f'Sending {requested_text} to Arduino at serial port {port} by {message.author}'
    if len(response) > 2000:
        await message.channel.send("*Your sentence was too long!* Type something shorter you fuckass.")
    else:
        arduino.write(("t" + requested_text).encode())
        audit_file = open("logBotAudit.txt", "a")
        audit_file.write(response + "\n")
        audit_file.close()
        await message.channel.send(response)
        time.sleep(1)

async def c_help(message):
    await message.channel.send("```Type: **/log-Your Message** to print it on my Arduino LCD Display.\nType: **/rotate-degrees-axis** to rotate the servo motor.```")

async def c_rotate(message):
    message_array = message.content.split('-')
    try:
        degrees = str(int(message_array[1]))
        axis = message_array[2]
        if axis in ["y"]:
            arduino.write(("m" + axis + degrees).encode())
            await message.channel.send(f'Rotating the {axis} axis servo to {degrees}')
            time.sleep(1)
        else:
            await message.channel.send("*Please specify a correct axis to rotate*, (y or x).")
    except:
        await message.channel.send("*Incorrect input values*. Do **/help** if you need help.")

