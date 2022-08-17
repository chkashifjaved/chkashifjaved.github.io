import os

def main():
  print("Hello from GitHub Actions!")
  token = os.environ.get("AUTH_TOKEN")
  print(token)
  
if __name__ == '__main__':
  main()
