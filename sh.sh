#！/bin/bash
wget -q https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/res/nod-0.txt -O ./nodeencode11
wget -q https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/res/nod-1.txt -O ./nodeencode12
wget -q https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/o/node.txt -O ./nodeencode13
wget -q https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/all2 -O ./nodeencode14
wget -q https://raw.githubusercontent.com/yongyesun/encode/rename/sub/sub_merge_base64.txt -O ./nodeencode15
mv ./nodeencode11 ./subconverter
mv ./nodeencode12 ./subconverter
mv ./nodeencode13 ./subconverter
mv ./nodeencode14 ./subconverter
mv ./nodeencode15 ./subconverter         
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
echo "url=nodeencode100|nodeencode99|nodeencode98|nodeencode97|nodeencode96|nodeencode11|nodeencode12|nodeencode13|nodeencode14|nodeencode15|nodeencode|nodeencode1" >> node_profile.ini
