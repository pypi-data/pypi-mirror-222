from openi.apis import DatasetFile,OpeniAPI
from openi.utils.file_utils import calculateMD5, read_file_chunk, get_file_chunk_info
import json
from concurrent.futures import ThreadPoolExecutor


def upload_with_tqdm(
        _file: DatasetFile,
        api: OpeniAPI,
        chunks: list,
        cluster: str = "NPU"
):
    _progress = len(_file.chunks) - len(chunks)
    with tqdm(total=_file.size, leave=True, unit='B',
              unit_scale=True, unit_divisor=1000,
              desc=f"{_file.filename} ({cluster}): uploading",
              bar_format='{desc}{percentage:3.0f}%|{bar}{r_bar}') as pbar:
        # checkpoint
        pbar.update(_file.max_chunk_size * _progress)
        # upload chunks
        for n in chunks:
            (start_position, chunk_size) = _file.chunks[n]
            url = api.get_multipart_url(_file, n, chunk_size)
            data = read_file_chunk(_file.filepath, start_position, chunk_size)
            api.put_upload(url, data, _file.upload_type)
            pbar.update(chunk_size)

def func():
    owner, repository = "chenzh01", "test"
    upload_type, cluster = "1","NPU"
    file = "./output/data.zip"

    _file = DatasetFile(file, owner, repository, upload_type)
    _file.chunks = get_file_chunk_info(max_chunk_size=_file.max_chunk_size, filesize=_file.size)
    _file.md5 = calculateMD5(_file.filepath)

    api = OpeniAPI(endpoint="http://192.168.207.34:8110/api/v1", token="4fc54cd1443f90bd09522cabd0bca981671bbc48")
    try:
        _file.dataset_id = api.get_dataset_repo(owner, repository)["data"][0]["id"]
    except Exception as e:
        raise ValueError(
            f'`❌ {owner}/{repository}` dataset does not exist, '
            f'please create dataset in the repo before uploading files.')

    _get_chunks = api.get_chunks(_file)
    print(json.dumps(_file.__dict__, indent=4))

    # upload starts
    if _get_chunks["uuid"] != '':
        if _get_chunks["uploaded"] == '1':
            raise ValueError(
                f'❌ Upload failed: {_file.filename}` ({cluster}) '
                f'already exists, cannot be uploaded again.')

        else:
            print('continue upload...')

            _file.uuid, _file.upload_id = _get_chunks["uuid"], _get_chunks["uploadID"]
            uploaded_chunks = [int(i.split('-')[0]) for i in _get_chunks["chunks"].split(',') if i != '']
            uploaded_chunks = sorted(uploaded_chunks)[:-1]
            continue_chunks = [i for i in _file.chunks if i not in uploaded_chunks]
            continue_chunks = sorted(continue_chunks)

            upload_with_tqdm(_file, api, continue_chunks, cluster)

    else:
        print('start new upload...')

        _file.uuid, _file.upload_id = api.new_multipart(_file)
        upload_chunks = list(_file.chunks.keys())

        upload_with_tqdm(_file, api, upload_chunks, cluster)


from tqdm import tqdm
import os

def download_with_tqdm(response, output_file):
    #response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KB

    with tqdm(total=total_size, leave=True, unit='B',
              unit_scale=True, unit_divisor=1000, #ascii=' |=',
              desc=f"Downloading {os.path.basename(output_file)[:20]:<20}(…): ",
              bar_format='{desc}{percentage:3.0f}%|{bar}{r_bar}') as pbar:
        with open(output_file, 'wb') as f:
            for data in response.iter_content(block_size):
                pbar.update(len(data))
                f.write(data)

def download_file(_uuid, upload_type,_output):
    _response = api.download_attachments(_uuid, upload_type)
    download_with_tqdm(_response, _output)

def type_to_cluster(upload_type: int):
    return "NPU" if upload_type == 0 else "GPU"


repo = "chenzh/quickstart"
owner, repository = repo.split("/")[0], repo.split("/")[1]
upload_type = 0
file = "iris.zip"
save_path = "./output"
all = True
api = OpeniAPI(endpoint="https://openi.pcl.ac.cn/api/v1", token="ee06cd664b63b8075f2ee13ecc28edd6d38f5fa7")

# print(f'downloading...')
if not all:
    _dataset_info = api.get_dataset_repo(owner, repository, upload_type)
    target_repo = {"ownerName": owner, "name": repository}
    _dataset = next((d for d in _dataset_info["data"] if d["repo"] == target_repo), None)
    _dataset_file = next((d for d in _dataset["attachments"] if d["name"] == file), None)
    _uuid = _dataset_file["uuid"]

    _dir = os.getcwd() if save_path is None else save_path
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    _output = os.path.join(_dir, file)

    download_file(_uuid, upload_type, _output)
else:
    _files = list()
    for t in range(2):
        _dataset_info = api.get_dataset_repo(owner, repository, upload_type = t)
        target_repo = {"ownerName": owner, "name": repository}
        _dataset_files = next((d for d in _dataset_info["data"] if d["repo"] == target_repo), None)["attachments"]
        _files += [(d["uuid"], d["name"], d["type"]) for d in _dataset_files]

    _dir = os.getcwd() if save_path is None else save_path
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    _fnames = ['(' + type_to_cluster(f[2]) + ')'+ f[1] for f in _files]
    _outputs = [os.path.abspath(os.path.join(_dir, f)) for f in _fnames]

    _tasks = list()
    for i in  range(len(_files)):
        _task = dict()
        _task["_uuid"] = _files[i][0]
        _task["upload_type"] = _files[i][2]
        _task["_output"] = _outputs[i]
        _tasks.append(_task)

    with ThreadPoolExecutor() as executor:
        # Submit download tasks to the executor
        future_to_task = [executor.submit(download_file, **task) for task in _tasks]

