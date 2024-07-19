from bing_image_downloader.downloader import download

query_string = 'face looking at camera'

download(query_string, limit=50,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)