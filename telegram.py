import time
import socket
from config.local import TELEGRAM
from urllib import request, parse

last_message_time = None
my_ip = None
url = 'https://api.telegram.org/bot%s/sendMessage' % TELEGRAM["bot_token"]


def send_message(warnings):
  global last_message_time
  now = time.time()
  if last_message_time is not None and (now - last_message_time < TELEGRAM["message_interval"]):
    return

  mapper = lambda item: '<b>%s</b> is used over <b>%s%%</b>' % (item[0], item[1])
  warning_str = ', '.join(list(map(mapper, warnings)))
  message = 'Server %s: %s' % (get_ip(), warning_str)

  body = {
    "chat_id": TELEGRAM["chat_id"],
    "text": message,
    "parse_mode": 'html'
  }
  try:
    data = parse.urlencode(body).encode()
    req = request.Request(url, data=data)
    print('Sending message: %s' % message)
    resp = request.urlopen(req)
    last_message_time = time.time()
  except Exception as error:
    print(error)


def get_ip():
  global my_ip
  if my_ip is None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
      s.connect(("8.8.8.8", 80))
      my_ip = s.getsockname()[0]
    except Exception:
      my_ip = socket.gethostname()
    finally:
      s.close()
  return my_ip
