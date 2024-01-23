import requests  
import time  
  
def test_live_stream(url):  
    try:  
        response = requests.get(url, stream=True)  
        response.raise_for_status()  # 如果请求失败则抛出异常  
        response.close()  
        return True  
    except requests.exceptions.RequestException as e:  
        print(f"Error fetching the live stream: {e}")  
        return False  
  
def fetch_live_streams():  
    # 假设你有多个直播源接口的URL列表  
    live_stream_urls = [  
        "https://xhdwc.tk/tvlive.txt",  
        # ... 其他直播源URLs ...  
    ]  
    live_streams = []  
    for url in live_stream_urls:  
        if test_live_stream(url):  
            live_streams.append(url)  
    return live_streams  
  
def update_list_file(live_streams):  
    with open("list.txt", "w") as file:  
        for stream in live_streams:  
            file.write(f"{stream}\n")  
  
if __name__ == "__main__":  
    live_streams = fetch_live_streams()  
    update_list_file(live_streams)  
    print("List updated successfully!")