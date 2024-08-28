import concurrent.futures
import multiprocessing
import requests

def downloadFile(url, name):
    print(f"starting Downloading {name}")
    response=requests.get(url)
    open(f"Python Photos/{name}.jpg", "wb").write(response.content)
    print(f"finished Downloading {name}")

"""if __name__=="__main__":
    url="https://picsum.photos/3500/2200"

    pros=[]
    for i in range(5):
        #downloadFile(url,i)
        p=multiprocessing.Process(target=downloadFile,args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()"""

if __name__=="__main__":
    url="https://picsum.photos/3500/2200"


    with concurrent.futures.ProcessPoolExecutor() as executor:
        l = [i for i in range(5)]
        l2 = [i for i in range(5)]
        results = executor.map(downloadFile, url, l, l2)
        for r in results:
            print(r)