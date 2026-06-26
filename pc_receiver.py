import socket
import os

def start_pc_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定本地所有网络接口，设置端口为 9999
    server.bind(('0.0.0.0', 9999))
    server.listen(1)
    
    print(f"🌟 电脑端就绪！请确保手机和 Mac 在同一个 Wi-Fi 下。")
    print(f"📌 监听端口: 9999\n等待手机连接...")

    while True:
        try:
            conn, addr = server.accept()
            print(f"\n🤝 成功建立连接！来自手机的 IP: {addr[0]}")
            
            # 先接收文件名
            file_name = conn.recv(1024).decode('utf-8').strip()
            if not file_name:
                continue
            print(f"📦 准备接收文件: {file_name}")
            
            # 开始接收文件数据并写入本地下载文件夹
            save_path = os.path.join(os.path.expanduser("~"), "Downloads", f"received_{file_name}")
            with open(save_path, 'wb') as f:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)
            
            print(f"🎉 传输完成！文件已安全保存至 Mac 的下载文件夹:\n👉 {save_path}")
            conn.close()
            print("\n等待下一次连接...")
            
        except Exception as e:
            print(f"❌ 发生错误: {e}")
            break

if __name__ == "__main__":
    start_pc_server()