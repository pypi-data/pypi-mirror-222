import sys
sys.path.insert(-2, "D:\\workspace\\bilibili\\src")
print(sys.path)
from bilibili_download.main import Main
main = Main()
main.main()
