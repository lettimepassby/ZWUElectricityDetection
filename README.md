# ZWUElectricityDetection
浙江万里学院电量检测脚本，接口基于易校园  
需要配置
1. PUSHPLUS_TOKEN(可选)
2. openId
3. wxArea
4. areaNo
5. buildNo
6. roomNo
### PUSHPLUS_TOKEN
找到pushplus，注册绑定就好，当然你也可以不用pushplus
### 剩下五个
2~6获取方式一致，首先你要用一个抓包工具这里我选择的是fiddler，使用教程请自行百度。打开学校查电量的网页（不是万里的话可以自行找找）
![image](https://github.com/user-attachments/assets/88767fdc-35aa-43de-a298-511bff28df33)
打开抓包软件，开启抓包
![image](https://github.com/user-attachments/assets/13c6dfb3-aef6-4afa-bd15-8bf46269b801)
在开启抓包的状态下点击缴电费
![image](https://github.com/user-attachments/assets/69c4b5f9-db9c-429b-a36b-5d1c5898580e)
找到对的url链接，复制下来（右键-复制-仅复制网址），在浏览器中打开
![image](https://github.com/user-attachments/assets/0b9b7dd8-21da-4ece-8c1e-243cdb52f683)
这时候应该显示这样的界面，按下f12打开开发者工具找到网络选项，然后点击对应房间的充值按钮
![image](https://github.com/user-attachments/assets/28098ed2-e3da-44a4-a9ce-46478c579851)
找到对应的访问请求，点击进去看负载
![image](https://github.com/user-attachments/assets/6995d113-209a-49c9-86a9-4797db0a76ad)
填入脚本即可。
可搭配青龙面板进行定期执行查询
