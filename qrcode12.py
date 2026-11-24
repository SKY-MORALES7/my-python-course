import qrcode

data = "https://carleton.ca/engineering-design/beng-first-year/fy-supplies/"
qr = qrcode.make(data)
qr.save('fy_supplies.png')