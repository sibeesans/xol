from xolpanel import *

@bot.on(events.CallbackQuery(data=b'create-vless'))
async def create_vless(event):
  async def create_vless_(event):
    async with bot.conversation(chat) as user:
      await event.respond('**Username:**')
      user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
      user = (await user).raw_text
    async with bot.conversation(chat) as pw:
      await event.respond("**Quota:**")
      pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
      pw = (await pw).raw_text
    async with bot.conversation(chat) as exp:
      await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline(" 3 Day ","3"),
Button.inline(" 7 Day ","7")],
[Button.inline(" 30 Day ","30"),
Button.inline(" 60 Day ","60")]])
      exp = exp.wait_event(events.CallbackQuery)
      exp = (await exp).data.decode("ascii")
    await event.edit("`Processing Crate Premium Account`")
    time.sleep(1)
    await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
    time.sleep(0)
    await event.edit("`Processing... 100%\n█████████████████████████ `")
    time.sleep(1)
    await event.edit("`Wait.. Setting up an Account`")
    cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" | add-vless'
    try:
      a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
      await event.respond("**User Already Exist**")
    else:
      today = DT.date.today()
      later = today + DT.timedelta(days=int(exp))
      x = [x.group() for x in re.finditer("vless://(.*)",a)]
      print(x)
      # remarks = re.search("#(.*)",x[0]).group(1)
      # domain = re.search("@(.*?):",x[0]).group(1)
      uuid = re.search("vless://(.*?)@",x[0]).group(1)
      # path = re.search("path=(.*)&",x[0]).group(1)
      msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ Xray/Vless Account ⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{user}`
**» Host Server :** `{DOMAIN}`
**» User Quota  :** `{pw} GB`
**» port TLS     :** `443`
**» Port NTLS    :** `80`
**» Port Grpc    :** `443`
**» Openclash TLS:** `443`
**» OpenClash NTLS:** `80`
**» port TLS CDN :** `443`
**» Port NTLS CDN:** `80`
**» Port Grpc CDN:** `443`
**» NetWork      :** `(WS) or (gRPC)`
**» User ID      :** `{uuid}`
**» Path Vless   :** `/vless `
**» Path Dynamic :** `http://BUG.COM/vless `
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS   : **
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link GRPC  :**
`{x[2].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Yaml Clash Ws   :** `http://{DOMAIN}:81/{user}-VlessTLS.yaml`
**◇━━━━━━━━━━━━━━━━━◇**
**» Yaml Clash NO Ws:** `http://{DOMAIN}:81/{user}-VlessNTLS.yaml`
**◇━━━━━━━━━━━━━━━━━◇**
**» CDN TLS         :** `http://{DOMAIN}:81/{user}-VlessTLSCDN.yaml`
**◇━━━━━━━━━━━━━━━━━◇**
**» CDN NTLS        :** `http://{DOMAIN}:81/{user}-VlessNTLSCDN.yaml`
**◇━━━━━━━━━━━━━━━━━◇**
**» CDN Grpc        :** `http://{DOMAIN}:81/{user}-VlessGrpcCDN.yaml`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link QR         :** `https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=${x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**» @Dragon_Emperor999
**◇━━━━━━━━━━━━━━━━━◇**
"""
      await event.respond(msg)
  chat = event.chat_id
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await create_vless_(event)
  else:
    await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'cek-vless'))
async def cek_vless(event):
  async def cek_vless_(event):
    cmd = 'bot-cek-vless'.strip()
    x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    print(x)
    z = subprocess.check_output(cmd, shell=True).decode("utf-8")
    await event.respond(f"""

{z}

**Shows Logged In Users Vless**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await cek_vless_(event)
  else:
    await event.answer("Access Denied",alert=True)
    
@bot.on(events.CallbackQuery(data=b'renew-vless'))
async def ren_vless(event):
  async def ren_vless_(event):
    async with bot.conversation(chat) as user:
      await event.respond('**Username:**')
      user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
      user = (await user).raw_text
    async with bot.conversation(chat) as exp:
      await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline(" 3 Day ","3"),
Button.inline(" 7 Day ","7")],
[Button.inline(" 30 Day ","30"),
Button.inline(" 60 Day ","60")]])
      exp = exp.wait_event(events.CallbackQuery)
      exp = (await exp).data.decode("ascii")
    await event.edit("`Processing Crate Premium Account`")
    time.sleep(1)
    await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
    time.sleep(0)
    await event.edit("`Processing... 100%\n█████████████████████████ `")
    time.sleep(1)
    await event.edit("`Wait.. Setting up an Account`")
    cmd = f'printf "%s\n" "{user}" {exp} | renew-vless'
    try:
      a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
      await event.respond("**User Not Found**")
    else:
      msg = f"""**Successfully Renewes {user} {exp} Days**"""
      await event.respond(msg)
  chat = event.chat_id
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await ren_vless_(event)
  else:
    await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-vless'))
async def delete_vless(event):
  async def delete_vless_(event):
    async with bot.conversation(chat) as user:
      await event.respond('**Username:**')
      user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
      user = (await user).raw_text
    await event.edit("`Processing Crate Premium Account`")
    time.sleep(1)
    await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
    time.sleep(1)
    await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
    time.sleep(0)
    await event.edit("`Processing... 100%\n█████████████████████████ `")
    time.sleep(1)
    await event.edit("`Wait.. Setting up an Account`")
    cmd = f'printf "%s\n" "{user}" | del-vless'
    try:
      a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
      await event.respond("**User Not Found**")
    else:
      msg = f"""**Successfully Deleted**"""
      await event.respond(msg)
  chat = event.chat_id
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await delete_vless_(event)
  else:
    await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-vless'))
async def trial_vless(event):
  async def trial_vless_(event):
    async with bot.conversation(chat) as exp:
      cmd = f'printf "%s\n"| trialvless'
    try:
      a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
      await event.respond("**User Already Exist**")
    else:
      #today = DT.date.today()
      #later = today + DT.timedelta(days=int(exp))
      x = [x.group() for x in re.finditer("vless://(.*)",a)]
      print(x)
      remarks = re.search("#(.*)",x[0]).group(1)
      # domain = re.search("@(.*?):",x[0]).group(1)
      uuid = re.search("vless://(.*?)@",x[0]).group(1)
      # path = re.search("path=(.*)&",x[0]).group(1)
      msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ Xray/Vless Account ⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks      :** `{remarks}`
**» Host Server  :** `{DOMAIN}`
**» port TLS     :** `443`
**» Port NTLS    :** `80`
**» Port Grpc    :** `443`
**» Openclash TLS:** `443`
**» OpenClash NTLS:** `80`
**» port TLS CDN :** `443`
**» Port NTLS CDN:** `80`
**» Port Grpc CDN:** `443`
**» NetWork      :** `(WS) or (gRPC)`
**» User ID      :** `{uuid}`
**» Path Vless   :** `/vless `
**» Path Dynamic :** `http://BUG.COM/vless `
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS   : **
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link GRPC  :**
`{x[2].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until :** `60 Minutes`
**» @Dragon_Emperor999
**◇━━━━━━━━━━━━━━━━━◇**
"""
      await event.respond(msg)
  chat = event.chat_id
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await trial_vless_(event)
  else:
    await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'vless'))
async def vless(event):
  async def vless_(event):
    inline = [
[Button.inline("[TRIAL VLESS]","trial-vless"),
Button.inline("[CREATE VLESS]","create-vless")],
[Button.inline("[CHECK VLESS]","cek-vless"),
Button.inline("[DELETE VLESS]","delete-vless")],
[Button.inline("[RENEW VLESS]","renew-vless")],
[Button.inline("‹ Main Menu ›","menu")]]
    z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
    msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**    ◇⟨ VLESS MANAGER ⟩◇**
**◇━━━━━━━━━━━━━━━━━◇**
** 🤖 Service:** `VLESS`
** 🤖 Hostname/IP:** `{DOMAIN}`
** 🤖 ISP:** `{z["isp"]}`
** 🤖 Country:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
    await event.edit(msg,buttons=inline)
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await vless_(event)
  else:
    await event.answer("Access Denied",alert=True)
