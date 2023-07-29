from xolpanel import *

@bot.on(events.CallbackQuery(data=b'create-trojan'))
async def create_trojan(event):
  async def create_trojan_(event):
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
    cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" | add-tr'
    try:
      a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
      await event.respond("**User Already Exist**")
    else:
      today = DT.date.today()
      later = today + DT.timedelta(days=int(exp))
      b = [x.group() for x in re.finditer("trojan://(.*)",a)]
      print(b)
      domain = re.search("@(.*?):",b[0]).group(1)
      uuid = re.search("trojan://(.*?)@",b[0]).group(1)
      msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**❤️⟨ Xray/Trojan Account ⟩❤️**
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{user}`
**» User Quota  :** `{pw} GB`
**» port TLS     :** `443`
**» Port NTLS    :** `80`
**» Port GRPC    :** `443`
**» OpenClash TLS:** `443`
**» port TLS CDN :** `443`
**» Port NTLS CDN:** `80`
**» Port GRPC CDN:** `443`
**» User ID     :** `{uuid}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `bug.com/trojan`
**» Path NLS     :** `bug.com/trojan`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `trojan-grpc`
**━━━━━━━━━━━━━━━━**
**» 💯Link TLS   : **
`{b[0]}`
**━━━━━━━━━━━━━━━━**
**» 💯Link NTLS    :** 
`{b[2].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**» 💯Link GRPC  :** 
`{b[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**» Yaml Clash Ws:** `http://{DOMAIN}:81/{user}-TRTLS.yaml`
**━━━━━━━━━━━━━━━━**
**» CDN TLS      :** `http://{DOMAIN}:81/{user}-TRTLSCDN.yaml`
**━━━━━━━━━━━━━━━━**
**» CDN No TLS   :** `http://{DOMAIN}:81/{user}-TRNOTLSCDN.yaml`
**━━━━━━━━━━━━━━━━**
**» CDN Grpc     :** `http://{DOMAIN}:81/{user}-TRGrpcCDN.yaml`
**━━━━━━━━━━━━━━━━**
**» Link QR      :** `https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=${b[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
      await event.respond(msg)
  chat = event.chat_id
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await create_trojan_(event)
  else:
    await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'cek-trojan'))
async def cek_trojan(event):
  async def cek_trojan_(event):
    cmd = 'bot-cek-tr'.strip()
    x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    print(x)
    z = subprocess.check_output(cmd, shell=True).decode("utf-8")
    await event.respond(f"""

{z}

**Shows Logged In Users Trojan**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await cek_trojan_(event)
  else:
    await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-trojan'))
async def trial_trojan(event):
  async def trial_trojan_(event):
    cmd = f'printf "%s\n" | trialtrojan'
    try:
      a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
      await event.respond("**User Already Exist**")
    else:
      #today = DT.date.today()
      #later = today + DT.timedelta(days=int(exp))
      b = [x.group() for x in re.finditer("trojan://(.*)",a)]
      print(b)
      remarks = re.search("#(.*)",b[0]).group(1)
      domain = re.search("@(.*?):",b[0]).group(1)
      uuid = re.search("trojan://(.*?)@",b[0]).group(1)
      msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**❤️⟨ Xray/Trojan Account ⟩❤️**
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{remarks}`
**» User Quota  :** `1 GB`
**» port TLS     :** `443`
**» Port NTLS    :** `80`
**» Port GRPC    :** `443`
**» OpenClash TLS:** `443`
**» port TLS CDN :** `443`
**» Port NTLS CDN:** `80`
**» Port GRPC CDN:** `443`
**» User ID     :** `{uuid}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `bug.com/trojan`
**» Path NLS     :** `bug.com/trojan`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `trojan-grpc`
**━━━━━━━━━━━━━━━━**
**» 💯Link TLS   : **
`{b[0]}`
**━━━━━━━━━━━━━━━━**
**» 💯Link NO WS  :** 
`{b[2].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**» 💯Link GRPC  :** 
`{b[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**» Yaml Clash Ws:** `http://{DOMAIN}:81/{user}-TRTLS.yaml`
**━━━━━━━━━━━━━━━━**
**» CDN TLS      :** `http://{DOMAIN}:81/{user}-TRTLSCDN.yaml`
**━━━━━━━━━━━━━━━━**
**» CDN No TLS   :** `http://{DOMAIN}:81/{user}-TRNOTLSCDN.yaml`
**━━━━━━━━━━━━━━━━**
**» CDN Grpc     :** `http://{DOMAIN}:81/{user}-TRGrpcCDN.yaml`
**━━━━━━━━━━━━━━━━**
**» Link QR  :** `https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=${b[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `60 Minutes`
**◇━━━━━━━━━━━━━━━━━◇**
"""
      await event.respond(msg)
  chat = event.chat_id
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await trial_trojan_(event)
  else:
    await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'renew-tr'))
async def ren_trojan(event):
  async def ren_trojan_(event):
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
    cmd = f'printf "%s\n" "{user}" {exp} | renew-tr'
    try:
      a = subprocess.check_output(cmd, shell=True).decode("utf-8")
    except:
      await event.respond("**User Not Found**")
    else:
      msg = f"""**Successfully Renewed {user} {exp}**"""
      await event.respond(msg)
  chat = event.chat_id
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await ren_trojan_(event)
  else:
    await event.answer("Akses Ditolak",alert=True)
    
@bot.on(events.CallbackQuery(data=b'delete-trojan'))
async def delete_trojan(event):
  async def delete_trojan_(event):
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
    cmd = f'printf "%s\n" "{user}" | del-tr'
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
    await delete_trojan_(event)
  else:
    await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trojan'))
async def trojan(event):
  async def trojan_(event):
    inline = [
[Button.inline("[TRIAL TROJAN]","trial-trojan"),
Button.inline("[CREATE TROJAN]","create-trojan")],
[Button.inline("[CHECK TROJAN]","cek-trojan"),
Button.inline("[DELETE TROJAN]","delete-trojan")],
[Button.inline("[]RENEW TROJAN]","renew-trojan")],
[Button.inline("‹🇮🇩 Main Menu 🇮🇩›","menu")]]
    z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
    msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**     ◇👑⟨ TROJAN MANAGER ⟩👑◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» 🤖Service:** `TROJAN`
**» 🤖Hostname/IP:** `{DOMAIN}`
**» 🤖ISP:** `{z["isp"]}`
**» 🤖Country:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
    await event.edit(msg,buttons=inline)
  sender = await event.get_sender()
  a = valid(str(sender.id))
  if a == "true":
    await trojan_(event)
  else:
    await event.answer("Access Denied",alert=True)
