import socket
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class PhoneSenderApp(App):
    def build(self):
        # 创建一个垂直排列的手机布局
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 1. 提示标签
        layout.add_widget(Label(text="🚀 局域网文件传输助手 (手机端)", font_size=20))
        
        # 2. 输入电脑 IP 的框（把默认值改成你 Mac 的局域网 IP）
        self.ip_input = TextInput(text='192.168.1.X', hint_text='请输入电脑的局域网 IP', multiline=False)
        layout.add_widget(self.ip_input)
        
        # 3. 模拟要发送的文件路径（暂时填一个测试文本）
        self.file_input = TextInput(text='test.txt', hint_text='要发送的文件名/路径', multiline=False)
        layout.add_widget(self.file_input)
        
        # 4. 发送按钮
        send_btn = Button(text='点我发送文件到电脑', background_color=(0, 0.7, 1, 1))
        send_btn.bind(on_press=self.send_file)
        layout.add_widget(send_btn)
        
        # 5. 状态显示栏
        self.status_label = Label(text="状态: 等待发送...", font_size=14)
        layout.add_widget(self.status_label)
        
        return layout

    def send_file(self, instance):
        pc_ip = self.ip_input.text.strip()
        file_to_send = self.file_input.text.strip()
        port = 9999
        
        # 临时创建一个虚拟测试文件，防止文件不存在报错
        if not os.path.exists(file_to_send):
            with open(file_to_send, 'w') as f:
                f.write("哈喽！这是从手机端通过 Socket 管道传输过来的机密文件！")

        try:
            self.status_label.text = "正在连接电脑..."
            # 建立 TCP 套接字管道连向电脑
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((pc_ip, port))
            
            # 第一步：把文件名甩过去（告诉电脑要接稳什么球）
            client.send(os.path.basename(file_to_send).encode('utf-8'))
            
            # 稍微歇个 0.1 秒，防止粘包
            import time
            time.sleep(0.1)
            
            # 第二步：把文件的二进制流源源不断塞过去
            with open(file_to_send, 'rb') as f:
                client.sendall(f.read())
                
            self.status_label.text = "🎉 发送成功！去电脑下载文件夹看看吧！"
            client.close()
        except Exception as e:
            self.status_label.text = f"❌ 失败: {e}\n请检查IP或Wi-Fi"

if __name__ == '__main__':
    PhoneSenderApp().run()