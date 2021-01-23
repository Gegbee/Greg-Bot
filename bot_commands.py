import serial, discord, time, sys

port = "COM5"
baudrate = 9600
arduino = serial.Serial(port, baudrate)

# async def c_log(message):
#     msg = message.content.replace("/log ", "", 1)
#     response = f'Sending {msg} to Arduino at serial port {port} by {message.author}'
#     if len(response) > 2000:
#         await message.channel.send("*Your sentence was too long!* Type something shorter you fuckass.")
#     else:
#         arduino.write(("w" + msg).encode())
#         audit_file = open("logBotAudit.txt", "a")
#         audit_file.write(response + "\n")
#         audit_file.close()
#         await message.channel.send(response)
#         time.sleep(1)

async def c_help(message):
    await message.channel.send("```Type: **/move** *time (ms) + direction (f or b)* to move my robot forward. \n Type: **/turn** *rotation (deg) + direction (r or l)* to turn my robot.```")
#    await message.channel.send("```Type: **/log-Your Message** to print it on my Arduino LCD Display.\nType: **/rotate-degrees-axis** to rotate the servo motor.```")

async def c_move(message):
    msg = message.content.split(" ")
    try:
        ms = str(int(msg[1]))
        d = msg[2]
        if d in ["f", "b"]:
            arduino.write(("m" + ms + "|" + d).encode())
            await message.channel.send(f'Moving robot {ms} centimeters.')
    except:
        await message.channel.send("*Incorrect input values*. Do **/help** if you need help.")

async def c_turn(message):
    msg = message.content.split(" ")
    try:
        degrees = str(int(msg[1]))
        d = mesg[2]
        if d in ["r", "l"]:
            arduino.write(("t" + degrees + "|" + d).encode())
            await message.channel.send(f'Turning robot {degrees} degrees.')
    except:
        await message.channel.send("*Incorrect input values*. Do **/help** if you need help.")

# async def c_rotate(message):
#     message_array = message.content.split(' ')
#     try:
#         degrees = str(int(message_array[1]))
#         axis = message_array[2]
#         if axis in ["y"]:
#             arduino.write(("r" + axis + degrees).encode())
#             await message.channel.send(f'Rotating the {axis} axis servo to {degrees}')
#             time.sleep(1)
#         else:
#             await message.channel.send("*Please specify a correct axis to rotate*, (y or x).")
#     except:
#         await message.channel.send("*Incorrect input values*. Do **/help** if you need help.")

