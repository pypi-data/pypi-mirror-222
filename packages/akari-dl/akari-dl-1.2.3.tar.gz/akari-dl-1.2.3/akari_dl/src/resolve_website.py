import akari_dl
from akari_dl import src

def resolve_website(self):
  """
    Resolve working url and login for user-specified website.
  """
  print(f"Connecting to {self.name}...")

  if isinstance(self.domains, tuple):
    i = 0
    connected = False
    for url in self.domains:
      try:
        while not connected:
          i += 1
          self.response = self.session.get(f"https://{url}")
          if self.response.status_code == 200:
            connected = True
      except Exception:
        try:
          print(f"Failed to connect to {self.name} via https://{url}... trying https://{self.domains[i]}.")
        except IndexError:
          print(f"Failed to connect to {self.name}.")
          exit()
  else:
    if akari_dl.conf_parser["debug"]:
      self.response = self.session.get(f"https://{self.domains}")
    else:
      try:
        self.response = self.session.get(f"https://{self.domains}")
      except Exception:
        print(f"Failed to connect to {self.name}.")
        exit()

  if akari_dl.conf_parser["debug"]:
    src.log_response(self.response)
  print(f"Connected to {self.response.url[:-1]}.")

  return self.response.url[:-1]
