import pvporcupine
from pvrecorder import PvRecorder


def wake_word():
    access_key = "v/O2pCxy02jiIRNubRhr+McSeIVB9nfrlPggp0g7TYbRLWxLLYVzow=="
    keyword_paths  = ["D:/created programs/DAEMON/wake_word_detection//Daemon_en_windows_v2_2_0.ppn"]
    keywords = ['Daemon']
    porcupine = pvporcupine.create(access_key=access_key, keywords=keywords, keyword_paths=keyword_paths)
    recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

    try:
        print("="*20)
        recoder.start()


        while True:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0:
                print(f"Detected {keywords[keyword_index]}")
                return True


    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()

