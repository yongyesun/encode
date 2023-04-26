#！/bin/bash
wget -q https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted/ss.txt -O ./nodeencode96
wget -q https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted/vless.txt -O ./nodeencode97
wget -q https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted/trojan.txt -O ./nodeencode98
wget -q https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted/ssr.txt -O ./nodeencode99
wget -q https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted/vmess.txt -O ./nodelist
base64 ./nodelist > nodeencode100 -w 0 || echo "It is a test"
mv ./nodeencode100 ./subconverter
mv ./nodeencode99 ./subconverter
mv ./nodeencode98 ./subconverter
mv ./nodeencode97 ./subconverter
mv ./nodeencode96 ./subconverter
echo "url=nodeencode100|nodeencode99|nodeencode98|nodeencode97|nodeencode96" >> node_profile.ini
