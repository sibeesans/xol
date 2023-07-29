from xolpanel import *

@bot.on(events.CallbackQuery(data=b'trial-ssh'))
async def trial_ssh(event):
	async def trial_ssh_(event):
		user = "trialX"+str(random.randint(100,1000))
		pw = "1"
		exp = "1"
		cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user}'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ Trial SSH Account ⟩**
**━━━━━━━━━━━━━━━━**
**» Host:** `{DOMAIN}`
**» Host SlowDNS:** `{SLDOMAIN}`
**» Username:** `{user.strip()}`
**» Password:** `{pw.strip()}`
**━━━━━━━━━━━━━━━━**
**» Host SlowDNS     :** `{SLDOMAIN}`
**» Pub Key       :** `{PUB}`
**» Port OpenSSH     :** `22`
**» Port Dropbear    :** `8585, 143, 109`
**» Port Dropbear WS :** `443, 109`
**» Port SSH WS      :** `80`
**» Port SSH SSL WS  :** `443`
**» Port SSH NSSL WS :** `8880`
**» Port SSL/TLS     :** `447, 777`
**» Port OVPN SSL    :** `110`
**» Port OVPN TCP    :** `1194`
**» Port OVPN UDP    :** `2200`
**» Port OHP SSH     :** `8686`
**» Port OHP Dropbear:** `8585`
**» Port OHP OpenVpn :** `8787`
**» Port UDP Custom  :** `1-65535`
**» Port UDP Custom  :** `56-65535`
**» Port UDP Custom  :** `10000-10150`
**» Proxy Squid      :** `3128, 8000`
**» BadVPN UDP       :** `7100-7900`
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ OpenVPN & OHP  ⟩**
**» OpenVPN TCP      :** `1194 http://{DOMAIN}:81/client-tcp-1194.ovpn'
**» OpenVPN UDP      :** `2200 http://{DOMAIN}:81/client-udp-2200.ovpn'
**» OpenVPN SSL      :** `110 http://{DOMAIN}:81/client-tcp-ssl.ovpn'
**» OHP OVPN         :** `8787 http://{DOMAIN}:81/client-tcp-ohp1194.ovpn'
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ Payload WS  ⟩**
`GET / HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf][crlf]`
**⟨ Payload WS SSL ⟩**
`GET wss:/// HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf]Connection: Keep-Alive[crlf][crlf]`
**━━━━━━━━━━━━━━━━**
**» Expired Until:** `{later}`
**» 🤖@Dragon_Emperor999**
**━━━━━━━━━━━━━━━━**
"""
			inline = [
[Button.url("[ Contact ]","t.me/Dragon_Emperor999"),
Button.url("[ Channel ]","t.me/JengkolTunneling12")]]
			await event.respond(msg,buttons=inline)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
